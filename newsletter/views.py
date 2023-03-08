from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.conf import settings
from newsletter.forms import EmailForm

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import logging
import hashlib

mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})

logger = logging.getLogger(__name__)


def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)


def subscribe_view(request):
    """
    Handle POST requests to subscribe a user's email to a
    Mailchimp audience using the Mailchimp API.

    If the request is not a POST request or the submitted
    form is invalid, the function renders a template with
    a blank email form.
    If the API call to Mailchimp is successful, the function
    logs a message and redirects the user to a
    "subscribe-success" page.
    If the API call to Mailchimp fails with an `ApiClientError`,
    the function logs an error message and redirects the user
    to a "subscribe-fail" page.

    :param request: A Django request object representing the
                    incoming HTTP request.
    :type request: HttpRequest
    :return: A Django HTTP response object representing the
            server's response to the incoming request.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                logger.info(f'API call successful: {response}')
                return redirect('newsletter:subscribe-success')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                return redirect('newsletter:subscribe-fail')

    template = 'newsletter/subscribe.html'
    context = {
        'form': EmailForm(),
    }
    return render(request, template, context)


def subscribe_success_view(request):
    """
    Renders a success message to the user after they have
    successfully subscribed to the mailing list.

    :param request: A Django request object representing the
                    incoming HTTP request.
    :type request: HttpRequest
    :return: A Django HTTP response object representing the
            server's response to the incoming request.
    :rtype: HttpResponse
    """
    template = 'newsletter/message.html'
    context = {
        'title': 'Successfully subscribed',
        'message': 'Yay, you have been successfully \
            subscribed to our mailing list.',
    }
    return render(request, template, context)


def subscribe_fail_view(request):
    """
    Renders a template to display an error message when
    a newsletter subscription attempt fails.

    :param request: A Django request object representing the
                    incoming HTTP request.
    :type request: HttpRequest
    :return: A Django HTTP response object representing the
            server's response to the incoming request.
    :rtype: HttpResponse
    """
    template = 'newsletter/message.html'
    context = {
        'title': 'Failed to subscribe',
        'message': 'Oops, something went wrong.',
    }
    return render(request, template, context)


def unsubscribe_view(request):
    """
    Renders the unsubscribe page and handles the form submission.

    This view function renders the 'newsletter/unsubscribe.html'
    template, which displays a form allowing the user to enter their
    email address and unsubscribe from the mailing list. If the form
    is submitted via POST request and is valid, the user's email
    address is hashed and used to update their status to 'unsubscribed'
    in the Mailchimp audience. If the update is successful, the user
    is redirected to the 'newsletter:unsubscribe-success' URL, otherwise
    they are redirected to the 'newsletter:unsubscribe-fail' URL.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                form_email_hash = hashlib.md5(
                    form_email.encode('utf-8').lower()).hexdigest()
                member_update = {
                    'status': 'unsubscribed',
                }
                response = mailchimp.lists.update_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    form_email_hash,
                    member_update,
                )
                logger.info(f'API call successful: {response}')
                return redirect('newsletter:unsubscribe-success')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                return redirect('newsletter:unsubscribe-fail')

    template = 'newsletter/unsubscribe.html'
    context = {
        'form': EmailForm(),
    }
    return render(request, template, context)


def unsubscribe_success_view(request):
    """
    Renders a success message to the user after they have
    successfully unsubscribed from the mailing list.

    :param request: A Django request object representing the
                    incoming HTTP request.
    :type request: HttpRequest
    :return: A Django HTTP response object representing the
            server's response to the incoming request.
    :rtype: HttpResponse
    """
    template = 'newsletter/message.html'
    context = {
        'title': 'Successfully unsubscribed',
        'message': 'You have been successfully \
                    unsubscribed from our mailing list.',
    }
    return render(request, template, context)


def unsubscribe_fail_view(request):
    """
    Renders a view to inform the user that their attempt to
    unsubscribe from
    the mailing list was unsuccessful.

    If the HTTP request method is a GET request, this function
    will render
    the 'newsletter/message.html' template with the title
    'Failed to unsubscribe'
    and the message 'Oops, something went wrong.'.

    :return:
        A rendered HttpResponse object with the
        'newsletter/message.html' template
        containing a message indicating that the unsubscribe
        attempt was unsuccessful.
    """
    template = 'newsletter/message.html'
    context = {
        'title': 'Failed to unsubscribe',
        'message': 'Oops, something went wrong.',
    }
    return render(request, template, context)
