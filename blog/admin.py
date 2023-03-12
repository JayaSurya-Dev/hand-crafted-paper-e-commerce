from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Post model in admin panel
    """
    summernote_fields = ('content',)

    list_display = (
        'id',
        'title',
        'status',
        'created_on',
        'updated_on',
        'featured'
        )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'featured')
    actions = [
        'featured',
        ]

    def featured(self, request, queryset):
        queryset.update(featured=True)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Comment model in admin panel
    """
    summernote_fields = ('body',)

    list_display = [
        'id',
        'user',
        'email',
        'post',
        'created_on',
        'approved',
    ]
    list_filter = [
        'approved',
        'created_on',
    ]
    search_fields = [
        'user',
        'email',
        'body',
    ]

    actions = ['approved']

    def approved(self, request, queryset):
        queryset.update(approved=True)
