from django.contrib import admin
from spending.models import SpendingRecords, SpendingCategories
# Register your models here.

admin.site.register(SpendingCategories)
admin.site.register(SpendingRecords)