# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-02 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0005_banword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='prix',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
