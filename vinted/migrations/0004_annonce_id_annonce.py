# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-31 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0003_annonce_etat'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='id_annonce',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]