# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-11 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0029_auto_20180111_0253'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='submission',
            name='map_submiss_source_18dcbc_idx',
        ),
        migrations.AlterField(
            model_name='submission',
            name='source_id',
            field=models.IntegerField(),
        ),
        migrations.AddIndex(
            model_name='submission',
            index=models.Index(fields=['source', 'source_id'], name='map_submiss_source_54d516_idx'),
        ),
    ]
