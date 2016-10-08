# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_amigo', '0006_auto_20160919_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabride',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='taxi_amigo_cabride_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cabride',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='cabride',
            name='service_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='taxi_amigo.ServiceType'),
        ),
        migrations.AlterField(
            model_name='cabride',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
