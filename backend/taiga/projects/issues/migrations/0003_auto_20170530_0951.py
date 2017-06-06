# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-30 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_issue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date'),
        ),
        migrations.AddField(
            model_name='issue',
            name='finished_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='finished date'),
        ),
        migrations.AddField(
            model_name='issue',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modified date'),
        ),
    ]
