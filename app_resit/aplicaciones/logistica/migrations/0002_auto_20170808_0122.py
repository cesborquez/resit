# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistica',
            name='patente',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]