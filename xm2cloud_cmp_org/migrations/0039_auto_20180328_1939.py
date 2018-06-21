# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-28 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0038_host_expiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='expiry_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
