# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20170716_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='num',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
