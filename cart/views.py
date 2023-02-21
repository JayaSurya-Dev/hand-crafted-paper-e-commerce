from django.shortcuts import render


def view_cart(request):
    """ view to render cart contents page """

    return render(request, "cart/cart.html")
