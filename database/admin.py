# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *


# Элемент анатомии
class AnatomyElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'lat_term']
    list_display_links = ['name', ]

    list_filter = []
    search_fields = ['name', 'lat_term']

    class Meta:
        model = AnatomyElement


admin.site.register(AnatomyElement, AnatomyElementAdmin)


# Элемент гистологии
class HistologyElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name', ]

    list_filter = []
    search_fields = ['name', 'lat_term']

    class Meta:
        model = HistologyElement


admin.site.register(HistologyElement, HistologyElementAdmin)


# Темы статьи
class ArticleThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['name', ]

    class Meta:
        model = ArticleTheme


admin.site.register(ArticleTheme, ArticleThemeAdmin)


# Статья
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date', 'is_main']
    list_display_links = ['title', ]

    list_filter = ['theme', ]
    search_fields = ['title', 'author']

    list_editable = ['is_main', ]

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)


# Изображение
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']
    list_display_links = ['id', ]

    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)


# Вопрос
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer']
    list_display_links = ['question', ]

    class Meta:
        model = Question


admin.site.register(Question, QuestionAdmin)


# Тест
class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name', ]

    class Meta:
        model = Test


admin.site.register(Test, TestAdmin)
