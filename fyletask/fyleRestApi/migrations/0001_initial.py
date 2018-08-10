# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-09 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndianBanks',
            fields=[
                ('ifsc', models.CharField(max_length=11)),
                ('bank_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank_name', models.CharField(max_length=49)),
            ],
        ),
    ]
