# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_product_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
    ]