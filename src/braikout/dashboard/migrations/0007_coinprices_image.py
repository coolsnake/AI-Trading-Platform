# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_coinprices_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinprices',
            name='image',
            field=models.ImageField(blank=True, upload_to='prediction_chart'),
        ),
    ]
