# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        ('services', '0004_category_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cities',
            field=models.ManyToManyField(to='geo.City'),
        ),
    ]
