# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 01:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
        ('cliente', '0001_initial'),
        ('logistica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateField()),
                ('fecha_confir', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('estado', models.IntegerField()),
                ('Cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('Logistica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logistica.Logistica')),
                ('Producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.Producto')),
            ],
        ),
    ]
