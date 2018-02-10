# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-22 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0038_auto_20180118_1848'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='establishment',
            index=models.Index(fields=['locality_id', 'scian_group_id'], name='map_establi_localit_91343f_idx'),
        ),
    ]