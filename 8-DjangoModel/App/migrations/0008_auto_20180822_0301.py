# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-22 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20180822_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_grade',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='App.Grade'),
        ),
    ]
