# -*- coding: utf-8 -*-
import json

from database.models import *


# Группы анатомии
class AnatomySection(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    variable = models.SlugField(verbose_name='Переменная',
                                help_text='Указывать на английском языке, используя вместо пробелов знаки "_"')
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Обложка')

    content = models.TextField(verbose_name='Контент', help_text='...')

    articles_count = models.IntegerField(blank=True, null=True, verbose_name='Количество статей')
    tests_count = models.IntegerField(blank=True, null=True, verbose_name='Количество тестов')

    def save(self, *args, **kwargs):
        articles_count = 0
        tests_count = 0
        for element in self.get_content():
            if element['type'] == 'article':
                articles_count += 1
            elif element['type'] == 'test':
                tests_count += 1
        self.articles_count = articles_count
        self.tests_count = tests_count
        super(AnatomySection, self).save(*args, **kwargs)

    def get_content(self):
        return json.loads(self.content)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Раздел анатомии'
        verbose_name_plural = 'Разделы анатомии'


# Гистология
class HistologySection(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    variable = models.SlugField(verbose_name='Переменная',
                                help_text='Указывать на английском языке, используя вместо пробелов знаки "_"')
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Обложка')

    content = models.TextField(verbose_name='Контент', help_text='...')

    articles_count = models.IntegerField(blank=True, null=True, verbose_name='Количество статей')
    tests_count = models.IntegerField(blank=True, null=True, verbose_name='Количество тестов')

    def save(self, *args, **kwargs):
        articles_count = 0
        tests_count = 0
        for element in self.get_content():
            if element['type'] == 'article':
                articles_count += 1
            elif element['type'] == 'test':
                tests_count += 1
        self.articles_count = articles_count
        self.tests_count = tests_count
        super(HistologySection, self).save(*args, **kwargs)

    def get_content(self):
        return json.loads(self.content)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Раздел гистологии'
        verbose_name_plural = 'Разделы гистологии'


# Физиология
class PhysiologySection(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    variable = models.SlugField(verbose_name='Переменная',
                                help_text='Указывать на английском языке, используя вместо пробелов знаки "_"')
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Обложка')

    content = models.TextField(verbose_name='Контент', help_text='...')

    articles_count = models.IntegerField(blank=True, null=True, verbose_name='Количество статей')
    tests_count = models.IntegerField(blank=True, null=True, verbose_name='Количество тестов')

    def save(self, *args, **kwargs):
        articles_count = 0
        tests_count = 0
        for element in self.get_content():
            if element['type'] == 'article':
                articles_count += 1
            elif element['type'] == 'test':
                tests_count += 1
        self.articles_count = articles_count
        self.tests_count = tests_count
        super(PhysiologySection, self).save(*args, **kwargs)

    def get_content(self):
        return json.loads(self.content)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Раздел физиологии'
        verbose_name_plural = 'Разделы физиологии'


unit_list = {'anatomy': {'name': 'Анатомия', 'variable': 'anatomy', 'model': AnatomyElement,
                         'section': AnatomySection},
             'histology': {'name': 'Гистология', 'variable': 'histology', 'model': HistologyElement,
                           'section': HistologySection},
             'physiology': {'name': 'Физиология', 'variable': 'physiology', 'model': None,
                            'section': PhysiologySection},
             }
