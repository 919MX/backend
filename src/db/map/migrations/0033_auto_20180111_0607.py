# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-11 06:07
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0032_action_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='contact',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, help_text='Contact data'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.TextField(),
        ),
    ]
