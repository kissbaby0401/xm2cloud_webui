# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='AlertContactGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('short_name', models.CharField(max_length=32, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Envirment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128)),
                ('vmcpu', models.IntegerField(blank=True, default=4)),
                ('vmmem', models.IntegerField(blank=True, default=4)),
                ('vmbandwidth', models.IntegerField(blank=True, default=30)),
                ('remoteip', models.GenericIPAddressField(unique=True)),
                ('localip', models.GenericIPAddressField(default='127.0.0.1')),
                ('vmstatus', models.SmallIntegerField(blank=True, default=0)),
                ('heartbeatstatus', models.SmallIntegerField(blank=True, default=0)),
                ('agentstatus', models.SmallIntegerField(blank=True, default=0)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
                ('alertcontactgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.AlertContactGroup')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.Cluster')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('website', models.URLField(default='')),
                ('short_name', models.CharField(max_length=32, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('type', models.CharField(default='linux', max_length=64)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.Continent')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.Region'),
        ),
        migrations.AddField(
            model_name='host',
            name='firm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.Manufacturer'),
        ),
        migrations.AddField(
            model_name='host',
            name='hostgroups',
            field=models.ManyToManyField(to='xm2cloud_cmp.HostGroup'),
        ),
        migrations.AddField(
            model_name='host',
            name='vmos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.OperatingSystem'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='env',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.Envirment'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xm2cloud_cmp.Project'),
        ),
        migrations.AddField(
            model_name='alertcontact',
            name='alertcontactgroups',
            field=models.ManyToManyField(to='xm2cloud_cmp.AlertContactGroup'),
        ),
    ]
