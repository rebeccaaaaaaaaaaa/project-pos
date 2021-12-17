from django.contrib import admin
from .models import BlogItem

# Register your models here.
class BlogItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'body') # list_display: list of fields to display in the admin list view
    list_filter = ("title",)
    search_fields = ['title', 'body']


admin.site.register(BlogItem)