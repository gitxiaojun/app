#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


# Create your models here.


class Gender(models.Model):
    shijian = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    name = models.CharField(max_length=32)


class Caiinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    shijian = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    name = models.CharField(max_length=30, verbose_name='菜名', editable=True)
    miaoshu = models.TextField(verbose_name='描述')
    img = models.ImageField(upload_to='upload', verbose_name='示例图片')
    cai_type = models.ForeignKey("CaiType", null=True, blank=True, verbose_name='类别')
    gender_choices = (
        (0, "热卖套餐"),
        (1, "折扣优惠"),
    )
    gender = models.IntegerField(choices=gender_choices, default=1, verbose_name="活动类型")

    class Meta:
        verbose_name = '菜单信息'
        verbose_name_plural = '菜单信息'

    def __str__(self):
        return self.name


class Caiinfo_list(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['cai_type']}),
        (None, {'fields': ['miaoshu']}),
        (None, {'fields': ['img']}),
    ]
    list_display = ('name', 'cai_type', 'shijian')
    list_filter = ['name']
    search_fields = ['name']


class CaiType(models.Model):
    shijian = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    name = models.CharField(max_length=200, verbose_name='菜系名')

    class Meta:
        verbose_name = '菜系'
        verbose_name_plural = '菜系'

    def __str__(self):
        return self.name


class CaiType_list(admin.ModelAdmin):
    list_display = ('name', 'shijian')


class Youhuixinxi(models.Model):
    shijian = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    name = models.CharField(max_length=500, verbose_name='标题')
    info = models.TextField(verbose_name='正文')
    img = models.ImageField(upload_to='upload', verbose_name='示例图片', default='null')
    begin_time = models.DateTimeField('开始时间')
    end_time = models.DateTimeField('结束时间')

    # begin_time = models.DateTimeField(widget=widgets.AdminDateWidget(), label=u'活动开始时间')
    class Meta:
        verbose_name = '优惠信息'
        verbose_name_plural = '优惠信息'

    def __str__(self):
        return self.name


class Youhuixinxi_list(admin.ModelAdmin):
    list_display = ('name', 'shijian')


class Xingyun(models.Model):
    riqi = models.CharField(max_length=15)
    xingzuoming = models.CharField(max_length=6, unique=True)
    zhengtiyunshixing = models.CharField(max_length=4)
    aiqingyunshixing = models.CharField(max_length=4)
    shiyeyunshixing = models.CharField(max_length=4)
    caifuyunshixing = models.CharField(max_length=4)
    jiankangzhishu = models.CharField(max_length=4)
    shangtanzhishu = models.CharField(max_length=4)
    xingyunyanse = models.CharField(max_length=8)
    xingyunshuzi = models.CharField(max_length=3)
    supeixingzuo = models.CharField(max_length=6)
    duanping = models.CharField(max_length=100)
    zhengtiyunshi = models.CharField(max_length=500)
    aiqingyunshi = models.CharField(max_length=100)
    shiyexueye = models.CharField(max_length=100)
    caifuyunshi = models.CharField(max_length=100)
    jiankangyunshi = models.CharField(max_length=100)
    turl = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class News(models.Model):
    newid = models.IntegerField(primary_key=True,default=1,unique=True)
    checksum = models.CharField(max_length=253,unique=True,default=None)
    datet = models.DateTimeField(default=None)
    type = models.CharField(max_length=10)
    titlen = models.CharField(max_length=100)
    picurln = models.CharField(max_length=150)
    urln = models.CharField(max_length=150)

class location(models.Model):
    userid = models.CharField(max_length=30,primary_key=True)
    userlocation = models.CharField(max_length=500)
    userxz = models.CharField(max_length=6,default='null')
    userstep = models.IntegerField(default=1)

class Xiaohua(models.Model):
    xid = models.IntegerField(primary_key=True,default=1,unique=True)
    content = models.TextField()
    contentid = models.CharField(max_length=32,default=None)