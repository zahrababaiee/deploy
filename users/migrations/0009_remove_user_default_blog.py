# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170716_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='default_blog',
        ),
    ]
