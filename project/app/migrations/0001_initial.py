# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-11 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_str', models.CharField(max_length=120)),
                ('signal_str', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NodeStats',
            fields=[
                ('node_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='nodedata',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.NodeStats'),
        ),
    ]