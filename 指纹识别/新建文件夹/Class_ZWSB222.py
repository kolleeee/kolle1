#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#识别网站版本

import os
import re
import sys
import socket
import httplib
import gzip,StringIO
import Queue,threading
import time
from threading import Thread
socket.setdefaulttimeout(10)


shaoxiao = []  #要扫描的消息总数
ownsize= None  #消息总数
class Class_ZWSB(threading.Thread):  #指纹识别

    def __init__(self,urls):
        threading.Thread.__init__(self)
        self.queue = Queue.Queue()  #消息队列  这样就变成类独享了  就可以开多线程了   其实这个地方应该使用数组   多线程下 就不会重复读取数据了
        self.ownsize= None  #消息总数
        self.urls = urls
        self.A= int(time.strftime('%H%M%S'))  #计时
        self.zhiwen = [
            'dedecms','shopex','ecshop','zblog','aspcms','discuz','drupal','dvbbs','emlog','empirecms','espcms','foosuncms',
            'hdwiki','joomla','kesioncms','kingcms','ljcms','php168','phpcms','phpwind','powereasy','qibosoft','siteserver',
            'southidc','wordpress','cnhww','metinfo','cmseasy',]
        self.open_file_url()  #读取URL

    def open_file_url(self):  #读取URL
        try:
            #合并字典
            doclist = os.listdir(os.getcwd()+r'\finger')
            doclist.sort()
            for i in doclist:
                for url in open('finger/'+i,'r'):
                    if url.strip() not in shaoxiao:
                        shaoxiao.append(url.strip())
            for url in shaoxiao:
                #print url
                self.queue.put(url) #插入消息队列
            self.ownsize = len(shaoxiao)  #消息总数
        except Exception,e:
            #print e
            return 0

        class crackThread(Thread):  #研究下c++类的继承  和嵌套看怎么继承CS_linkftp类
            def __init__(self,queue1,urls,ownsize,zhiwen):
                Thread.__init__(self)
                self.queue=queue1  #队列
                self.urls=urls     #URL地址
                self.ownsize=ownsize  #控制进度条
                self.zhiwen=zhiwen #版本
                self.sotp=0
                while 1:
                    if self.queue.empty():   #判断队列是否为空
                        #print u"空"
                        break #跳出整个循环
                    if self.sotp==1:
                        break #跳出整个循环
                    data=self.queue.get(0.5).strip()  #get()方法从队头删除并返回一个项目
                    self.hack(data)


            def hack(self,uu):
                getsize = self.queue.qsize()
                ownsize = self.ownsize
                i = 100-getsize*100/ownsize
                sys.stdout.write('[LOG] <info> Sniffing for cms :'+str(i)+'%\r') #进度条
                sys.stdout.flush()
                headers = {'User-agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
                try:
                    args = self.urls.split('//')[1]
                    conn = httplib.HTTPConnection(args)
                    conn.request('GET',uu,None,headers)
                    httpres = conn.getresponse()
                    if httpres.status == 200:
                        if ('content-encoding', 'gzip') in httpres.getheaders():
                            compressedstream = StringIO.StringIO(httpres.read())
                            gzipper = gzip.GzipFile(fileobj=compressedstream)
                            html = gzipper.read()
                        else:
                            html = httpres.read()
                        for cms in self.zhiwen:
                            n = re.compile(cms)
                            m = n.findall(html,re.I)
                            #m = re.search(key,html,re.I)
                            if m:
                                global stop11
                                stop11="CMS  版本:"+cms
                                self.sotp=1


                except Exception,e:
                    print e
                    return 0

        threads = []  #线程
        for i in range(5):  #nthreads=10  创建10个线程
            threads.append(crackThread(self.queue,self.urls,self.ownsize,self.zhiwen))

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.start()  #start就是开始线程

        for thread in threads:   #不理解这是什么意思    是结束线程吗
            thread.join()
        print "time用时 %s S\r\n"%(int(time.strftime('%H%M%S'))-self.A)
        print stop11




################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(Class_ZWSB("http://www.133i.com"))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程




