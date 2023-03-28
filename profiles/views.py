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
    new_wish = Product.objects.filter(wishlist=request.user)
    paginator = Paginator(new_wish, 12)
    page = request.GET.get("page")
    try:
        new_wish = paginator.page(page)
    except PageNotAnInteger:
        new_wish = paginator.page(1)
    template = 'profiles/wishlist.html'
    context = {
        'new_wish': new_wish,
        'page': page,
    }
    return render(request, template, context)


@login_required
def wish_add_remove(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug)
    if product.wishlist.filter(id=request.user.id).exists():
        product.wishlist.remove(request.user)
    else:
        product.wishlist.add(request.user)

    return redirect(reverse('products:product_detail',
                            args=[product.id, product.slug]))


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the \
            form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
