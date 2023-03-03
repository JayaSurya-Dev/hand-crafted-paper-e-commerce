from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/<slug:slug>/',
         views.product_detail,
         name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/<slug:slug>/',
         views.edit_product,
         name='edit_product'),
]
