from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger

from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    """
    Display a list of published posts.
    Parameters:
        request (HttpRequest): the HTTP request object
    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    posts = Post.objects.filter(status="published")
    paginator = Paginator(posts, 8)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    template = ["blog/post_list.html"]
    context = {
        "page_title": "Blog",
        "posts": posts,
        "page": page,
    }

    return render(request, template, context)


def post_detail(request, slug):
    """
    Display a single post and a comment form.
    Parameters:
        request (HttpRequest): The HTTP request made to the view.
        slug (str): The slug identifier for the post.
    Returns:
        HttpResponse: The rendered HTML template for the post detail page.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.email = request.user.email
            if request.user.is_staff:
                comment.approved = True
                comment.save()
                messages.success(request, "Thank you for your comment.")
            else:
                comment.save()
                messages.success(request, "Your comment it's been reviewed.")

            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()

    template = "blog/post_detail.html"
    context = {
        "page_title": "Blog Article",
        "comments": comments,
        "form": form,
        "post": post,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    """
    View function for creating a new blog article.

    If the user is a staff member, a new PostForm is created with
    the POST and FILES data from the request.
    If the request method is POST and the form is valid, a new Post
    object is created with the form data,
    and the author field is set to the current user. The new post is
    saved to the database,
    and a success message is added to the request's messages framework.
    The user is then redirected to the newly created post's detail page.
    If the form is not valid, the user is shown the form again with
    any validation errors displayed.

    Decorators:
    - @login_required: Only authenticated users can access this view.

    Parameters:
        request (HttpRequest): the HTTP request object
    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """

    if request.user.is_staff:
        form = PostForm(
            request.POST or None,
            request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            form.instance.author = request.user
            post.save()
            messages.success(
                request, "Article has been created successfully.")

            return redirect(reverse("blog:post_detail", kwargs={
                "slug": form.instance.slug
            }))
        else:
            form = PostForm()

    template = "blog/post_create.html"
    context = {
        "page_title": "Add Article",
        "form_type": "Add",
        "form": form,
    }
    return render(request, template, context)


@login_required
def post_update(request, slug):
    """
    Update an existing blog article.
    This view handles POST requests to update a blog article with a given
    slug. It first retrieves the post to be updated from the database and
    then renders a
    form for the user to edit the post. The form used depends on whether the
    user making the request is an administrator. If the request method is POST,
    the form is validated and, if valid, the post is updated and a success
    message is displayed to the user. If the form is invalid or the request
    method is not POST, the form is re-rendered with the existing post data.
    Parameters:
        request: an HTTP POST request to update the post.
        slug: a string representing the unique slug for the post.
    Returns:
        An HTTP response containing the rendered form for updating the post or
        a redirect to the updated post detail page.
    """

    post = get_object_or_404(Post, slug=slug)

    if request.user.is_staff:
        form = PostForm(
            request.POST or None,
            request.FILES or None,
            instance=post)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only authorized staff can do that.')
        return redirect(reverse("home:index"))

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your article has been successfully updated.")
            return redirect(reverse("blog:post_detail", kwargs={
                "slug": form.instance.slug
            }))
        else:
            messages.error(request,
                           'Failed to update article. \
                            Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = "blog/post_create.html"
    context = {
        "page_title": "Update Article",
        "form_type": "Update",
        "form": form,
    }
    return render(request, template, context)


@login_required
def post_delete(request, slug):
    """
    Delete an article with the given slug.
    Accepts a POST request with a slug parameter and deletes the post
    with the given slug from the database.
    On GET request, render a confirmation form.
    Parameters:
        request: the request object
        slug: the slug of the post to delete
    Returns:
        On a POST request:
            A redirect to the post list page
        On a GET request:
            A rendered form template to confirm the post deletion
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        post.delete()
        messages.success(
            request, "Article deleted.")
        return redirect(reverse("blog:post_list"))
    else:
        form = PostForm(instance=post)

    template = "blog/delete_modal.html"
    context = {
        "form_type": "Delete",
        "post": post,
        "form": form,
    }
    return render(request, template, context)
