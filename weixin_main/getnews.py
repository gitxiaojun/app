import json, urllib
from urllib import urlencode
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import random


def getnews(a):
    url = "http://v.juhe.cn/toutiao/index"
    params = {
        "key": '',
        "type": a,
    }
    params = urlencode(params)
    f = urllib.urlopen("%s?%s" % (url, params))
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            content1 = []
            random_list = random.sample(range(0, 30), 10)
            for i in random_list:
                d = {}
                d['title'] = res['result']["data"][i]['title']
                d['picurl'] = res['result']["data"][i]['thumbnail_pic_s']
                d['url'] = res['result']["data"][i]['url']
                content1.append(d)
            return content1
        else:
            content1 = "%s:%s" % (res["error_code"], res["reason"])
            return content1
    else:
        content1 = "request api error"
        return content1
