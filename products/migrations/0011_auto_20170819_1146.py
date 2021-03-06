# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productimage_is_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категорія товару',
                'verbose_name_plural': 'Категорія товарів',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategory'),
        ),
    ]
