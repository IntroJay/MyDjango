# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-09 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=16)),
                ('g_info', models.CharField(max_length=64)),
            ],
        ),
    ]
