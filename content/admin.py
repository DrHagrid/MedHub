# -*- coding: utf-8 -*-
from django.contrib import admin
from database.models import *
from .models import *


# Анатомия
class AnatomySectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'type']
    list_display_links = ['id', 'group']

    class Meta:
        model = AnatomySection


admin.site.register(AnatomySection, AnatomySectionAdmin)


# Гистология
class HistologySectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'group']
    list_display_links = ['id', 'group']

    class Meta:
        model = HistologySection


admin.site.register(HistologySection, HistologySectionAdmin)
