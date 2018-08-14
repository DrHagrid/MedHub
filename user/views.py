# -*- coding: utf-8 -*-
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from .models import *


def create_user_info(request):
    if request.user.is_authenticated:
        user_info, created = UserInfo.objects.get_or_create(user=request.user)
    else:
        created = False
    return created


class RegisterFormView(FormView):
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "../login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "user/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "user/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
