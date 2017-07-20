# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170716_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='default_blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog'),
        ),
    ]
