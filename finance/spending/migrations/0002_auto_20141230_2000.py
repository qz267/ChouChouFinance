# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpendingRecords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spending_date', models.DateField()),
                ('spending_amount', models.FloatField(default=0.0)),
                ('spending_note', models.CharField(max_length=200)),
                ('spending_category_id', models.ForeignKey(to='spending.SpendingCategories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='spending',
            name='spending_category_id',
        ),
        migrations.DeleteModel(
            name='Spending',
        ),
    ]
