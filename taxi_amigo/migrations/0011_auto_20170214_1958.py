# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-15 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0010_auto_20170130_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktaxi',
            name='destination_latitude',
            field=models.CharField(blank=True, default=0.0, max_length=200),
        ),
        migrations.AlterField(
            model_name='booktaxi',
            name='destination_longitude',
            field=models.CharField(blank=True, default=0.0, max_length=200),
        ),
    ]
