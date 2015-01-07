from django.contrib import admin
from blog.models import Category
from blog.models import Entry


admin.site.register(Category)
admin.site.register(Entry)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
