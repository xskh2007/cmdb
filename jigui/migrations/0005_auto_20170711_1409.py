# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jigui', '0004_auto_20170710_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jiguiinfo',
            name='d',
            field=models.ManyToManyField(null=True, to='jigui.dx', verbose_name='多选'),
        ),
        migrations.AlterField(
            model_name='jiguiinfo',
            name='sh',
            field=models.CharField(max_length=64, null=True, verbose_name='整包'),
        ),
        migrations.AlterField(
            model_name='jiguiinfo',
            name='xz',
            field=models.CharField(max_length=64, null=True, verbose_name='闲置'),
        ),
        migrations.AlterField(
            model_name='jiguiinfo',
            name='zb',
            field=models.CharField(max_length=64, null=True, verbose_name='在售'),
        ),
        migrations.AlterField(
            model_name='jiguiinfo',
            name='ziy',
            field=models.CharField(max_length=64, null=True, verbose_name='在用'),
        ),
        migrations.AlterField(
            model_name='jiguiinfo',
            name='zs',
            field=models.CharField(max_length=64, null=True, verbose_name='自用'),
        ),
        migrations.AlterField(
            model_name='jiguiinfo',
            name='zy',
            field=models.CharField(max_length=64, null=True, verbose_name='自用'),
        ),
    ]
