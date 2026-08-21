from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'created_at')
    list_filter = ('post', 'author')
    search_fields = ('body',)
    ordering = ('-created_at',)
