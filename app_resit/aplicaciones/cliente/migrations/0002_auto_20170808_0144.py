# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cod_cliente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
