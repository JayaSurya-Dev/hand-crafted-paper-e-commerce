from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('pages/contact/', views.contact_view, name='contact_view'),
    path('pages/about/', views.about_view, name='about_view'),
    path('pages/faq/', views.frequently_asked_questions_view, name='faq_view'),
    path('', views.index, name='index'),
]
