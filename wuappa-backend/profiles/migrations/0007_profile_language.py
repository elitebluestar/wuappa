# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20180125_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.CharField(default='en', max_length=7, blank=True, null=True),
        ),
    ]
