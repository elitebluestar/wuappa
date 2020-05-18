# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 12:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coupon', '0003_auto_20171228_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='user',
        ),
        migrations.AddField(
            model_name='usedcoupon',
            name='coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_by', to='coupon.Coupon'),
        ),
        migrations.AddField(
            model_name='usedcoupon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_coupons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='usedcoupon',
            unique_together=set([('coupon', 'user')]),
        ),
    ]