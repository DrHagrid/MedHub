# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-11 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20180809_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='anatomysection',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткая информация'),
        ),
        migrations.AddField(
            model_name='histologysection',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткая информация'),
        ),
    ]
