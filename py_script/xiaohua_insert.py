#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode
import time,random
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
pageid = random.randint(1, 1000)
url = "http://japi.juhe.cn/joke/content/list.from"
params = {
             "sort": "desc",
             "page": pageid,
             "pagesize": "20",
             "time": str(time.time())[:10],
             "key": "19d8c93cd0d36dbfe8599f359ef1fa74"}
params = urlencode(params)
f = urllib.urlopen("%s?%s" % (url, params))
content = f.read()
res = json.loads(content)
if res:
    error_code = res["error_code"]
    if error_code == 0:
        conn = MySQLdb.connect(host='localhost', user='yczjd', passwd='yczjd', db='yczjd')
        cur = conn.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        csql = 'select count(1) from weixin_main_xiaohua;'
        idnum3 = cur.execute(csql) + 1
        for i in range(20):
            xiaohua = res["result"]["data"][i]["content"]
            xiaohuaid = res["result"]["data"][i]["hashId"]
            xiaohuaid = str(xiaohuaid)
            xiaohua = str(xiaohua)
            sql = '''insert into weixin_main_xiaohua(xid,content,contentid) VALUES (\'%s\',\'%s\',\'%s\');''' % (idnum3,xiaohua,xiaohuaid)
            sql = sql.encode('utf8')
            try:
                cur.execute(sql)
                idnum3 += 1
            except MySQLdb.Error:
                pass
        conn.commit()
        cur.close()
        conn.close()
    else:
        print "状态不是200"
else:
    print "没有获取到数据"