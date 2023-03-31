from django.shortcuts import (
    render, redirect,
    reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def wish_list(request):
    """
    This view function displays the user's wish list of products.
    It uses Django's built-in Paginator class to display the products
    in sets of 12 per page.

    Parameters:
    request (HttpRequest): The HTTP request sent by the user.

    Returns:
    HttpResponse: The HTTP response containing the rendered wishlist
    template with the paginated results.

    """
    # Get all the products in the user's wishlist
    new_wish = Product.objects.filter(wishlist=request.user)

    # Paginate the results to display 12 products per page
    paginator = Paginator(new_wish, 12)
    page = request.GET.get("page")
    try:
        new_wish = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, default to the first page
        new_wish = paginator.page(1)

    # Set up the dictionary of variables to pass to the template
    template = 'profiles/wishlist.html'
    context = {
        'new_wish': new_wish,
        'page': page,
    }

    # Render the template with the variables
    return render(request, template, context)


@login_required
def wish_add_remove(request, product_id, slug):
    """
    This view function adds or removes a product from the user's wishlist.
    It first gets the product object using the provided product_id and slug.
    If the user has already added the product to their wishlist, it removes
    it from the list. Otherwise, it adds it to the list.

    Parameters:
    request (HttpRequest): The HTTP request sent by the user.
    product_id (int): The ID of the product to add/remove from the wishlist.
    slug (str): The slug of the product to add/remove from the wishlist.

    Returns:
    HttpResponseRedirect: A redirect response to the product detail page
    for the product that was added/removed.

    """
    # Get the product object based on the provided ID and slug
    product = get_object_or_404(Product, id=product_id, slug=slug)

    # If the user has already added the product to their wishlist,
    # remove it. Otherwise, add it.
    if product.wishlist.filter(id=request.user.id).exists():
        product.wishlist.remove(request.user)
    else:
        product.wishlist.add(request.user)

    # Redirect the user back to the product detail page
    return redirect(reverse('products:product_detail',
                            args=[product.id, product.slug]))


@login_required
def profile(request):
    """
    This view function displays the user's profile.
    If a POST request is received, it updates the user's profile
    information using the submitted form.
    If a GET request is received, it displays the user's profile
    information and order history.

    Parameters:
    request (HttpRequest): The HTTP request sent by the user.

    Returns:
    HttpResponse: The HTTP response containing the rendered profile
    template with the user's profile information and order history.
    """
    # Get the user's UserProfile object
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # If a POST request is received, update the user's profile
        # information with the submitted form
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        # If a GET request is received, display the user's profile
        # information and order history
        form = UserProfileForm(instance=profile)

    # Get the user's order history
    orders = profile.orders.all()

    # Set up the dictionary of variables to pass to the template
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    # Render the template with the variables
    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    This view function displays the details of a previously completed order.

    Parameters:
    request (HttpRequest): The HTTP request sent by the user.
    order_number (str): The order number of the previously completed order.

    Returns:
    HttpResponse: The HTTP response containing the rendered
    checkout_success template with the details of the completed order.
    """
    # Get the order object based on the provided order number
    order = get_object_or_404(Order, order_number=order_number)

    # Display a message to the user about the completed order
    messages.info(request, f'This is a past confirmation for order number \
{order_number}. A confirmation email was sent on the order date.')

    # Set up the dictionary of variables to pass to the template
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    # Render the template with the variables
    return render(request, template, context)
