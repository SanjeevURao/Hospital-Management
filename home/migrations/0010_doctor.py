# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-18 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=100)),
                ('Speciality', models.CharField(max_length=100)),
            ],
        ),
    ]
