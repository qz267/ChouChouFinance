from django.contrib import admin
from blog.models import Category


admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

# Register your models here.
