from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.post_create, name='post_create'),
    path('', views.post_list, name='post_list'),
    path('article/<slug:slug>/', views.post_detail, name='post_detail'),
    path('article/update/<slug:slug>/', views.post_update, name='post_update'),
    path('article/delete/<slug:slug>/', views.post_delete, name='post_delete'),
    path('article/comment/<slug:slug>/',
         views.post_detail, name='post_comment'),
    path('article/delete/comment/<int:comment_id>/<slug:slug>/',
         views.delete_comment, name='delete_comment'),
]
