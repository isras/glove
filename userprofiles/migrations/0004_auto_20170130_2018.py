# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-31 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_user_player_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_phone',
            field=models.CharField(blank=True, default='xxx-xxxxxxx', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='xxx-xxxxxxx', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='player_id',
            field=models.CharField(blank=True, default='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', max_length=200),
        ),
    ]