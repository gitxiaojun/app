# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caiinfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('shijian', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=30, verbose_name='\u83dc\u540d')),
                ('miaoshu', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('img', models.ImageField(upload_to='upload', verbose_name='\u793a\u4f8b\u56fe\u7247')),
                ('gender', models.IntegerField(choices=[(0, '\u70ed\u5356\u5957\u9910'), (1, '\u6298\u6263\u4f18\u60e0')], default=1, verbose_name='\u6d3b\u52a8\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u83dc\u5355\u4fe1\u606f',
                'verbose_name_plural': '\u83dc\u5355\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='CaiType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shijian', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=200, verbose_name='\u83dc\u7cfb\u540d')),
            ],
            options={
                'verbose_name': '\u83dc\u7cfb',
                'verbose_name_plural': '\u83dc\u7cfb',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shijian', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30)),
                ('userlocation', models.CharField(max_length=500)),
                ('userxz', models.CharField(default='null', max_length=6)),
                ('userstep', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riqi', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=5)),
                ('titlen', models.CharField(max_length=100)),
                ('picurln', models.CharField(max_length=150)),
                ('urln', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Xiaohua',
            fields=[
                ('xid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('contentid', models.CharField(default=None, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Xingyun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riqi', models.CharField(max_length=15)),
                ('xingzuoming', models.CharField(max_length=6, unique=True)),
                ('zhengtiyunshixing', models.CharField(max_length=4)),
                ('aiqingyunshixing', models.CharField(max_length=4)),
                ('shiyeyunshixing', models.CharField(max_length=4)),
                ('caifuyunshixing', models.CharField(max_length=4)),
                ('jiankangzhishu', models.CharField(max_length=4)),
                ('shangtanzhishu', models.CharField(max_length=4)),
                ('xingyunyanse', models.CharField(max_length=8)),
                ('xingyunshuzi', models.CharField(max_length=3)),
                ('supeixingzuo', models.CharField(max_length=6)),
                ('duanping', models.CharField(max_length=100)),
                ('zhengtiyunshi', models.CharField(max_length=500)),
                ('aiqingyunshi', models.CharField(max_length=100)),
                ('shiyexueye', models.CharField(max_length=100)),
                ('caifuyunshi', models.CharField(max_length=100)),
                ('jiankangyunshi', models.CharField(max_length=100)),
                ('turl', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Youhuixinxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shijian', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=500, verbose_name='\u6807\u9898')),
                ('info', models.TextField(verbose_name='\u6b63\u6587')),
                ('img', models.ImageField(default='null', upload_to='upload', verbose_name='\u793a\u4f8b\u56fe\u7247')),
                ('begin_time', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4f18\u60e0\u4fe1\u606f',
                'verbose_name_plural': '\u4f18\u60e0\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='caiinfo',
            name='cai_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='weixin_main.CaiType', verbose_name='\u7c7b\u522b'),
        ),
    ]
