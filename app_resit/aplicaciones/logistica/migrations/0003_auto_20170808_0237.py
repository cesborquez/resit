# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0002_auto_20170808_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logistica',
            name='estado',
            field=models.IntegerField(default='0', editable=False),
        ),
    ]
