from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request):
    """
    Display a list of all products, including sorting and search queries
    Parameters:
        request (HttpRequest): the HTTP request object
    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    products = Product.objects.all()

    template = ["products/list.html"]
    context = {
        'products': products,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """
    Display an individual product details
    Parameters:
        request (HttpRequest): the HTTP request made to the view.
        product_id: The unique identifier for the product.
    Returns:
        HttpResponse: The rendered HTML template for the product detail page.
    """
    product = get_object_or_404(Product, pk=product_id)

    template = ["products/detail.html"]
    context = {
        'product': product,
    }

    return render(request, template, context)
