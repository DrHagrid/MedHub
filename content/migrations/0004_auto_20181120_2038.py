# Generated by Django 2.1 on 2018-11-20 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_test_image'),
        ('content', '0003_auto_20180830_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysiologySection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('variable', models.SlugField(help_text='Указывать на английском языке, используя вместо пробелов знаки "_"', verbose_name='Переменная')),
                ('content', models.TextField(help_text='...', verbose_name='Контент')),
                ('articles_count', models.IntegerField(blank=True, null=True, verbose_name='Количество статей')),
                ('tests_count', models.IntegerField(blank=True, null=True, verbose_name='Количество тестов')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.Image', verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'Раздел гистологии',
                'verbose_name_plural': 'Разделы гистологии',
            },
        ),
        migrations.AddField(
            model_name='histologysection',
            name='articles_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество статей'),
        ),
        migrations.AddField(
            model_name='histologysection',
            name='tests_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество тестов'),
        ),
    ]
