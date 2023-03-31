from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse,
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    A view function for caching checkout data when a user is making a
    payment using Stripe.

    Parameters:
    - request: the HTTP request object containing the payment data

    Returns:
    - An HTTP response with a status code of 200 if successful, or
    - An HTTP response with a status code of 400 and an error message if
    an error occurs
    """

    try:
        # Get the payment intent ID from the POST data
        pid = request.POST.get('client_secret').split('_secret')[0]

        # Get the Stripe API key from settings
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Modify the payment intent with the given ID and add metadata to it
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })

        # Return an HTTP response with a status code of 200 if successful
        return HttpResponse(status=200)

    except Exception as e:
        # If an error occurs, display an error message to the user and return
        # an HTTP response with a status code of 400
        messages.error(
            request, 'Sorry, your payment cannot be processed right now. \
Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Render the checkout page, handle the form submission and process
    the payment using Stripe.
    """

    # Get the Stripe API keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Get the cart data from the session
        cart = request.session.get('cart', {})

        # Get the data submitted in the form
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        # Validate the form data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Create a new order object with the validated form data
            # but don't save it to the database yet.
            order = order_form.save(commit=False)

            # Add the payment intent ID to the order object
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid

            # Save the original cart data in the order object
            order.original_cart = json.dumps(cart)

            # Save the order object to the database
            order.save()

            # Create order line items for each product in the cart
            for item_id, item_data in cart.items():
                try:
                    # Get the product object for the current item
                    product = Product.objects.get(id=item_id)

                    # Create an order line item object for the current item
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'] \
                                                                .items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    # If the product no longer exists, delete the order and
                    # redirect to the cart page
                    messages.error(request, "One of the products in your cart \
wasn't found in our database. Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('cart:view_cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout:checkout_success',
                        args=[order.order_number]))
        else:
            # If the form is invalid, display an error message
            messages.error(request, 'There was an error with your form. \
Please double check your information.')
    else:
        # If the request is not a POST request, render the checkout page
        # with the form and payment intent
        cart = request.session.get('cart', {})
        if not cart:
            # If there are no items in the cart, display an error message
            # and redirect to the product list page
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('products:product_list'))

        # Calculate total and create stripe payment intent
        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info the user maintains in
        # their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            # if the user's profile does not exist, create a new order form.
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        # if the user is not authenticated, create a new order form.
        else:
            order_form = OrderForm()
    # if the Stripe public key is missing, show a warning message
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
Did you forget to set it in your environment?')

    # set the template for the checkout page
    template = 'checkout/checkout.html'
    # create a context dictionary with the order form, Stripe public key,
    # and PaymentIntent client secret
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    View function that handles successful checkouts.

    Arguments:
    request -- An HttpRequest object that contains information about
    the current request.
    order_number -- A string representing the order number of the
    successfully processed order.
    """
    # Check if the user wants to save their shipping information for
    # future purchases
    save_info = request.session.get('save_info')

    # Get the order object that matches the provided order_number
    order = get_object_or_404(Order, order_number=order_number)

    # If the user is authenticated, attach their user profile to the order
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    # If the user chose to save their shipping information, update
    # their profile with the information from the order
    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_town_or_city': order.town_or_city,
            'default_county': order.county,
            'default_postcode': order.postcode,
            'default_country': order.country,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    # Create a success message to display to the user
    messages.success(request, f'Order successfully processed! \
Your order number is {order_number}. A confirmation \
email will be sent to {order.email}.')

    # If the user had a cart in the session, delete it
    if 'cart' in request.session:
        del request.session['cart']

    # Render the checkout_success.html template with the order object
    # as the context variable
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
