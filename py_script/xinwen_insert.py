import json, urllib
from urllib import urlencode
import sys,MySQLdb,hashlib

reload(sys)
sys.setdefaultencoding('utf8')


def getnews(a):
    url = "http://v.juhe.cn/toutiao/index"
    params = {
        "key": '7ee6c2268c3008929f090b9e63add5c4',
        "type": a,
    }
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
            # print res["result"]["data"]
            csql = 'select count(1) from weixin_main_news;'
            idnum3 = cur.execute(csql) + 1
            for i in res["result"]["data"]:
                bbb2 = hashlib.md5()
                bbb2.update(i['title'])
                checksum = bbb2.hexdigest()
                tname = i['title']
                tname = str(tname).replace('"','')
                sql = ''' INSERT INTO  weixin_main_news(newid,checksum,datet,type,titlen,picurln,urln) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\") ;'''%(idnum3,checksum,i['date'],a,tname,i['thumbnail_pic_s'],i['url'])
                sql = sql.encode('utf8')
                # print sql
                try:
                    cur.execute(sql)
                    idnum3 += 1
                except MySQLdb.Error:
                    print 'error'
            conn.commit()
            cur.close()
            conn.close()
        else:
            content1 = "%s:%s" % (res["error_code"], res["reason"])
            return content1
    else:
        content1 = "request api error"
        return content1
news_type_list = ('top','shehui','junshi','guonei','guoji','yule','tiyu','keji','caijing','shishang')
for i in news_type_list:
    getnews(i)