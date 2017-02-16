#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from weixin_main.models import Youhuixinxi as YouhuixinxiModel

def index(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'index.html', {'TutorialList': TutorialList})
def onsale(request):
    if request.method == 'GET':
        onsalexinxi = []
        for i in YouhuixinxiModel.objects.all():
            info_dict = {'name':i.name,'img':i.img,'info':i.info,'begin_time':i.begin_time,'end_time':i.end_time}
            onsalexinxi.append(info_dict)
    return render(request, 'onsale.html', {'onsalexinxi': onsalexinxi})