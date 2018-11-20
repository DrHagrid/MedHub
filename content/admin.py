# -*- coding: utf-8 -*-
from django.contrib import admin
from database.models import *
from .models import *


# Анатомия
class AnatomySectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['name', ]

    class Meta:
        model = AnatomySection


admin.site.register(AnatomySection, AnatomySectionAdmin)


# Гистология
class HistologySectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['name', ]

    class Meta:
        model = HistologySection


admin.site.register(HistologySection, HistologySectionAdmin)


# Физиология
class PhysiologySectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'variable']
    list_display_links = ['name', ]

    class Meta:
        model = PhysiologySection


admin.site.register(PhysiologySection, PhysiologySectionAdmin)
