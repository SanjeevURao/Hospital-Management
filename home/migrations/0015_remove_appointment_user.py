# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-20 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20180219_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]
