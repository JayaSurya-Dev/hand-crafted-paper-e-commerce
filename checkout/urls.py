from django.urls import path
from .webhooks import webhook

from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]
