from django.shortcuts import render
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
