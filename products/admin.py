from django.contrib import admin
from .models import Category, Product
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'slug',
        )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'category',
        'price',
        'rating',
        'available',
        'created_on',
        'updated_on',
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
