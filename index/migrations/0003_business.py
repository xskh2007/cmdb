# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0002_auto_20170710_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, null=True, verbose_name='机房')),
                ('code', models.CharField(default='SA', max_length=32, null=True, verbose_name='产品线')),
            ],
            options={
                'verbose_name': '机房组',
                'verbose_name_plural': '机房组',
                'db_table': 'Business',
            },
        ),
    ]