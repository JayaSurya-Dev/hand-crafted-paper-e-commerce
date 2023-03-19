from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.contrib import messages

from django.template.loader import render_to_string

from .models import FAQ
from .forms import ContactForm

from blog.models import Post


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


def frequently_asked_questions_view(request):
    """
    Render the frequently asked questions page template
    """
    faqs = FAQ.objects.filter(active=True)
    template = ["home/faq.html"]
    context = {
        "page_title": "Frequently Asked Questions",
        "faqs": faqs,
    }

    return render(request, template, context)


@login_required
def contact_view(request):
    """
    Handle the contact form submission.
    Display a blank form when called with an HTTP GET request.
    When called with an HTTP POST request, validate the form data
    and send an email if the form is valid.
    Args:
        request: An HTTP request object.
    Returns:
        An HTTP response object containing the contact form.
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd.get('name')
            email = request.user.email
            content = cd.get('content')
            recipient = cd.get('email')
            subject = 'Hand-Crafted Designs Enquiry'
            message = 'Email sent through Gmail'
            html = render_to_string(
                "home/emails/contact_form.html",
                {
                    "name": name,
                    "email": email,
                    "recipient": recipient,
                    "content": content,
                })
            if name and email and content and recipient \
                    and subject and message and html:
                try:
                    send_mail(
                        subject,
                        message,
                        recipient,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                        html_message=html
                        )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                messages.success(request, 'Email Sent!!')
                return redirect('products:product_list')
    else:
        ContactForm()

    template = 'home/contact.html'
    context = {
        'page_title': 'Contact Us',
        'form': form,
    }
    return render(request, template, context)
