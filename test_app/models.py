# -*- coding: utf-8 -*-
from django.db import models
from database.models import *


# Вопросы
class Question(models.Model):
    TEST_TYPE_CHOICES = (
        ('input', 'Ввод'),
        ('radio', 'Выбор 1 ответа'),
    )

    question = models.CharField(max_length=128, blank=True, null=True, verbose_name='Вопрос')
    answer = models.CharField(max_length=64, blank=True, null=True, verbose_name='Ответ')
    test_type = models.CharField(max_length=64, default='radio', choices=TEST_TYPE_CHOICES, verbose_name='Тип вопроса')
    options = models.TextField(default='', blank=True, null=True, verbose_name='Варианты',
                               help_text='Впишите в это поле все варианты, включая верный, разделяя знаком ";"')
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Иллюстрация')

    anatomy = models.ForeignKey('database.AnatomyElement', on_delete=models.DO_NOTHING, blank=True, null=True,
                                verbose_name='На основе анатомического элемента',
                                help_text='Оставьте это поле пустым, если нет')

    histology = models.ForeignKey('database.HistologyElement', on_delete=models.DO_NOTHING, blank=True, null=True,
                                  verbose_name='На основе гистологического элемента',
                                  help_text='Оставьте это поле пустым, если нет')

    def save(self, *args, **kwargs):
        if self.anatomy:
            self.answer = self.anatomy.name
            self.image = self.anatomy.image
        if self.histology:
            self.question = 'Назовите изображенный препарат'
            self.answer = self.histology.name
            self.image = self.histology.image
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.question, self.answer)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


# Собственный тест
class Test(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Краткая информация')
    questions = models.ManyToManyField(Question, verbose_name='Вопросы')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
