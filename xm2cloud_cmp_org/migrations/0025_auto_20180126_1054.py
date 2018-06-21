# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0024_checkhostresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkhostresult',
            name='end_time',
            field=models.DateTimeField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkhostresult',
            name='sta_time',
            field=models.DateTimeField(auto_created=True, db_index=True, default=django.utils.timezone.now),
        ),
    ]
