# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 13:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20170627_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='managing',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='test',
            name='mngr',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=[]),
        ),
    ]