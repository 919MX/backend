# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0040_auto_20180130_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='source',
        ),
    ]
