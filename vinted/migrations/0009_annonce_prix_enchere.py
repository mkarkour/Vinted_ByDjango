# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-03 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0008_auto_20200802_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='prix_enchere',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
