# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-17 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
