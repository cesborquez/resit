# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logistica',
            fields=[
                ('patente', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('vehiculo', models.CharField(max_length=20)),
                ('conductor', models.CharField(max_length=50)),
            ],
        ),
    ]