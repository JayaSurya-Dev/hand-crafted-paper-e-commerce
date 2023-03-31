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
    Retrieve a list of published posts and render a template to display them.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered template.
    """

    # Retrieve all published posts from the database
    posts = Post.objects.filter(status="published")

    # Paginate the list of posts
    paginator = Paginator(posts, 8)

    # Get the current page number from the request parameters
    page = request.GET.get("page")

    try:
        # Attempt to retrieve the requested page of posts
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, default to the first page
        posts = paginator.page(1)

    # Define the template to be used to render the view
    template_name = "blog/post_list.html"

    # Define the variables to be passed to the template
    context = {
        "page_title": "Blog",
        "posts": posts,
        "page": page,
    }

    # Render the template with the given context and return the response
    return render(request, template_name, context)


def post_detail(request, slug):
    """
    Render the detail page for a single blog post, along with a comment
    form for users to leave comments.

    Args:
        request (HttpRequest): The HTTP request made to the view.
        slug (str): The slug identifier for the post.

    Returns:
        HttpResponse: The rendered HTML template for the post detail page.
    """
    # Retrieve the post object that matches the given slug,
    # or raise a 404 error if it doesn't exist.
    post = get_object_or_404(Post, slug=slug)

    # Retrieve all approved comment objects that are associated with the post.
    comments = post.comments.filter(approved=True)

    # Initialize the comment object to None.
    comment = None

    if request.method == 'POST':
        # If the request method is POST, it means the user has
        # submitted a comment form.
        form = CommentForm(request.POST)

        if form.is_valid():
            # If the comment form data is valid, create a new comment
            # object but don't save it to the database yet.
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.email = request.user.email

            if request.user.is_staff:
                # If the user is a staff member, approve and save the comment
                # to the database and display a success message.
                comment.approved = True
                comment.save()
                messages.success(request, "Thank you for your comment.")
            else:
                # If the user is not a staff member, save the comment but don't
                # approve it yet. Display a different success message.
                comment.save()
                messages.success(request, "Your comment is being reviewed.")

            # Redirect the user back to the same post detail page where they
            # left the comment.
            return redirect('blog:post_detail', slug=post.slug)
    else:
        # If the request method is not POST, create a new, empty CommentForm.
        form = CommentForm()

    # Set the template and context variables
    template = "blog/post_detail.html"
    context = {
        "page_title": post.title,
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
    object is created with the form data, and the author field is
    set to the current user. The new post is saved to the database,
    and a success message is added to the request's messages framework.
    The user is then redirected to the newly created post's detail page.

    If the form is not valid, the user is shown the form again with
    any validation errors displayed.

    Decorators:
    - @login_required: Only authenticated users can access this view.

    Parameters:
    - request (HttpRequest): the HTTP request object

    Returns:
    - HttpResponse: the HTTP response object with the rendered template
    """

    # Check if the user is a staff member, and create a new PostForm
    # instance with the POST and FILES data from the request
    if request.user.is_staff:
        form = PostForm(
            request.POST or None,
            request.FILES or None)

    # Check if the request method is POST
    if request.method == "POST":

        # Check if the form is valid
        if form.is_valid():
            # dont save it to the database yet.
            post = form.save(commit=False)

            # Set the author field to the current user
            form.instance.author = request.user

            # Save the post to the database
            post.save()

            # Add a success message to the request's messages framework
            messages.success(
                request, "Article has been created successfully.")

            # Redirect the user to the newly created post's detail page
            return redirect(reverse("blog:post_detail",
                                    kwargs={'slug': form.instance.slug}))
        else:
            # If the form is not valid, show it again with any validation
            # errors displayed
            form = PostForm()

    # Set the template and context variables
    template = "blog/post_create.html"
    context = {
        "page_title": "Add Article",
        "form_type": "Add",
        "form": form,
    }

    # Render the template with the context variables
    return render(request, template, context)


@login_required
def post_update(request, slug):
    """
    Update an existing blog article.
    This view handles POST requests to update a blog article with a given
    slug. It first retrieves the post to be updated from the database and
    then renders a form for the user to edit the post.

    The form used depends on whether the
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

    # Retrieve the post to be updated from the database
    post = get_object_or_404(Post, slug=slug)

    # Check if user is an administrator
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only authorized staff can do that.')
        return redirect(reverse("blog:post_list"))

    # User is an administrator, create a PostForm instance with the
    # existing post data
    form = PostForm(instance=post)

    if request.method == "POST":
        # A POST request was made, validate the form
        form = PostForm(request.POST or None,
                        request.FILES or None,
                        instance=post)
        if form.is_valid():
            # Form is valid, save the post and display success message
            form.save()
            messages.success(
                request, "Your article has been successfully updated.")
            return redirect(reverse("blog:post_detail",
                                    kwargs={'slug': form.instance.slug}))
        else:
            # Form is invalid, display error message
            messages.error(request, 'Failed to update article. \
Please ensure the form is valid.')
    # If form is not submitted or is invalid, re-render form with
    # existing post data
    form = PostForm(instance=post)
    # Display info message when rendering the template
    messages.info(request, f'You are editing {post.title}')

    # Set the template and context variables
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
    View function for deleting a blog post. If the request method is POST, the
    post with the given slug is deleted from the database. If the request
    method
    is GET, a form is rendered to confirm the deletion.

    Parameters:
    - request: the HTTP request object
    - slug: the slug of the post to be deleted

    Returns:
    - If the request method is POST: a redirect to the post list page
    - If the request method is GET: a rendered form template to confirm
    deletion
    """

    # Get the post to be deleted based on the slug parameter
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        # If the request method is POST, delete the post from the database
        post.delete()

        # Display a success message to the user
        messages.success(request, "Article deleted.")

        # Redirect the user to the post list page
        return redirect(reverse("blog:post_list"))
    else:
        # If the request method is GET, render a form template to confirm
        # deletion

        # Create a new instance of the PostForm, pre-populated with the data
        # from the post to be deleted
        form = PostForm(instance=post)

        # Set the context variables for the template
        template = "blog/delete_modal.html"
        context = {
            "form_type": "Delete",
            "post": post,
            "form": form,
        }

        # Render the form template with the context variables
        return render(request, template, context)


@login_required
def delete_comment(request, comment_id, slug):
    """
    View function for deleting a comment on a blog post. If the user
    is the author of the comment or a superuser, the comment is deleted
    from the database.

    Parameters:
    - request: the HTTP request object
    - comment_id: the ID of the comment to be deleted
    - slug: the slug of the post containing the comment

    Returns:
    - A redirect to the detail view of the post
    """

    # Get the comment to be deleted based on the comment_id parameter
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is authorized to delete the comment
    if request.user == comment.user or request.user.is_superuser:
        # If the user is authorized, delete the comment from the database
        comment.delete()

        # Display a success message to the user
        messages.success(request, "Comment deleted successfully!")
    else:
        # If the user is not authorized, display an error message
        messages.error(
            request, "You are not authorized to delete this comment.")

    # Redirect the user to the detail view of the post
    return redirect('blog:post_detail', slug=slug)
