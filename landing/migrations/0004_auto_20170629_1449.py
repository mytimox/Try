# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20170629_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pib',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='pib',
            name='years',
        ),
        migrations.AlterField(
            model_name='pib',
            name='first_name',
            field=models.CharField(max_length=22, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='pib',
            name='last_name',
            field=models.CharField(max_length=33, verbose_name='Прізвище'),
        ),
    ]
