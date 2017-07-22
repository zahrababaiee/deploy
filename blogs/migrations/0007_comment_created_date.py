# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blog_isdefault'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
