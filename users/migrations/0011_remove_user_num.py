# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='num',
        ),
    ]