# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commssion_rate',
            name='commission_rate',
            field=models.FloatField(),
        ),
    ]
