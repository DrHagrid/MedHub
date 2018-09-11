# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from user.models import UserInfo
from user.views import create_user_info
from content.models import *
import json


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

    section_list = unit['section'].objects.all()
    return render(request, 'content/unit.html', locals())


def section_page(request, unit, section):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    unit = unit_list[unit]
    section = unit['section'].objects.get(variable=section)

    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        if user_info.data:
            user_data = user_info.get_data()
        else:
            user_data = dict()

    elements = list()
    for element in section.get_content():
        if element['type'] == 'article':
            article = Article.objects.get(pk=element['id'])
            elements.append({'name': article.title, 'type': 'article',
                             'url': article.id, 'description': article.description,
                             'image': article.image})
        elif element['type'] == 'test':
            test = Test.objects.get(pk=element['id'])

            total = len(test.questions.all())
            if request.user.is_authenticated:
                if not (unit['variable'] + "_" + section.variable + "_" + str(test.id) in user_data.keys()):
                    user_data[unit['variable'] + "_" + section.variable + "_" + str(test.id)] = {'correct': 0, 'incorrect': 0,
                                                                                          'incorrect_list': []}
                    user_info.set_data(user_data)
                    user_info.save()
                correct = user_data[unit['variable'] + "_" + section.variable + "_" + str(test.id)]['correct']
                incorrect = user_data[unit['variable'] + "_" + section.variable + "_" + str(test.id)]['incorrect']
                correct_percent = round((int(correct) / total) * 100)
                incorrect_percent = round((int(incorrect) / total) * 100)
            else:
                correct_percent = 0
                incorrect_percent = 0
            elements.append({'name': test.name, 'type': 'test',
                             'url': test.id, 'description': test.description,
                             'image': test.image,
                             'correct': correct_percent, 'incorrect': incorrect_percent})

    return render(request, 'content/section.html', locals())


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


def section_article_page(request, unit, section, id):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    unit = unit_list[unit]
    section = unit['section'].objects.get(variable=section)

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


# Файлы индексирования
def robots(request):
    return render(request, 'robots.txt', content_type='text/plain')


def sitemap(request):
    return render(request, 'sitemap.xml', content_type='text/plain')
