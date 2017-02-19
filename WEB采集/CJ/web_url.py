#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import time
import urllib
import re
import list
import urllib2
import urllister
import class_Queue  #消息队列
url_root1 = class_Queue.url_root1  #要采集的URL
url_root2 = class_Queue.url_root2  #要存贮URL


class web_url(threading.Thread):
    def __init__(self,url,th,max): #url   线程   深度
        threading.Thread.__init__(self)
        global url_gjz
        self.url=url  #url
        self.urlname=self.url  #限制#域名关键字
        self.th=th  #线程
        self.max=max  #深度

    def run(self):
        try:
            global url_root1
            if url_root1.empty():   #判断队列是否为空
                print u"已经没有可操作的URL了"
                time.sleep(30)
                self.run()
            if url_root2.qsize()>=8000:  #
                print u"url_root2 >=8000"
                time.sleep(30)
                self.run()
            self.URL = url_root1.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.URL==0:  #读取网页内容
                print u"%s:URL网站可能无法打开"%(self.URL)
                time.sleep(5)
                self.run()
            self.CS_URL(self.URL)

            self.run()
        except Exception,e:
            print e
            self.run()
            return 0

    def CS_URL(self,url):  #采集URL
        try:
            global url_root2
            print u"开始采集:",url
            list_2=[]
            list=self.getURL(url)
            if list==0:
                return 0
            for i in list:  #去重重复数据
                if i not in list_2:
                    if self.urlname in i:
                        list_2.append(i)
#            if len(list_2) > 0:
            for url in list_2:
                http=url[0:7]  #提取http
                if http=="http://":
                    url_root2.put(url.strip().lstrip().rstrip('\n'),0.5)   #插入队列
            return 0
        except Exception,e:
            print e
            return 0

    def getURL(self,URL):  #getURL(url)用来将HTML中的url放入urls列表中
        try:
            LS = list.Clist()  #初始化类
            LS.list_del()  #清空list列表
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            p = re.compile( r'<a.+?href=.+?>.+?</a>' )
            pname = re.compile( r'(?<=>).*?(?=</a>)' )
            phref = re.compile( r'(?<=href\=\").*?(?=\")')
            #构造及编译正则表达式
            sarr = p.findall(ss)#找出一条一条的<a></a>标签   #这添加到数组在过滤重复值减少mysql压力
            i=0
            for every in sarr:
                if i>=3000:
                    break
                else:
                    i+=1
                sname = pname.findall( every )
                if sname:
                    #sname = sname[0]
                    shref = phref.findall( every )
                    if shref:
                        shref = shref[0]
                        #print shref #获取URL
                        http=shref[0:7]  #提取http
                        if http=="http://":
                            LS.liet_add(shref)  #添加到数组
            LS.liet_lsqc() #数组列表去重复
            return LS.list_2

        except Exception,e:
            print u"getURL",e
            return 0
