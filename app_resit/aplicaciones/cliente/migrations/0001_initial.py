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
            name='Cliente',
            fields=[
                ('cod_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('cod_postal', models.IntegerField()),
                ('tiempo_recorrido', models.IntegerField()),
            ],
        ),
    ]
