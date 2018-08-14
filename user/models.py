# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import json


class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    data = models.TextField(blank=True, null=True, verbose_name='Данные', help_text='Поле для хранения JSON информации')

    def set_data(self, x):
        self.data = json.dumps(x)

    def get_data(self):
        return json.loads(self.data)

    def __str__(self):
        return "%s" % self.user.username

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'
