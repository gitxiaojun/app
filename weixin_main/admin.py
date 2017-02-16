#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.contrib import admin

# Register your models here.
from weixin_main import models
admin.site.register(models.Caiinfo,models.Caiinfo_list)
admin.site.register(models.CaiType,models.CaiType_list)
admin.site.register(models.Youhuixinxi,models.Youhuixinxi_list)
