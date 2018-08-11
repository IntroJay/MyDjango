# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=16)),
                ('s_age', models.IntegerField(default=18)),
                ('is_delete', models.BooleanField(default=False)),
                ('s_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Grade')),
            ],
        ),
    ]
