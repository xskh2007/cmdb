# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0002_auto_20170711_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='Manufacturer',
        ),
        migrations.RemoveField(
            model_name='host',
            name='cpu_core',
        ),
        migrations.RemoveField(
            model_name='host',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='host',
            name='product',
        ),
        migrations.RemoveField(
            model_name='host',
            name='sn',
        ),
        migrations.RemoveField(
            model_name='host',
            name='vendor_id',
        ),
    ]