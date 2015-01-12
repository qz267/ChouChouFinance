# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150105_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('excerpt', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text=b'Suggested value automatically generated from title. Must be unique.', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text=b'Maximum 250 characters.', max_length=250),
            preserve_default=True,
        ),
    ]
