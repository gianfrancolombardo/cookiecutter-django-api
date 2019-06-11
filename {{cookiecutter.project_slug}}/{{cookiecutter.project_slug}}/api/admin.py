"""Api admin."""

# Django
from django.contrib import admin

# Own
from {{cookiecutter.project_slug}}.api.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ('title','created')
    search_fields = ('title',)
    list_filter = ('created',)

 