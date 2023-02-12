from django.shortcuts import render


def index(request):
    """view to render index page"""
    return render(request, "home/index.html")
