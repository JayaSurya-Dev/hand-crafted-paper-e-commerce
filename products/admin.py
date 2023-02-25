from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Product
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category model in admin panel
    """
    list_display = (
        'friendly_name',
        'name',
        'parent',
        'slug',
        )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Product model in admin panel
    """
    summernote_fields = '__all__'

    list_display = (
        'name',
        'slug',
        'category',
        'price',
        'rating',
        'available',
        'created_on',
        'updated_on',
        'image',
        )

    list_filter = (
        'available',
        'created_on',
        'updated_on',
    )

    list_editable = (
        'price',
        'available',
    )
    prepopulated_fields = {'slug': ('name',)}
