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
    return statusCode==200  #返回 True  False
########################################################
if __name__ == '__main__':
#    data="""<a href="http://fj-kw.com/daiyun/zeh1n7n7/index.html" target="_blank">绍兴按摩</a>"""
#    print re_cx_data('(?<=href\=\").*?(?=\")',data)
    print test("http://fj-kw.com/daiyun/zeh1n7nss/")

