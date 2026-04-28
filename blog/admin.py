from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_ai_generated')
    list_filter = ('is_ai_generated', 'created_at', 'author')
    search_fields = ('title', 'content')
