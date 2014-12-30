from django.db import models


class SpendingCategories(models.Model):
    category_title = models.CharField(max_length=100)


class Spending(models.Model):
    spending_date = models.DateField()
    spending_amount = models.FloatField(default=0.0)
    spending_category_id = models.ForeignKey(SpendingCategories)
    spending_note = models.CharField(max_length=200)


