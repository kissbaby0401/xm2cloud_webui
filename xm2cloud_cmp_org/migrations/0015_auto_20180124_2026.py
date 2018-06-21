# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xm2cloud_cmp', '0014_auto_20180124_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statuscheck',
            name='check_condition',
        ),
        migrations.RemoveField(
            model_name='statuscheck',
            name='check_value',
        ),
        migrations.AddField(
            model_name='statuscheck',
            name='critical_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statuscheck',
            name='error_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statuscheck',
            name='warning_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='calculated_status',
            field=models.CharField(choices=[('PASSING', '\u6b63\u5e38'), ('FAILING', '\u5f02\u5e38')], default='PASSING', max_length=64),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='compare_method',
            field=models.CharField(choices=[('avges', '\u5e73\u5747\u503c'), ('mines', '\u6700\u5c0f\u503c'), ('maxes', '\u6700\u5927\u503c')], default='avges', max_length=32),
        ),
        migrations.AlterField(
            model_name='statuscheck',
            name='importance',
            field=models.CharField(choices=[('CRITICAL', '\u4e25\u91cd'), ('WARNING', '\u8b66\u544a'), ('ERROR', '\u9519\u8bef')], default='ERROR', max_length=32),
        ),
    ]
