# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20170822_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]