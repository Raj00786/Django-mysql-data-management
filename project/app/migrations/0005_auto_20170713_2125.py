# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 21:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170711_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nodedata',
            old_name='timestamp',
            new_name='ctimestamp',
        ),
    ]
