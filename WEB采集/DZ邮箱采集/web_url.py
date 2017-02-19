#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import threading
import socket
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import time
import urllib
import re
from bs4 import BeautifulSoup as soup
import class_Queue  #消息队列
url_root1 = class_Queue.url_root1  #要采集的URL
url_root2 = class_Queue.url_root2  #要存贮URL
url_xl= 0 #URL提取的数量

class web_url(threading.Thread):
    def __init__(self,url,id): #url   线程   深度
        threading.Thread.__init__(self)
        global url_gjz
        self.id=id  #ID
        self.url=url  #url
        self.urlname=self.url  #限制#域名关键字
        self.file_name=self.url
        self.file_name=self.file_name.replace('http://','')
        self.file_name=self.file_name.replace('https://','')
        self.file_name=self.file_name.replace('/','_')
        #self.th=th  #线程
        #self.max=max  #深度

    def run1(self):
        try:
            self.run()
        except Exception,e:
            self.run()
            pass
    def run(self):
        try:
            global url_root1
            global url_xl
            if url_root1.empty():   #判断队列是否为空
                print u".",
                time.sleep(30)
                self.run1()
            if url_root2.qsize()>=5000:  #
                url_xl+= 1 #URL提取的数量
                print u"url_root2 >=5000"
                time.sleep(30)
                self.run1()
            self.URL = url_root1.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.URL==0:  #读取网页内容
                time.sleep(5)
                self.run1()
            self.CS_URL(self.URL)
            url_xl+= 1 #URL提取的数量

            self.run1()
        except Exception,e:
            print e
            self.run1()
            return 0

    def CS_URL(self,url):  #采集URL
        try:
            global url_root2
            list=self.getURL(url)
            a=0
            for i in list:  #去重重复数据
                if self.urlname in i:
                    a=a+1
                    url_root2.put(i.strip().lstrip().rstrip('\n'),0.5)   #插入队列
            print u"TXID:%d采集url:%s --%d个地址要存储"%(self.id,url,a)
            return 0
        except Exception,e:
            pass

    def URL_TQURL(self,url): #URL提取URL
        try:
            #查看字符串结尾是否是/是就直接返回  http://www.383k.com/bbs/
            data=url[len(url)-1:len(url)]
            if data=="/":
                return url
                #截取字符串 http://www.383k.com/bbs/forum-4-1.html   http://www.383k.com/bbs/
            nPos =url.rfind('/') #查找字符  从尾部查找
            sStr1 = url[0:nPos+1] #复制指定长度的字符
            return sStr1
        except:
            pass

    def gl_url(self,url):   #过滤模糊的链接
    #forumdisplay.php?fid=48&orderby=lastpost&filter=7948800
    #forumdisplay.php?fid=48
        try:
            self.nPos =url.index('&') #查找字符
            if self.nPos>0:
                sStr1 = url[0:self.nPos] #复制指定长度的字符
                return sStr1
            return url
        except Exception,e:
            return url
            pass

    def TXT_file_email(self,data):  #写入文本
        try:
            file_object = open("email\\"+self.file_name+"email.txt",'a+')
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            pass

#    def TXT_file_QQ(self,data):  #写入文本
#        try:
#            file_object = open("QQ\\"+self.file_name+"QQ.txt",'a+')
#            file_object.writelines(data)
#            file_object.writelines("\n")
#            file_object.close()
#        except Exception,e:
#            pass

    def getURL(self,url):  #getURL(url)用来将HTML中的url放入urls列表中
        try:
            self.list=[]
            self.list_2=[]
            self.uk=self.URL_TQURL(url) #URL提取URL
            url1 = urllib.urlopen(url)
            s = url1.read()
            url1.close()
            #正则获取邮箱
            try:
                #(<)?\s*(\w+@\w+)\s*(?(1)>)
                #(<)?\s*(\w+@\S+)\s*(?(1)>)
                #[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}
                #\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b
                email=re.findall('[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}',s,re.I)
                for i in email:
                    print u"邮箱地址:",i
                    self.TXT_file_email(i)  #写入文本
            except Exception,e:
                pass
#            #正则QQ  误差太大了
#            try:
#                #^[1-9]{1}[0-9]{4,8}$
#                #^[1-9]*[1-9][0-9]*$
#                #[1-9][0-9]{4})|([0-9]{6,10
#                qq=re.findall('[1-9][0-9]{5,9}',s,re.I)
#                for i in qq:
#                    print u"QQ号:",i
#                    self.TXT_file_QQ(i)  #写入文本
#            except Exception,e:
#                pass

            list = soup(s)
            lr = list.findAll({'dd':True,'b':True,'li':True,'span':True, 'h2':True})  #'li':True,'span':True, 'h2':True
            for i in lr:
                try:
                #                print i
                    url1=i.a['href']
                    #                for L in [".html",".htm",".php",".asp"]:
                    #                    if url.__contains__(L):
                    url1=self.gl_url(url1)   #过滤模糊的链接
                    data=url1[0:1]
                    if data=="/":
                        url1=url1[1:len(url1)]
                    data=url1[0:4] #http
                    if data=="http":
                        shref="%s"%(url1)
                    else:
                        shref="%s%s"%(self.uk,url1)
                    http=shref[0:4]  #提取http
                    if http=="http":
                        self.list.append(shref)  #添加数据
                except:
                    pass

            for i in self.list:
                if i not in self.list_2:
                    self.list_2.append(i)

            return self.list_2

        except Exception,e:
            print u"getURL",e
            pass
