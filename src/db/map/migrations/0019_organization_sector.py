# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-05 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0018_locality_has_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='sector',
            field=models.TextField(choices=[('civil', 'Civil'), ('public', 'Público'), ('private', 'Privado'), ('religious', 'Religioso')], db_index=True, default='privado'),
            preserve_default=False,
        ),
    ]