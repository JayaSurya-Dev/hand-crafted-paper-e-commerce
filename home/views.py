from django.shortcuts import render


def index(request):
    """
    View to render index page
    """
    return render(request, "home/index.html")


def about_view(request):
    """
    Render the about page template
    """
    template = ["home/about.html"]
    context = {
        "page_title": "About",
    }

    return render(request, template, context)
