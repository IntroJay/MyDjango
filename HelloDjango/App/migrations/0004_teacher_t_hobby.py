# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-11 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='t_hobby',
            field=models.CharField(default='eat', max_length=128, null=True),
        ),
    ]
