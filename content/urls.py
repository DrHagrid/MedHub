# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^robots\.txt$', views.robots, name='robots'),
    url(r'^sitemap\.xml$', views.sitemap, name='sitemap'),

    url(r'^$', views.start_page, name='start'),
    url(r'^start/(?P<unit>\w+)/$', views.unit_page, name='unit_page'),
    url(r'^start/(?P<unit>\w+)/(?P<section>\w+)/$', views.section_page, name='group_page'),
    url(r'^articles/(?P<theme>\w+)/$', views.articles_page, name='articles_page'),
    url(r'^start/(?P<unit>\w+)/(?P<section>\w+)/article/(?P<id>\w+)/$', views.section_article_page, name='section_article_page'),
    url(r'^article/(?P<id>\w+)/$', views.article_page, name='article_page'),

    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^contacts/$', views.contacts_page, name='contacts_page'),
    url(r'^license/$', views.license_page, name='license_page'),
]
