# -*- coding:utf-8 -*-
import urllib2
import random
import re
def getlocation(jingdu,weidu):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    headers = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"]

    url = "http://www.gpsspg.com/apis/maps/geo/?output=jsonp&lat=%s0&lng=%s&type=0&callback=jQuery110205437386237656285_1481075582455&_=1481075582457" %(jingdu,weidu)
    random_header = random.choice(headers)
    """
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典中就是下面元组的键值对应
    """
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("GET",url)
    # req.add_header("Host","www.baidu.com")
    req.add_header("Referer","http://www.gpsspg.com/iframe/maps/baidu_161128.htm?mapi=1")
    content = urllib2.urlopen(req).read()
    address = re.compile(ur'"address":"(.+?)",',re.DOTALL)
    weizhi = address.findall(content)[0]
    return weizhi