from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ view to render cart contents page """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """ View a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError as e:
        messages.error(
                    request,
                    f'ValueError: {e} - Quantity must be a digit.')
        return redirect(redirect_url)

    cart = request.session.get('cart', {})
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} \
                    quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        quantity = int(request.POST.get('quantity'))
    except ValueError as e:
        messages.error(
                    request,
                    f'ValueError: {e} - Quantity must be a digit.')
        return redirect(reverse('cart:view_cart'))

    cart = request.session.get('cart', {})
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to \
                {cart[item_id]["items_by_size"][size]}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('cart:view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    product = Product.objects.get(pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
