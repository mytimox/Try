# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-14 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170814_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='media/products_images'),
        ),
    ]
