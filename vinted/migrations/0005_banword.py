# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-02 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinted', '0004_annonce_id_annonce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wordinit', models.CharField(max_length=30)),
                ('wordfinal', models.CharField(max_length=30)),
            ],
        ),
    ]
