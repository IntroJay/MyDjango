# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-22 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20180822_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=32)),
                ('g_buyer', models.ManyToManyField(to='App.Buyer')),
            ],
        ),
    ]