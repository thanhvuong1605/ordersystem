# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-22 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order_system_app', '0004_auto_20180221_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('total', models.FloatField()),
                ('status', models.IntegerField(choices=[(2, 'Ready'), (4, 'Delivered'), (1, 'Cooking'), (3, 'On the way')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('picked_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_system_app.Customer')),
                ('restaurent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_system_app.Restaurant')),
            ],
        ),
    ]
