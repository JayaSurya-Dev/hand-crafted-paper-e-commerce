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
    """ View to render cart contents page """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """
    Add a specified quantity of a product to the shopping cart. If the
    product has a specified size,
    add the product and its size to the cart. If the product does not
    have a specified size, add the
    quantity to the existing quantity in the cart or add the product
    to the cart if it doesn't already
    exist.

    Args:
        request: The HTTP request object.
        item_id: The ID of the product to add to the cart.

    Returns:
        Redirects to the previous page with success or error
        messages displayed, or raises a 404 error
        if the product with the given ID does not exist.

    Raises:
        Http404: If the product with the given ID does not exist.
    """

    # get the product object based on its ID
    product = get_object_or_404(Product, pk=item_id)
    # get the URL to redirect to after adding to cart
    redirect_url = request.POST.get('redirect_url')

    try:
        # get the quantity of the product to add to cart
        quantity = int(request.POST.get('quantity'))
    except ValueError as e:
        # display an error message if quantity is not a valid integer
        messages.error(
                    request,
                    f'Quantity must be a digit.')
        # redirect back to the previous page
        return redirect(redirect_url)

    # initialize the size to None
    size = None

    # if a product size was specified, get it from the form data
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # get the current cart from the session, or initialize an empty cart
    cart = request.session.get('cart', {})

    # if the product has a specified size
    if size:
        # if the product is already in the cart
        if item_id in list(cart.keys()):
            # if the size is already in the cart for this product
            if size in cart[item_id]['items_by_size'].keys():
                # add the quantity to the existing size quantity
                cart[item_id]['items_by_size'][size] += quantity
                # display a success message indicating the updated quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} \
quantity to {cart[item_id]["items_by_size"][size]}')
            else:
                # add a new size to the cart for this product
                cart[item_id]['items_by_size'][size] = quantity
                # display a success message indicating the added item
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your cart')
        else:
            # add the product and size to the cart
            cart[item_id] = {'items_by_size': {size: quantity}}
            # display a success message indicating the added item
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your cart')
    else:
        # if the product does not have a specified size
        if item_id in list(cart.keys()):
            # add the quantity to the existing quantity
            cart[item_id] += quantity
            # display a success message indicating the updated quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            # add the product to the cart
            cart[item_id] = quantity
            # display a success message indicating the added item
            messages.success(request, f'Added {product.name} to your cart')

    # update the cart in the session
    request.session['cart'] = cart
    # redirect back to the previous page
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    and update the user's cart session.

    Args:
        request (HttpRequest): The current request object.
        item_id (int): The ID of the product to adjust the quantity for.

    Returns:
        HttpResponseRedirect: Redirects the user back to the cart view.

    Raises:
        None.

    """

    # Get the product associated with the given item ID, or raise a 404 error
    product = get_object_or_404(Product, pk=item_id)

    try:
        # Try to get the quantity from the POST data in the request object
        quantity = int(request.POST.get('quantity'))
    except ValueError as e:
        # If the quantity is not a valid integer, add an error message
        # and  redirect back to the cart view
        messages.error(
                    request,
                    f'Quantity must be a digit.')
        return redirect(reverse('cart:view_cart'))

    # Initialize the size to None
    size = None

    # Check if a size was specified in the POST data
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get the current cart dictionary from the user's session,
    # or initialize it to an empty dictionary
    cart = request.session.get('cart', {})

    # If a size was specified
    if size:
        # If the quantity is greater than zero
        if quantity > 0:
            # Update the quantity for the specified size in the cart dictionary
            cart[item_id]['items_by_size'][size] = quantity
            # Add a success message indicating the size and quantity that were
            # updated
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to \
{cart[item_id]["items_by_size"][size]}')
        else:
            # If the quantity is zero or less, remove the size from the cart
            # dictionary
            del cart[item_id]['items_by_size'][size]
            # If there are no more sizes in the items_by_size dictionary, #
            # remove the entire product from the cart
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            # Add a success message indicating the size that was removed
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your cart')
    # If no size was specified
    else:
        # If the quantity is greater than zero
        if quantity > 0:
            # Update the quantity for the specified product ID in the cart.
            # dictionary
            cart[item_id] = quantity
            # Add a success message indicating the quantity that was updated
            messages.success(
                request,
                f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            # If the quantity is zero or less, remove the product from the
            # cart dictionary
            cart.pop(item_id)
            # Add a success message indicating the product that was removed
            messages.success(request, f'Removed {product.name} from your cart')

    # Save the updated cart dictionary back to the user's session
    request.session['cart'] = cart
    # Redirect the user back to the cart view
    return redirect(reverse('cart:view_cart'))


def remove_from_cart(request, item_id):
    """
    This function retrieves the user's shopping cart from the session,
    removes the specified item from the cart, and updates the
    session accordingly. If the item is successfully removed, a success message
    is added to the user's session. If an error occurs, an error message
    is added to the user's session.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the product to remove from the cart.

    Returns:
        HttpResponse: An HTTP response with a status code of 200 on success,
        or a status code of 500 on failure.

    Raises:
        None

    """

    # Get the product from the database using its ID
    product = Product.objects.get(pk=item_id)

    try:
        # Try to retrieve the size of the product from the request
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        # Get the user's cart from the session or set it to an empty
        # dictionary if it doesn't exist
        cart = request.session.get('cart', {})

        if size:
            # If the size is specified, remove the item with the specified
            # size from the cart
            del cart[item_id]['items_by_size'][size]
            # If the cart no longer contains any items with the specified
            # product ID, remove the product from the cart entirely
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            # Add a success message to the user's session indicating that the
            # item was removed
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your cart')
        else:
            # If the size is not specified, remove the entire product from the
            # cart
            cart.pop(item_id)
            # Add a success message to the user's session indicating that the
            # item was removed
            messages.success(request, f'Removed {product.name} from your cart')

        # Set the updated cart back into the session
        request.session['cart'] = cart
        # Return an HTTP response with a status code of 200 to indicate success
        return HttpResponse(status=200)

    except Exception as e:
        # If an error occurs, add an error message to the user's session and
        # return an HTTP response with a status code of 500
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
