# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test_data/$', views.test_data, name='test_data'),
    url(r'^start/(?P<unit>\w+)/(?P<group>\w+)/test/(?P<test_id>\w+)/$', views.test_page, name='test_page'),
    url(r'^start/(?P<unit>\w+)/(?P<group>\w+)/test/(?P<test_id>\w+)/stat/$', views.stat_page, name='stat_page'),

]
