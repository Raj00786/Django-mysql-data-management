# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-11 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170711_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodedata',
            name='signal_str',
            field=models.CharField(default='100', max_length=120),
        ),
    ]
