# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-03 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0009_annonce_prix_enchere'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='reservation',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]