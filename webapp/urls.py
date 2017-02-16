#!/usr/bin/env python
# -*- coding:utf-8 -*-
#webapp_urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^onsale',views.onsale,name='onsale')
]