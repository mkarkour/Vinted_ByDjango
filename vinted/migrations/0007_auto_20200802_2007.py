# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-02 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0006_auto_20200802_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='prix',
            field=models.FloatField(default=0, null=True),
        ),
    ]
