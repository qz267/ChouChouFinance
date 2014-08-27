from django.contrib import admin
from mysite.spend_record.models import OrderType, Order, PackageTracking, PackageCarrier, Refound

admin.site.register(OrderType)
admin.site.register(Order)
admin.site.register(PackageTracking)
admin.site.register(PackageCarrier)
admin.site.register(Refound)
