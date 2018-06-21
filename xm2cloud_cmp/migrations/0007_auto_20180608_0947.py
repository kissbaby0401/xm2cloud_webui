# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-08 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0006_script_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='scriptlog',
            name='sevent_uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=36),
        ),
        migrations.AlterField(
            model_name='script',
            name='timeout',
            field=models.IntegerField(blank=True, default=300),
        ),
    ]