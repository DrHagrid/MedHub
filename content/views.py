# -*- coding: utf-8 -*-
from django.shortcuts import render
from user.models import UserInfo
from user.views import create_user_info
from content.models import *

# Внутренние функции


# Представления
def start_page(request):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    articles = Article.objects.filter(is_main=True)
    last_articles = list()
    for article in articles:
        last_articles.append(article)
    last_articles.reverse()
    last_articles = last_articles[0:6]
    return render(request, 'start.html', locals())


def unit_page(request, unit):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    unit = unit_list[unit]

    group_list = unit['group'].objects.all()
    return render(request, 'content/unit.html', locals())


def group_page(request, unit, group):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    unit = unit_list[unit]
    group = unit['group'].objects.get(variable=group)

    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        user_data = user_info.get_data()

    section_list = list()
    for section in unit['section'].objects.filter(group=group):
        elements = list()

        for article in section.articles.all():
            elements.append({'name': article.title, 'type': 'article',
                             'url': article.id, 'description': article.description})

        for test in section.tests.all():
            total = len(Test.objects.get(pk=test.id).questions.all())
            if request.user.is_authenticated:
                if not (unit['variable'] + "_" + group.variable + "_" + str(test.id) in user_data.keys()):
                    user_data[unit['variable'] + "_" + group.variable + "_" + str(test.id)] = {'correct': 0, 'incorrect': 0,
                                                                                          'incorrect_list': []}
                correct = user_data[unit['variable'] + "_" + group.variable + "_" + str(test.id)]['correct']
                correct_percent = round((int(correct) / total) * 100)
                incorrect_percent = 100 - correct_percent
            else:
                correct_percent = 0
                incorrect_percent = 0
            elements.append({'name': test.name, 'type': 'test',
                             'url': test.id, 'description': test.description,
                             'correct': correct_percent, 'incorrect': incorrect_percent})
        # Тест по латинским терминам
        if section.is_latin_test:
            total = len(unit['model'].objects.filter(group=group).filter(type=section.type))
            if request.user.is_authenticated:
                if not (unit['variable'] + "_" + group.variable + "_" + 'lat_' + section.type.variable in user_data.keys()):
                    user_data[unit['variable'] + "_" + group.variable + "_" + 'lat_' + section.type.variable] = {
                        'correct': 0, 'incorrect': 0, 'incorrect_list': []}
                correct = user_data[unit['variable'] + "_" + group.variable + "_" + 'lat_' + section.type.variable]['correct']
                correct_percent = round((int(correct) / total) * 100)
                incorrect_percent = 100 - correct_percent
            else:
                correct_percent = 0
                incorrect_percent = 0
            elements.append({'name': 'Тест по латинским терминам', 'type': 'test',
                             'url': 'lat_' + section.type.variable,
                             'description': 'Проверь свои знания латинским терминов',
                             'correct': correct_percent, 'incorrect': incorrect_percent})

        section_list.append({'name': section.type.name, 'elements': elements})

    return render(request, 'content/group.html', locals())


def articles_page(request, theme):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    themes = ArticleTheme.objects.all()
    articles = Article.objects.filter(is_main=True)
    if not(theme == 'all'):
        theme = ArticleTheme.objects.get(variable=theme)
        articles = articles.filter(theme=theme)
    article_list = list()
    for article in articles:
        article_list.append(article)
    article_list.reverse()
    return render(request, 'content/articles.html', locals())


def article_page(request, id):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    article = Article.objects.get(pk=id)
    return render(request, 'content/article.html', locals())


def section_article_page(request, unit, group, id):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    unit = unit_list[unit]
    group = unit['group'].objects.get(variable=group)

    article = Article.objects.get(pk=id)
    return render(request, 'content/article.html', locals())


def about_page(request):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    return render(request, 'content/about.html', locals())


def contacts_page(request):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    return render(request, 'content/contacts.html', locals())


def license_page(request):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    return render(request, 'content/license.html', locals())