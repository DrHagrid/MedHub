# Generated by Django 2.1 on 2018-09-11 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20180830_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.Image', verbose_name='Иллюстрация'),
        ),
    ]