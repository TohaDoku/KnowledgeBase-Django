from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')