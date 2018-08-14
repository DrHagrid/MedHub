# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# Элемент анатомии
class AnatomyElement(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    lat_term = models.CharField(max_length=64, verbose_name='Латинский термин')
    eng_term = models.CharField(max_length=64, blank=True, null=True, verbose_name='Английский термин',
                                help_text='Необязательное поле')
    group = models.ForeignKey('database.AnatomyGroup', blank=True, null=True, on_delete=models.DO_NOTHING,
                              verbose_name='Группа')
    type = models.ForeignKey('database.AnatomyType', blank=True, null=True, on_delete=models.DO_NOTHING,
                             verbose_name='Тип')
    info = models.TextField(blank=True, null=True, verbose_name='Информация',
                            help_text='Разрешено использовать тэги HTML')
    image = models.FilePathField(path="static/media/database/images/", blank=True, null=True, verbose_name='Иллюстрация')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Анатомия - элемент'
        verbose_name_plural = 'Анатомия - элементы'


# Группа анатомического элемента
class AnatomyGroup(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    variable = models.SlugField(verbose_name='Переменная',
                                help_text='Указывать на английском языке, используя вместо пробелов знаки "_"')
    description = models.TextField(blank=True, null=True, verbose_name='Краткая информация')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Анатомия - группа'
        verbose_name_plural = 'Анатомия - группы'


# Тип анатомического элемента
class AnatomyType(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    variable = models.SlugField(verbose_name='Переменная',
                                help_text='Указывать на английском языке, используя вместо пробелов знаки "_"')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Анатомия - тип'
        verbose_name_plural = 'Анатомия - типы'


# Элемент гистологии
class HistologyElement(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    lat_term = models.CharField(max_length=64, blank=True, null=True, verbose_name='Латинский термин',
                                help_text='Необязательное поле')
    eng_term = models.CharField(max_length=64, blank=True, null=True, verbose_name='Английский термин',
                                help_text='Необязательное поле')
    group = models.ForeignKey('database.HistologyGroup', blank=True, null=True, on_delete=models.DO_NOTHING,
                              verbose_name='Группа')
    info = models.TextField(blank=True, null=True, verbose_name='Информация',
                            help_text='Разрешено использовать тэги HTML')
    image = models.FilePathField(path="static/media/database/images/", blank=True, null=True, verbose_name='Иллюстрация')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Гистология - элемент'
        verbose_name_plural = 'Гистология - элементы'


# Группа гистологического элемента
class HistologyGroup(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    variable = models.SlugField(verbose_name='Переменная',
                                help_text='Указывать на английском языке, используя вместо пробелов знаки "_"')

    description = models.TextField(blank=True, null=True, verbose_name='Краткая информация')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Гистология - группа'
        verbose_name_plural = 'Гистология - группы'


# Статьи
class ArticleTheme(models.Model):
    COLOR_CHOICES = (
        ('primary', 'Фиолетовый'),
        ('info', 'Голубой'),
        ('success', 'Зеленый'),
        ('danger', 'Красный'),
        ('warning', 'Желтый'),
        ('default', 'Серый'),
    )

    name = models.CharField(max_length=64, verbose_name='Название')
    color = models.CharField(max_length=64, default='default', choices=COLOR_CHOICES, verbose_name='Цвет')
    variable = models.SlugField(verbose_name='Переменная',
                                help_text='Указывать на английском языке, используя вместо пробелов знаки "_"')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тема статьи'
        verbose_name_plural = 'Темы статьи'


class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    description = models.TextField(blank=True, null=True, verbose_name='Краткая информация')
    content = models.TextField(verbose_name='Содержимое', help_text='Разрешено использовать тэги HTML')
    theme = models.ForeignKey(ArticleTheme, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Тема')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Автор')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    image = models.FilePathField(path="static/media/database/images/", blank=True, null=True, verbose_name='Иллюстрация')
    is_main = models.BooleanField(default=True, verbose_name='Отображать на главной странице')

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Image(models.Model):
    file = models.ImageField(upload_to='database/images', blank=True, null=True, verbose_name='Файл')
    url = models.CharField(max_length=256, blank=True, null=True, verbose_name='Ссылка')
    code = models.CharField(max_length=256, blank=True, null=True, verbose_name='Код для вставки')

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Image.objects.get(pk=self.pk)
            if old_self.file and self.file != old_self.file:
                old_self.file.delete(False)
        super(Image, self).save(*args, **kwargs)
        self.url = self.file.url
        self.code = '<img src="/' + self.url + '" class="img-fluid">'
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@receiver(pre_delete, sender=Image)
def file_delete(sender, instance, **kwargs):
    if instance.file.name:
        instance.file.delete(False)
