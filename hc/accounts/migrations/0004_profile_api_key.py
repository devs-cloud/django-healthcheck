# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='api_key',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
