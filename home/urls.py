from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('contact/', views.contact_view, name='contact_view'),
    path('about/', views.about_view, name='about_view'),
    path('', views.index, name='index'),
]
