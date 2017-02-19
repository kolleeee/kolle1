#!/usr/bin/python
#coding:utf8
#filename:URLLister.py
#神龙  QQ29295842
from sgmllib import SGMLParser

class URLLister(SGMLParser):  #注意这里的处理html的类是继承了SGMLParser类的。。。
    def reset(self):
        try:
            SGMLParser.reset(self)
            self.urls = []
        except Exception,e:
            print "reset111111111111",e
            return 0

    def start_a(self,attrs):  #这里的是找的所有的<a>标签。
        try:
            href = [v for k,v in attrs if k=='href']  #这里的语法很特别，返回的是一个列表
            if href:
                self.urls.extend(href)
        except Exception,e:
            print "start_a111111111111",e
            return 0
