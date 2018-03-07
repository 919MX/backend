# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-07 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0049_auto_20180303_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='donor',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
