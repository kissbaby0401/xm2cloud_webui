# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-09 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0080_auto_20180509_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='metric_uuid',
            field=models.UUIDField(default=b'f9348e2d-1fd8-4370-a913-d467e413f2ca'),
        ),
    ]