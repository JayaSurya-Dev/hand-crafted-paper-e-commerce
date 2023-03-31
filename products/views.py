from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Category, Product, ProductReview
from .forms import ProductForm, ProductReviewForm


def product_list(request):
    """
    Display a list of all products, including sorting and search queries,
    paginated.

    Parameters:
        request (HttpRequest): the HTTP request object

    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    # Get all available products
    products = Product.objects.filter(available=True)
    # Initialize query, categories, sort, and direction to None
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        # Check if the 'sort' parameter is present in the GET request
        if 'sort' in request.GET:
            # Get the value of the 'sort' parameter and assign it to 'sortkey'
            sortkey = request.GET['sort']
            # Assign the value of 'sortkey' to 'sort' as well
            sort = sortkey

            # If the 'sortkey' parameter is 'rating', sort the products
            # based on their rating
            if sortkey == 'rating':
                # Get the 'direction' parameter from the GET request,
                # or use 'desc' as the default value
                direction = request.GET.get('direction', 'desc').lower()
                # Sort the products based on their rating, in either ascending
                # or descending order depending on the value of 'direction'
                products = sorted(
                    products,
                    # Use a lambda function as the sorting key to access the
                    # rating of each product
                    key=lambda p: p.get_rating(),
                    # Set the 'reverse' argument to True if 'direction' is not
                    # 'asc', which means sorting in descending order
                    reverse=direction != 'asc')

            # If the sorting method is anything else (e.g., 'name', 'price'),
            # sort the products using the Django ORM's order_by method
            else:
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

        # If the 'category' parameter is present, extract the
        # selected categories and filter the products based on them
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # If the 'q' parameter is present, extract the search term and
        # filter the products using the Django ORM's Q objects to perform
        # a case-insensitive search on the name and description fields
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products:product_list'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)

            products = products.filter(queries)

    # Set the current sorting direction as a string of the form
    # 'sort_direction'
    current_sorting = f'{sort}_{direction}'

    # Create a Paginator object with 12 products per page and set the
    # current page based on the 'page' GET parameter
    paginator = Paginator(products, 12)
    page = request.GET.get("page")
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If 'page' is not an integer, default to the first page
        products = paginator.page(1)

    # Render a template with the list of products, search term,
    # selected categories, current sorting method, and current page
    # number as context variables
    template = ["products/list.html"]
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        "page": page,

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
    # Retrieve the product object from the database or return 404
    # error if not found
    product = get_object_or_404(Product,
                                pk=product_id,
                                slug=slug,
                                available=True)

    # Check if the current user has the product in their wishlist
    wished = False
    if product.wishlist.filter(id=request.user.id).exists():
        wished = True

    # Handle submission of product review form
    review = None
    if request.method == 'POST':
        # If the request method is POST, validate the form data
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            # If the form is valid, create a new review object,
            # associate it with the product and user, and save it
            # to the database
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            # Display a success message to the user
            messages.success(request, "Thank you for your review.")
            # Redirect the user back to the product detail page
            return redirect(reverse('products:product_detail',
                            args=[product.id, product.slug]))
    else:
        # If the request method is not POST, display an empty
        # product review form
        form = ProductReviewForm()

    # Render the product detail page template and pass in the product
    # object, wished variable, and product review form as context variables
    template = ["products/detail.html"]
    context = {
        'product': product,
        'wished': wished,
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_product(request):
    """
    Add a product to the store

    Parameters:
        request (HttpRequest): the HTTP request made to the view.

    Returns:
        HttpResponse: The rendered HTML template for the add product page.
    """

    # Check if the user is a staff member
    if not request.user.is_staff:
        # If not, display an error message and redirect to the home page
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home:index'))

    if request.method == 'POST':
        # If the HTTP request method is POST, create a ProductForm
        # object with the submitted data and files
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # If the form is valid, create a new Product object with the form
            # data, save it to the database, and redirect to the product
            # detail page with a success message
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products:product_detail',
                            args=[product.id, product.slug]))
        else:
            # If the form is invalid, display an error message
            messages.error(request, 'Failed to add product. \
Please ensure the form is valid.')
    else:
        # If the HTTP request method is GET, create an empty ProductForm object
        form = ProductForm()

    # Render the add_product.html template with the form object in the
    # context dictionary
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
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

    # Check if user is a staff member
    if not request.user.is_staff:
        # Display error message and redirect to home page if user is not staff
        # member
        messages.error(request, 'Sorry, only store owners can edit products.')
        return redirect(reverse('home:index'))

    # Retrieve product from database
    product = get_object_or_404(Product, pk=product_id, slug=slug)

    if request.method == 'POST':
        # Create new ProductForm instance using data from POST request and
        # product instance
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Save changes to product and display success message
            form.save()
            messages.success(request, 'Successfully updated product!')
            # Redirect user to product detail page
            return redirect(reverse('products:product_detail',
                                    args=[product.id, product.slug]))
        else:
            # Display error message if form is not valid
            messages.error(request, 'Failed to update product. \
Please ensure the form is valid.')
    else:
        # Create new ProductForm instance using product instance
        form = ProductForm(instance=product)
        # Display info message about editing product
        messages.info(request, f'You are editing {product.name}')

    # Render edit product template with form and product as context
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
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
    # Check if user is authorized to delete a product
    if not request.user.is_staff:
        # Send an error message if user is not authorized to delete a product
        messages.error(request,
                       'Sorry, only store owners can delete a product.')
        # Redirect user to the product list page if user is not authorized to
        # delete a product
        return redirect(reverse('products:product_list'))

    # Retrieve the product to be deleted
    product = get_object_or_404(Product,
                                pk=product_id, slug=slug)

    # Check if a POST request was made
    if request.method == "POST":
        # Create a form instance with the POST data and the product to be
        # deleted
        form = ProductForm(request.POST, instance=product)
        # Delete the product from the database
        product.delete()
        # Send a success message after deleting the product
        messages.success(request, 'Product deleted!')
        # Redirect user to the product list page after deleting the product
        return redirect(reverse('products:product_list'))
    else:
        # If a POST request was not made, create a form instance with the
        # product to be deleted
        form = ProductForm(instance=product)

    # Render a modal to confirm that the user wants to delete the product
    template = "products/delete_modal.html"
    context = {
        "form_type": "Delete",
        "product": product,
        "form": form,
    }

    return render(request, template, context)
