# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from database.models import *
from test_app.models import Test


# Группы анатомии
class AnatomySection(models.Model):
    group = models.ForeignKey(AnatomyGroup, on_delete=models.DO_NOTHING, verbose_name='Группа')
    type = models.ForeignKey(AnatomyType, on_delete=models.DO_NOTHING, verbose_name='Тип')
    image = models.FilePathField(path="/static/media/database/images/", blank=True, null=True, verbose_name='Обложка')

    articles = models.ManyToManyField(Article, blank=True, verbose_name='Статьи')
    tests = models.ManyToManyField(Test, blank=True, verbose_name='Тесты')
    is_latin_test = models.BooleanField(default=False, verbose_name='Автоматический тест по латинским терминам')

    def __str__(self):
        return "%s - %s" % (self.group.name, self.type.name)

    class Meta:
        verbose_name = 'Анатомия - секция'
        verbose_name_plural = 'Анатомия - секции'


# Гистология
class HistologySection(models.Model):
    group = models.ForeignKey(HistologyGroup, on_delete=models.DO_NOTHING, verbose_name='Группа')
    image = models.FilePathField(path="/static/media/database/images/", blank=True, null=True, verbose_name='Обложка')

    articles = models.ManyToManyField(Article, blank=True, verbose_name='Статьи')
    tests = models.ManyToManyField(Test, blank=True, verbose_name='Тесты')
    is_latin_test = models.BooleanField(default=False, verbose_name='Автоматический тест по латинским терминам')

    def __str__(self):
        return "%s" % self.group.name

    class Meta:
        verbose_name = 'Гистология - секция'
        verbose_name_plural = 'Гистология - секции'


unit_list = {'anatomy': {'name': 'Анатомия', 'variable': 'anatomy', 'model': AnatomyElement,
                         'group': AnatomyGroup, 'type': AnatomyType, 'section': AnatomySection},
             'histology': {'name': 'Гистология', 'variable': 'histology', 'model': HistologyElement,
                           'group': HistologyGroup, 'type': None, 'section': HistologySection},
             }