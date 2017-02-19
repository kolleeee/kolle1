#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import os
import re
import sys
import socket
import httplib
import gzip,StringIO
import Queue,threading
import time
from threading import Thread
import list
import hashlib
import urllib2
import class_Queue #消息队列维护
socket.setdefaulttimeout(10)

class Class_url_cms(threading.Thread):  #指纹识别
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.TH=i
        self.LS = list.Clist()  #初始化类
        self.LS.list_del()  #清空list列表
        self.open_file()  #读取CMS
        self.LS.liet_lsqc() #数组列表去重复
        print "run Thread:%d  cms:%s"%(self.TH,len(self.LS.list_2))

    def run_run(self):
        try:
            self.run()
        except:
            time.sleep(3)
            self.run()

    def run(self):
        try:
            if class_Queue.cms_url.empty():   #判断队列是否为空
                time.sleep(10)
                self.run_run()
            self.Chost = class_Queue.cms_url.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(10)
                self.run_run()

            if not self.open_url_200(self.Chost):
                class_Queue.S_suliang+=1  ##扫描完成的数量
                print "\rnot WEB url:%s"%(self.Chost),
                time.sleep(0.5)
                self.run_run()

            self.CS_cms(self.Chost) #测试url地址  CMS

        except:
            time.sleep(10)
            self.run_run()

    def open_url_200(self,url):  #判断URL是否能打开
        headers = {'User-agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        try:
            conn = httplib.HTTPConnection(url)
            conn.request('GET',"",None,headers)
            httpres = conn.getresponse()
            if httpres.status == 200:
                return httpres.read()
        except Exception,e:
            #print e
            return 0

    def open_file(self):
        try:
            #合并字典
            doclist = os.listdir(os.getcwd()+r'\cms')
            doclist.sort()
            for i in doclist:
                for url in open('cms/'+i,'r'):
                    data=url.strip().decode("gbk")
                    self.file_add(data)  #添加数组
                    #print self.list
                    #print len(self.list)
        except Exception,e:
            #print e
            return 0

    def file_add(self,data):  #添加数组
        try:
            if "#" in data:
                return 0
                #print data
            ss = data.split("|")
            self.LS.liet_add(ss)  #添加数据
        except Exception,e:
            #print e
            return 0

        ############################
    def CS_cms(self,url): #遍历页里的地址
        self.A= int(time.strftime('%H%M%S'))  #计时
        class crackThread(Thread):  #研究下c++类的继承  和嵌套看怎么继承CS_linkftp类
            def __init__(self,URL,list):
                Thread.__init__(self)
                self.URL=URL
                self.list=list
                self.B= int(time.strftime('%H%M%S'))  #计时
                self.for_list()

            def TXT_file_add(self,name,url):  #写入文本
                try:
                    file_object = open(name,'a')
                    file_object.writelines(url)
                    #file_object.write(url.encode("utf-8")) #成功
                    file_object.writelines("\n")
                    file_object.close()
                except Exception,e:
                    print name,"TXT except",url,e
                    return 0

            def url_post(self,URL):
                try:
                    req = urllib2.Request(URL)
                    req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
                    urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
                except:
                    pass

            def text_cms(self,url,cms): #CMS 处理方式
                try:
                    URL="http://webxscan.com/cms.php?url=%s&cms=%s"%(url,cms)
                    self.url_post(URL)   #后门
                    name="www/%s.txt"%(cms)
                    self.TXT_file_add(name,url)  #写入文本
                    class_Queue.OK_CMS+=1  #已经识别出来的RUL个数
                except:
                    pass

            def for_list(self):
                try:
                    for i in self.list:
                        #print i #URL链接文件(地址)|CMS名称|关键字|文件MD5
                        try:
                            if int(int(time.strftime('%H%M%S'))-self.B)>=class_Queue.cms_time:
                                message_data="url:%s CMS>=time:%s/S"%(url,class_Queue.cms_time)
                                print message_data
                                break #跳出整个循环
                            data=self.open_url(self.URL,i[0]) #网址  URL链接文件(地址)
                            if i[2]:#关键字
                                if data: #关键字匹配
                                    pname = re.compile(i[2])
                                    sarr = pname.findall(data)
                                    if sarr:
                                        print "\nurl:%s  cms:%s  hand_url:%s  KEY:%s"%(self.URL,i[1],i[0],i[2])
                                        self.text_cms(self.URL,i[1]) #CMS 处理方式
                                        break #跳出整个循环
                            if i[3]:#文件MD5
                                if data: #文件MD5
                                    list_feil_md5=self.GetFileMd5(data)
                                    if list_feil_md5[0]:
                                        if str(i[3]).lower()==str(list_feil_md5[1]):  #转换成小写在比对
                                            print "\nurl:%s  cms:%s  hand_url:%s  MD5:%s"%(self.URL,i[1],i[0],i[3])
                                            self.text_cms(self.URL,i[1]) #CMS 处理方式
                                            break #跳出整个循环
                        except:
                            pass
                except Exception,e:
                    #print e
                    return 0

            def open_url(self,url,hand_url):  #获取URL内容
                headers = {'User-agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
                try:
                    conn = httplib.HTTPConnection(url)
                    conn.request('GET',hand_url,None,headers)
                    httpres = conn.getresponse()
                    if httpres.status == 200:
                        return httpres.read()
                except Exception,e:
                    #print e
                    return 0

            def GetFileMd5(self,File_data):
                file = None
                #bRet = False
                strMd5 = ""
                try:
                    #file = open(strFile, "rb")
                    md5 = hashlib.md5()
                    strRead = File_data
                    #        while True:
                    #strRead = file.read(8096)
                    if not strRead:
                        return [0,""]
                    md5.update(strRead)
                    #read file finish
                    bRet = True
                    strMd5 = md5.hexdigest()
                except:
                    bRet = False
                finally:
                    if file:
                        file.close()
                return [bRet, strMd5]


        threads = []  #线程
        for i in range(1):  #nthreads=10  创建10个线程
            threads.append(crackThread(url,self.LS.list_2))

        for thread in threads:
            thread.start()  #start就是开始线程

        for thread in threads:
            thread.join()#结束线程吗
        class_Queue.S_suliang+=1  ##扫描完成的数量
        print "\nurl_cms:%s time:%s/S"%(url,int(time.strftime('%H%M%S'))-self.A)
        self.run()

