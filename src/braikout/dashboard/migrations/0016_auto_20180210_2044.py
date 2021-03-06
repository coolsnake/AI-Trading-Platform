# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-10 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20180210_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinprices',
            name='five_day_predictions',
            field=models.FloatField(default=100.0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coinprices',
            name='predictions',
            field=models.FloatField(default=100.0, max_length=10),
            preserve_default=False,
        ),
    ]
