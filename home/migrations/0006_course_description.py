# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-14 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_course_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]