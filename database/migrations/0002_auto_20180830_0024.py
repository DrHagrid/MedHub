# Generated by Django 2.1 on 2018-08-29 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anatomyelement',
            options={'verbose_name': 'Элемент анатомии', 'verbose_name_plural': 'Элементы анатомии'},
        ),
        migrations.AlterModelOptions(
            name='histologyelement',
            options={'verbose_name': 'Элемент гистологии', 'verbose_name_plural': 'Элементы гистологии'},
        ),
    ]
