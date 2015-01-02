from django.db import models


class SpendingCategories(models.Model):
    category_title = models.CharField(max_length=100)

    def __str__(self):
        return self.category_title.encode('utf-8')

    class Admin:
        pass


class SpendingRecords(models.Model):
    spending_date = models.DateField()
    spending_amount = models.FloatField(default=0.0)
    spending_category = models.ForeignKey(SpendingCategories)
    spending_note = models.CharField(max_length=200)

    def __str__(self):
        return self.spending_date, self.spending_amount, self.spending_category, self.spending_note

    class Admin:
        pass


