from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product


def product_list(request):
    """
    Display a list of all products, including sorting and search queries
    Parameters:
        request (HttpRequest): the HTTP request object
    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    products = Product.objects.filter(available=True)
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products:product_list'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)

            products = products.filter(queries)

    template = ["products/list.html"]
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,

    }

    return render(request, template, context)


def product_detail(request, product_id, slug):
    """
    Display an individual product details
    Parameters:
        request (HttpRequest): the HTTP request made to the view.
        product_id: The unique identifier for the product.
        slug (str): The human friendly identifier for the product.
    Returns:
        HttpResponse: The rendered HTML template for the product detail page.
    """
    product = get_object_or_404(Product,
                                pk=product_id,
                                slug=slug,
                                available=True)

    template = ["products/detail.html"]
    context = {
        'product': product,
    }

    return render(request, template, context)
