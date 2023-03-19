from django.contrib import admin
from .models import FAQ
from django.contrib.auth.decorators import login_required


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Frequent Asked Question model in admin panel
    """

    list_display = (
        'question',
        'active',
        'created_on',
        )

    list_editable = (
        'active',
    )
