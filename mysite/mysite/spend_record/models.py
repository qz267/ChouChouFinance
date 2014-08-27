from django.db import models

# Create your models here.

class OrderType(models.Model):
    """
    This is class represent order type table
    """
    order_type_id = models.IntegerField()
    order_type_title = models.CharField(max_length=50)
    is_active = models.BooleanField()
    create_time = models.DateTimeField(editable=False)
    creator_id = models.IntegerField()
    update_time = models.DateTimeField()
    updator_id = models.IntegerField()


class Order(models.Model):
    """
    This class represent a individule spending record
    """

    order_id = models.IntegerField()
    order_type_id = models.ForeignKey(OrderType)
    order_date = models.DateField()
    order_amount = models.DecimalField(max_digits=6, decimal_places=2)
    order_detail = models.CharField(max_length=200)
    is_refund = models.BooleanField(default=False)
    create_time = models.DateTimeField(editable=False)
    creator_id = models.IntegerField()
    update_time = models.DateTimeField()
    updator_id = models.IntegerField()


class PackageTracking(models.Model):
    """
    This class represent package tracking record
    """
    package_tracking_id = models.IntegerField()
    order_id = models.ForeignKey(Order)
    package_tracking_number = models.CharField(max_length=50)
    package_carrier_id = models.IntegerField()
    create_time = models.DateTimeField(editable=False)
    creator_id = models.IntegerField()
    update_time = models.DateTimeField()
    updator_id = models.IntegerField()


class PackageCarrier(models.Model):
    """
    This is a class represent package carrier table
    """

    package_carrier_id = models.IntegerField()
    carrier_name = models.CharField(max_length=50)
    create_time = models.DateTimeField(editable=False)
    creator_id = models.IntegerField()
    update_time = models.DateTimeField()
    updator_id = models.IntegerField()


class Refound(models.Model):
    """
    This is a class represent refund table
    """
    
    refound_id = models.IntegerField()
    order_id = models.ForeignKey(Order)
    refound_amount = models.DecimalField(max_digits=9, decimal_places=2)
    create_time = models.DateTimeField(editable=False)
    creator_id = models.IntegerField()
    update_time = models.DateTimeField()
    updator_id = models.IntegerField()


