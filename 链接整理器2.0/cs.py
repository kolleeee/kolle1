#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import re
import httplib
import StringIO
import gzip
import urllib
import urllib2
import ConfigParser  #INI读取数据

def re_cx_data(re_data,data):  #正则查询内容是否存在
    p = re.compile( r'%s'%re_data )
    sarr = p.findall(data)
    if len(sarr[0])>=7:
        return True,sarr[0]
    else:
        return False,0
    #return sarr[0]

import urllib
def url_http_200(url):
    statusCode =urllib.urlopen(url).getcode()
    #return statusCode==200  #返回 True  False
    if statusCode==200:
        #local = url.split('/')[-1]
        if len(urllib.urlopen(url).read())>=1000:
            return True
    return False
########################################################
if __name__ == '__main__':
#    data="""<a href="http://fj-kw.com/daiyun/zeh1n7n7/index.html" target="_blank">绍兴按摩</a>"""
#    print re_cx_data('(?<=href\=\").*?(?=\")',data)
#    print test("http://fj-kw.com/daiyun/zeh1n7nss/")
#    url_http_200("http://blog.sina.com.cn/s/blog_44c43500010008pz.html")
    data2="""<a href="$url" target="_blank">$key</a>"""
    data2=data2.replace('$url','11111111111')
    data2=data2.replace('$key','222222')
    print data2















