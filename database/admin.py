# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *


# Анатомия
class AnatomyElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'lat_term']
    list_display_links = ['id', 'name']

    list_filter = ['group', 'type']
    search_fields = ['name', 'lat_term']

    class Meta:
        model = AnatomyElement


admin.site.register(AnatomyElement, AnatomyElementAdmin)


class AnatomyGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['id', 'name']

    class Meta:
        model = AnatomyGroup


admin.site.register(AnatomyGroup, AnatomyGroupAdmin)


class AnatomyTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['id', 'name']

    class Meta:
        model = AnatomyType


admin.site.register(AnatomyType, AnatomyTypeAdmin)


# Гистология
class HistologyElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

    list_filter = ['group', ]
    search_fields = ['name', 'lat_term']

    class Meta:
        model = HistologyElement


admin.site.register(HistologyElement, HistologyElementAdmin)


class HistologyGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['id', 'name']

    class Meta:
        model = HistologyGroup


admin.site.register(HistologyGroup, HistologyGroupAdmin)


# Статьи
class ArticleThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['id', 'name']

    class Meta:
        model = ArticleTheme


admin.site.register(ArticleTheme, ArticleThemeAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date', 'is_main']
    list_display_links = ['id', 'title']

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
