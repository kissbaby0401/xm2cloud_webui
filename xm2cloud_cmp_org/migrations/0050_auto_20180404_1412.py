# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-04 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0049_auto_20180404_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipline',
            name='band',
            field=models.IntegerField(blank=True, default=30),
        ),
        migrations.AddField(
            model_name='ipline',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
