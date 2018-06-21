# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-31 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0045_auto_20180331_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporting',
            name='task_id',
            field=models.CharField(blank=True, default=uuid.UUID('e5142c24-a741-45cd-8f43-59f67fec20a5'), max_length=36),
        ),
        migrations.AlterField(
            model_name='reporttask',
            name='task_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
