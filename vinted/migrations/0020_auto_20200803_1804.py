# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-03 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0019_auto_20200803_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enchere',
            name='encherisseur',
            field=models.ManyToManyField(blank=True, null=True, related_name='antonio', to='vinted.User'),
        ),
    ]