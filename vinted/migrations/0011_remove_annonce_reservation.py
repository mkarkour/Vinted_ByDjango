# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-03 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0010_annonce_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annonce',
            name='reservation',
        ),
    ]