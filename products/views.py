from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Category, Product
from .forms import ProductForm


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
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    template = ["products/list.html"]
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,

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


def add_product(request):
    """
    Add a product to the store
    Parameters:
        request (HttpRequest): the HTTP request made to the view.
    Returns:
        HttpResponse: The rendered HTML template for the add product page.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products:product_detail',
                            args=[product.id, product.slug]))
        else:
            messages.error(request,
                           'Failed to add product. \
                            Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id, slug):
    """
    Edit a product in the store
    Parameters:
        request (HttpRequest): the HTTP request made to the view.
        product_id: The unique identifier for the product.
        slug (str): The human friendly identifier for the product.
    Returns:
        HttpResponse: The rendered HTML template for the edit product page.
    """

    product = get_object_or_404(Product,
                                pk=product_id, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products:product_detail',
                            args=[product.id, product.slug]))
        else:
            messages.error(
                request, 'Failed to update product. \
                    Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id, slug):
    """
    Delete a product from the store
    Parameters:
        request (HttpRequest): the HTTP request made to the view.
        product_id: The unique identifier for the product.
        slug (str): The human friendly identifier for the product.
    Returns:
        HttpResponse: The rendered HTML template for the product list page.
    """

    product = get_object_or_404(Product,
                                pk=product_id, slug=slug)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products:product_list'))
