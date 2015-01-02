# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0002_auto_20141230_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spendingrecords',
            old_name='spending_category_id',
            new_name='spending_category',
        ),
    ]
