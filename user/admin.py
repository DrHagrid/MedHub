# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']

    class Meta:
        model = UserInfo


admin.site.register(UserInfo, UserInfoAdmin)
