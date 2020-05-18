# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_cities'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('PUB', 'Public'), ('PRI', 'Private')], default='PUB', max_length=3),
        ),
    ]