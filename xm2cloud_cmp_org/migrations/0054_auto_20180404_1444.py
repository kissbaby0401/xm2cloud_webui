# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-04 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0053_auto_20180404_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='localip',
        ),
        migrations.RemoveField(
            model_name='host',
            name='remoteip',
        ),
        migrations.RemoveField(
            model_name='host',
            name='vmbandwidth',
        ),
    ]