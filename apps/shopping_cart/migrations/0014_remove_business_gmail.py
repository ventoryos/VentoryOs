# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-24 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0013_remove_business_gmail_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='gmail',
        ),
    ]