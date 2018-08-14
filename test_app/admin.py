# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


# Вопросы
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer']
    list_display_links = ['id', 'question']

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)


# Собственный тест
class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

    class Meta:
        model = Test


admin.site.register(Test, TestAdmin)
