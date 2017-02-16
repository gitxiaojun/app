# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import (TextMessage, VoiceMessage, ImageMessage,
                                 VideoMessage, LinkMessage, LocationMessage, EventMessage
                                 )

from wechat_sdk.context.framework.django import DatabaseContextStore
from .models import Youhuixinxi as Youhuixinximodel
from .models import Caiinfo as Caiinfomodel
# from getnews import getnews
from getlocation import getlocation
from models import location as locationModel
from models import Xingyun as XingyunModel
from models import Xiaohua as XiaohuaModel
from models import News as NewsModel
import urllib2
import time,re,sys,random
reload(sys)
sys.setdefaultencoding('utf8')
# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token='',
    appid='',
    appsecret=''
)
menu_list = {
    'button':[
        {
            'name': '有料一刻',
            'sub_button': [
                {
                    'type': 'click',
                    'name': '每日星运',
                    'key': 'V01_TODAY_xingzuo'
                },
                {
                    'type': 'click',
                    'name': '新闻要闻',
                    'key': 'V02_TODAY_news'
                },
                {
                    'type': 'click',
                    'name': '开心一笑',
                    'key': 'V03_laugh'
                }
            ]
        },
        {
            'name': '点餐',
            'sub_button': [
                {
                    'type': 'view',
                    'name': '菜单',
                    'url': 'http://www.bangwz.cn/dadmin'
                },
                {
                    'type': 'view',
                    'name': '优惠菜品',
                    'url': 'http://www.bangwz.cn/onsale'
                },
                {
                    'type': 'click',
                    'name': '店铺地址',
                    'key': 'V04_address'
                }
            ]
        }
    ]
}
wechat_instance.create_menu(menu_list)
def getxingzuo(word):
    if word in ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']:
        ltime = time.localtime()
        date_name = time.strftime("%Y年%m月%d日", ltime)
        try:
            xingyun_object = XingyunModel.objects.get(xingzuoming__contains=word, riqi=date_name)
            touxiangurl = xingyun_object.turl
            zhengtiyunshixing1 = xingyun_object.zhengtiyunshixing
            aiqingyunshixing1 = xingyun_object.aiqingyunshixing
            shiyeyunshixing1 = xingyun_object.shiyeyunshixing
            caifuyunshixing1 = xingyun_object.caifuyunshixing
            jiankangzhishu1 = xingyun_object.jiankangzhishu
            shangtanzhishu1 = xingyun_object.shangtanzhishu
            xingyunyanse1 = xingyun_object.xingyunyanse
            xingyunshuzi1 = xingyun_object.xingyunshuzi
            supeixingzuo1 = xingyun_object.supeixingzuo
            duanping1 = xingyun_object.duanping
            zhengtiyunshi1 = xingyun_object.zhengtiyunshi
            # aiqingyunshi1 = xingyun_object.aiqingyunshi
            # shiyexueye1 = xingyun_object.shiyexueye
            # caifuyunshi1 = xingyun_object.caifuyunshi
            # jiankangyunshi1 = xingyun_object.jiankangyunshi
            tihuanlist = {u'白羊座': 'Aries', u'金牛座': 'Taurus', u'双子座': 'Gemini', u'巨蟹座': 'Cancer', u'狮子座': 'Leo',
                          u'处女座': 'Virgo', u'天秤座': 'Libra', u'天蝎座': 'Scorpio', u'射手座': 'Sagittarius', u'摩羯座': 'Capricorn',
                          u'水瓶座': 'Aquarius', u'双鱼座': 'Pisces'}
            tihuanlist = dict((re.escape(k), v) for k, v in tihuanlist.iteritems())
            pattern = re.compile("|".join(tihuanlist.keys()))
            url123 = pattern.sub(lambda m: tihuanlist[re.escape(m.group(0))], word)
            response = wechat_instance.response_news([
                {
                    'title': '今日%s运势播报',
                    'picurl': '%s',
                    'url': 'http://www.xzw.com/fortune/%s/'},
                {
                    'title': '整体指数:%s,爱情指数:%s\n事业指数:%s,财运指数:%s\n健康指数:%s,商谈指数:%s', 'url': 'http://www.xzw.com/fortune/%s/'},
                {'title': '幸运颜色:%s,幸运数字:%s\n速配星座:%s', 'url': 'http://www.xzw.com/fortune/%s/'},
                {'title': '短评:%s\n-------------\n整体运势:\n%s', 'url': 'http://www.xzw.com/fortune/%s/'}
            ]) % (word, touxiangurl, url123, zhengtiyunshixing1, aiqingyunshixing1, shiyeyunshixing1, caifuyunshixing1,jiankangzhishu1, shangtanzhishu1, url123, xingyunyanse1, xingyunshuzi1, supeixingzuo1, url123,duanping1, zhengtiyunshi1, url123)
            return response
        except XingyunModel.DoesNotExist:
            tihuanlist = {u'白羊座': 'Aries', u'金牛座': 'Taurus', u'双子座': 'Gemini', u'巨蟹座': 'Cancer', u'狮子座': 'Leo',
                          u'处女座': 'Virgo', u'天秤座': 'Libra', u'天蝎座': 'Scorpio', u'射手座': 'Sagittarius', u'摩羯座': 'Capricorn',
                          u'水瓶座': 'Aquarius', u'双鱼座': 'Pisces'}
            tihuanlist = dict((re.escape(k), v) for k, v in tihuanlist.iteritems())
            pattern = re.compile("|".join(tihuanlist.keys()))
            word = pattern.sub(lambda m: tihuanlist[re.escape(m.group(0))], word)
            touxiangurl = "http://img.bangwz.cn/xingzuotouxiang/%s.png" % word
            xingzuoming = re.compile(ur'<dd><h4>(.+?)今日运势', re.DOTALL)
            zhengtiyunshixing = re.compile(ur'<label>整体运势：</label><span class="star_m star_blue"><em style="width:(.+?)px',
                                           re.DOTALL)
            aiqingyunshixing = re.compile(ur'<label>爱情运势：</label><span class="star_m star_blue"><em style="width:(.+?)px',
                                          re.DOTALL)
            shiyeyunshixing = re.compile(ur'<label>事业学业：</label><span class="star_m star_blue"><em style="width:(.+?)px',
                                         re.DOTALL)
            caifuyunshixing = re.compile(ur'<label>财富运势：</label><span class="star_m star_blue"><em style="width:(.+?)px',
                                         re.DOTALL)
            jiankangzhishu = re.compile(ur'<label>健康指数：</label>(.+?)</li>', re.DOTALL)
            shangtanzhishu = re.compile(ur'<li><label>商谈指数：</label>(.+?)</li>', re.DOTALL)
            xingyunyanse = re.compile(ur'<li><label>幸运颜色：</label>(.+?)</li>', re.DOTALL)
            xingyunshuzi = re.compile(ur'<li><label>幸运数字：</label>(.+?)</li>', re.DOTALL)
            supeixingzuo = re.compile(ur'<li><label>速配星座：</label>(.+?)</li>', re.DOTALL)
            duanping = re.compile(ur'<li class="desc"><label>短评：</label>(.+?)</li>', re.DOTALL)
            zhengtiyunshi = re.compile(ur'<p><strong class="p1">整体运势</strong><span>(.+?)</span>', re.DOTALL)
            aiqingyunshi = re.compile(ur'<p><strong class="p2">爱情运势</strong><span>(.+?)</span>', re.DOTALL)
            shiyexueye = re.compile(ur'<p><strong class="p3">事业学业</strong><span>(.+?)</span>', re.DOTALL)
            caifuyunshi = re.compile(ur'<p><strong class="p4">财富运势</strong><span>(.+?)</span>', re.DOTALL)
            jiankangyunshi = re.compile(ur'<p><strong class="p5">健康运势</strong><span>(.+?)</span>', re.DOTALL)
            # dingyi xingjitihuan de guize
            rep = {'16': u'一星', '32': u'二星', '48': u'三星', '64': u'四星', '80': u'五星完美'}
            rep = dict((re.escape(k), v) for k, v in rep.iteritems())
            pattern = re.compile("|".join(rep.keys()))
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/51.0.2704.106 Safari/537.36'}
            req = urllib2.Request(url="http://www.xzw.com/fortune/%s/" % word, headers=headers)
            html123 = urllib2.urlopen(req).read()
            html123 = html123.decode('gb2312')
            num0 = xingzuoming.findall(html123)
            xingzuoming1 = num0[0].encode('utf8')
            num1 = zhengtiyunshixing.findall(html123)[0]
            num1 = pattern.sub(lambda m: rep[re.escape(m.group(0))], num1)
            num2 = aiqingyunshixing.findall(html123)[0]
            num2 = pattern.sub(lambda m: rep[re.escape(m.group(0))], num2)
            num3 = shiyeyunshixing.findall(html123)[0]
            num3 = pattern.sub(lambda m: rep[re.escape(m.group(0))], num3)
            num4 = caifuyunshixing.findall(html123)[0]
            num4 = pattern.sub(lambda m: rep[re.escape(m.group(0))], num4)
            num5 = jiankangzhishu.findall(html123)[0]
            num6 = shangtanzhishu.findall(html123)[0]
            num7 = xingyunyanse.findall(html123)[0]
            num8 = xingyunshuzi.findall(html123)[0]
            num9 = supeixingzuo.findall(html123)[0]
            num10 = duanping.findall(html123)[0]
            num11 = zhengtiyunshi.findall(html123)[0]
            num12 = aiqingyunshi.findall(html123)[0]
            num13 = shiyexueye.findall(html123)[0]
            num14 = caifuyunshi.findall(html123)[0]
            num15 = jiankangyunshi.findall(html123)[0]
            try:
                XingyunModel.objects.get(xingzuoming=xingzuoming1)
                XingyunModel.objects.filter(xingzuoming=xingzuoming1).update(riqi=date_name, zhengtiyunshixing=num1,
                                                                         aiqingyunshixing=num2, shiyeyunshixing=num3,
                                                                         caifuyunshixing=num4, jiankangzhishu=num5,
                                                                         shangtanzhishu=num6, xingyunyanse=num7,
                                                                         xingyunshuzi=num8, supeixingzuo=num9,
                                                                         duanping=num10, zhengtiyunshi=num11,
                                                                         aiqingyunshi=num12, shiyexueye=num13,
                                                                         caifuyunshi=num14, jiankangyunshi=num15,
                                                                         turl=touxiangurl)
            except XingyunModel.DoesNotExist:
                bbb1 = XingyunModel(xingzuoming=xingzuoming1,riqi=date_name, zhengtiyunshixing=num1,
                                                                             aiqingyunshixing=num2,
                                                                             shiyeyunshixing=num3,
                                                                             caifuyunshixing=num4, jiankangzhishu=num5,
                                                                             shangtanzhishu=num6, xingyunyanse=num7,
                                                                             xingyunshuzi=num8, supeixingzuo=num9,
                                                                             duanping=num10, zhengtiyunshi=num11,
                                                                             aiqingyunshi=num12, shiyexueye=num13,
                                                                             caifuyunshi=num14, jiankangyunshi=num15,
                                                                             turl=touxiangurl)

                bbb1.save()
            xingyunneirong='''%s的记录为空,系统正在更新数据,请三秒后查询/:rose %s''' % (word, date_name)
            response = wechat_instance.response_text(content=xingyunneirong)
            return  response
    else:
        xingyunneirong = '''你输入的不是星座名,%s''' % word
        response = wechat_instance.response_text(content=xingyunneirong)
        return response

@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")

    # POST
    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')

    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()
    # 利用本次请求中的用户OpenID来初始化上下文对话
    context = DatabaseContextStore(openid=message.source)

    response = None

    if isinstance(message, TextMessage):
        if message.content == '优惠':
            response = wechat_instance.response_news([
                {
                    'title': '本店优惠菜品',
                    'picurl': 'http://img.bangwz.cn/static/images/1753663641.jpg',
                    'description': '点击跳转到本店优惠菜品页面',
                    'url': 'http://www.bangwz.cn/onsale',
                }
            ])
        elif message.content in ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座','白羊', '金牛', '双子', '巨蟹', '狮子', '处女', '天秤', '天蝎', '射手', '摩羯', '水瓶', '双鱼']:
            xinngzuoming = message.content
            xinngzuoming = xinngzuoming.strip('座')
            xinngzuoming += '座'
            response = getxingzuo(xinngzuoming)
            try:
                locationModel.objects.get(userid=message.source)
                locationModel.objects.filter(userid=message.source).update(userxz=xinngzuoming)

            except locationModel.DoesNotExist:
                uuu1 = locationModel(userid=message.source,userxz=xinngzuoming)
                uuu1.save()
        else:
            reply_text = ('未知对话！')
            response = wechat_instance.response_text(content=reply_text)
        return HttpResponse(response, content_type="application/xml")
        # 将新的数据存入上下文对话中
        context['step'] = step + 1
        context['last_text'] = content
        context.save()  # 非常重要！请勿忘记！临时数据保存入数据库！
    elif isinstance(message, VoiceMessage):
        reply_text = '语音信息我听不懂/:P-(/:P-(/:P-('
    elif isinstance(message, ImageMessage):
        reply_text = '图片信息我也看不懂/:P-(/:P-(/:P-('
    elif isinstance(message, VideoMessage):
        reply_text = '视频我不会看/:P-('
    elif isinstance(message, LinkMessage):
        reply_text = '链接信息'
    elif isinstance(message, LocationMessage):
        reply_text = '地理位置信息'
    elif isinstance(message, EventMessage):  # 事件信息
        if message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
            follow_event = Caiinfomodel.objects.get(keyword='关注事件')
            reply_text = follow_event.content
            # 如果 key 和 ticket 均不为空，则是扫描二维码造成的关注事件
            if message.key and message.ticket:
                reply_text += '\n来源：扫描二维码关注'
            else:
                reply_text += '\n来源：搜索名称关注'
            response = wechat_instance.response_text(content=reply_text)
            return HttpResponse(response, content_type="application/xml")
        elif message.type == 'unsubscribe':
            reply_text = '取消关注事件'
            response = wechat_instance.response_text(content=reply_text)
            return HttpResponse(response, content_type="application/xml")
        elif message.type == 'scan':
            reply_text = '已关注用户扫描二维码！'
            response = wechat_instance.response_text(content=reply_text)
            return HttpResponse(response, content_type="application/xml")
        elif message.type == 'location':
            addr = getlocation(message.latitude,message.longitude)
            try:
                locationModel.objects.get(userid=message.source)
                locationModel.objects.filter(userid=message.source).update(userlocation=addr)
            except locationModel.DoesNotExist:
                u1 = locationModel(userid=message.source,userlocation=addr)
                u1.save()
            # reply_text = '''你当前的位置为: %s ''' % addr
            # response = wechat_instance.response_text(content=reply_text)
            # return HttpResponse(response, content_type="application/xml")
        elif message.type == 'click':
            if message.key == 'V01_TODAY_xingzuo':
                try:
                    userxingzuo = locationModel.objects.values("userxz").get(userid=message.source)['userxz']
                    if userxingzuo == 'null':
                        reply_text = "请输入你的星座名1"
                        response = wechat_instance.response_text(content=reply_text)
                    else:
                        response = getxingzuo(userxingzuo)
                except locationModel.DoesNotExist:
                    reply_text = "请输入你的星座名2"
                    response = wechat_instance.response_text(content=reply_text)
                return HttpResponse(response, content_type="application/xml")
            if message.key == 'V02_TODAY_news':
                numid = NewsModel.objects.count()
                if numid <12:
                    numid = 12
                content1 = []
                random_list = set()
                for i in range(10):
                    random_list.add(random.randrange(2,numid,2))

                for i in random_list:
                    d = {}
                    try:
                        d['title'] = NewsModel.objects.values("titlen").get(newid=i)["titlen"]
                        d['picurl'] = NewsModel.objects.values("picurln").get(newid=i)["picurln"]
                        d['url'] = NewsModel.objects.values("urln").get(newid=i)["urln"]
                        content1.append(d)
                    except NewsModel.DoesNotExist:
                        pass
                response = wechat_instance.response_news(content1)
                return HttpResponse(response, content_type="application/xml")
            if message.key == 'V03_laugh':
                numid =random.randrange(2, XiaohuaModel.objects.count(),2)
                try:
                    reply_text = XiaohuaModel.objects.values("content").get(xid=numid)['content']
                except XiaohuaModel.DoesNotExist:
                    reply_text = XiaohuaModel.objects.values("content").latest('xid')['content']
                response = wechat_instance.response_text(content=reply_text)
                return HttpResponse(response, content_type="application/xml")
            if message.key == 'V04_address':
                reply_text = '运城空港新区100街区11号 联系电话：0359-10258888'
                response = wechat_instance.response_text(content=reply_text)
                return HttpResponse(response, content_type="application/xml")
        elif message.type == 'view':
            pass
            # reply_text = '自定义菜单跳转链接'
            # response = wechat_instance.response_text(content=reply_text)
            # return HttpResponse(response, content_type="application/xml")
        elif message.type == 'templatesendjobfinish':
            reply_text = '模板消息'
            response = wechat_instance.response_text(content=reply_text)
            return HttpResponse(response, content_type="application/xml")
