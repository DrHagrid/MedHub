# Generated by Django 2.1 on 2018-08-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20180813_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='code',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Код для вставки'),
        ),
        migrations.AlterField(
            model_name='anatomyelement',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='static/media/database/images/', verbose_name='Иллюстрация'),
        ),
        migrations.AlterField(
            model_name='anatomyelement',
            name='info',
            field=models.TextField(blank=True, help_text='Разрешено использовать тэги HTML', null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(help_text='Разрешено использовать тэги HTML', verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='histologyelement',
            name='image',
            field=models.FilePathField(blank=True, null=True, path='static/media/database/images/', verbose_name='Иллюстрация'),
        ),
        migrations.AlterField(
            model_name='histologyelement',
            name='info',
            field=models.TextField(blank=True, help_text='Разрешено использовать тэги HTML', null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ссылка'),
        ),
    ]