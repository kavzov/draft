# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170627_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='manager',
            new_name='mngr',
        ),
    ]