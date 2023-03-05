from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import CommentForm


def post_list(request):
    """
    Display a list of published posts.
    Parameters:
        request (HttpRequest): the HTTP request object
    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    posts = Post.objects.filter(status="published")
    template = ["blog/post_list.html"]
    context = {
        "page_title": "Blog",
        "posts": posts,
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
