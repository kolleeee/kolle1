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
socket.setdefaulttimeout(10)

queue = Queue.Queue()  #消息队列
shaoxiao = []  #要扫描的消息总数
ownsize= None  #消息总数
class Class_ZWSB(threading.Thread):  #指纹识别
    zhiwen = [
        'dedecms','shopex','ecshop','zblog','aspcms','discuz','drupal','dvbbs','emlog','empirecms','espcms','foosuncms',
        'hdwiki','joomla','kesioncms','kingcms','ljcms','php168','phpcms','phpwind','powereasy','qibosoft','siteserver',
        'southidc','wordpress','cnhww','metinfo','cmseasy',]

    def __init__(self,urls):
        threading.Thread.__init__(self)
        self.urls = urls
        self.ownsize = ownsize
        self.servie = servie
        self.stop = False
        while 1:
            if queue.empty() == True or self.servie or self.stop:
            #if queue.empty() == True:
                break
            self.hack()

    def hack(self):
        uu = queue.get().strip()
        getsize = queue.qsize()
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
                        print "111111111"+cms
                        self.servie = cms
        except Exception,e:
            #print e
            self.stop = True #为了防止经常性超时 有超时情况出现结束指纹识别！
            pass
def scan_finger(urls):
    global servie #版本
    servie = None

    global ownsize #消息总数
    ownsize= None  #消息总数
    threads = []
    #合并字典
    doclist = os.listdir(os.getcwd()+r'\finger')
    doclist.sort()

    for i in doclist:
        for url in open('finger/'+i,'r'):
            if url.strip() not in shaoxiao:
                shaoxiao.append(url.strip())
    for url in shaoxiao:
        #print url
        queue.put(url) #插入消息队列
    ownsize = len(shaoxiao)  #消息总数
    for x in range(5):  #启动5个线程扫描
        y = Class_ZWSB(urls)
        y.start()
        threads.append(y)
    for x in threads:
        x.join()
    if servie:
        sys.stdout.write('[LOG] <info> Sniffing for cms :'+servie+'\r\n') #进度条
        sys.stdout.flush()
    else:
        sys.stdout.write(u'[LOG] <info> Sniffing for cms : 版本不在识别范围内'+'\r\n') #进度条
        sys.stdout.flush()
    if servie:
        return servie
    else:
        return u'版本不在识别范围内'




if __name__ == '__main__':#引入本地模拟环境
    scan_finger('http://www.133i.com')
################################################
#if __name__=='__main__':
#    threads = []  #线程
#    nthreads=1
#    for i in range(nthreads):  #nthreads=10  创建10个线程
#        threads.append(cms("www.skyscom.com"))
#
#    for t in threads:   #不理解这是什么意思    是结束线程吗
#        t.start()  #start就是开始线程




