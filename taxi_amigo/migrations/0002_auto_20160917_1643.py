# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktaxi',
            name='latitude',
            field=models.CharField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='booktaxi',
            name='longitude',
            field=models.CharField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='delivery',
            name='destination_latitude',
            field=models.CharField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='delivery',
            name='destination_longitude',
            field=models.CharField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='delivery',
            name='initial_latitude',
            field=models.CharField(default=0.0, max_length=200),
        ),
        migrations.AddField(
            model_name='delivery',
            name='initial_longitude',
            field=models.CharField(default=0.0, max_length=200),
        ),
    ]
