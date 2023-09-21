# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-03 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0020_auto_20200803_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enchere',
            name='encherisseur',
        ),
        migrations.AddField(
            model_name='enchere',
            name='encherisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vinted.User'),
        ),
    ]
