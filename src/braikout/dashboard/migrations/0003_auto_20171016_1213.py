# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_coinprices_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinprices',
            name='current_price',
            field=models.FloatField(verbose_name=100),
        ),
    ]
