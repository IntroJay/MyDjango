# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=16)),
                ('t_age', models.IntegerField(default=18)),
            ],
            options={
                'db_table': 'laoshi',
            },
        ),
    ]
