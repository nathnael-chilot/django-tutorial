from django.contrib import admin
from .models import Post, Category

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'category', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)