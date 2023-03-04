from django.shortcuts import (
    render,
    reverse,
    )
from .models import Post, Comment
from django.contrib import messages


def post_list(request):
    """
    Display a list of published posts.
    Parameters:
        request (HttpRequest): the HTTP request object
    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    posts = Post.objects.filter(status="published")

    template = ["blog/post/post_list.html"]
    context = {
        "page_title": "Coding Articles",
        "posts": posts,
    }

    return render(request, template, context)
