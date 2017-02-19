#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
import web_url
#from class_Queue import C_Queue  #消息队列
import class_Queue  #消息队列
import threading
import time
#神龙  QQ:29295842
url_root1 = class_Queue.url_root1  #当前要采集的URL
#url_close = class_Queue.url_close #数据库被清空

##################################################
import sys
import os
import atexit
def close1():
    try:
        close()
    except:
        close()
def close():  #自动重启本程序
    try:
        print u"------------------自动重启本程序------------------"
        python = sys.executable
        os.execl(python, python, * sys.argv)
        #########
    except:
        print u"------------------自动重启本程序---异常------------------"
        close1()
        pass
        #sys.exit(0)  #结束进程

bool=1  #控制采集
def tx_run(url): #线程系统
    try:
        global url_root1
        global bool
        bool=0  #控制采集
        #th=5 #线程
        #max=5 #深度
        #消息队列维护
        url_root1.put(url,0.5)   #插入队列
        tx_Queue = []  #线程
        tx_web_url = []  #线程
        for i in range(1):
            tx_Queue.append(class_Queue.C_Queue())
        for t in tx_Queue:
            t.start()
            #采集
        for i in range(5):  #nthreads=10  创建10个线程
            t = tx_web_url.append(web_url.web_url(url,i))
        for t1 in tx_web_url:   #不理解这是什么意思    是结束线程吗
            t1.start()  #start就是开始线程
    except Exception,e:
        print e
        pass


##########################################################
url=""
def run1():
    try:
        Crun()
    except Exception,e:
        close()  #自动重启本程序
def Crun():  #启动
    try:
        global bool
        global url
        while True:
            if class_Queue.url_close>=5:  #10次没数据
                print "==============NULL==============%d"%(class_Queue.url_close)
            if class_Queue.url_int>=100000:  #防止读取的数据量过大
                time.sleep(1)
                close()  #自动重启本程序
            if class_Queue.url_close>=15:  #10次没数据
                time.sleep(1)
                close()  #自动重启本程序
                #return 1
                #atexit.register(close)#自动重启本程序

            if bool:  #self.bool=1  #控制采集
                tx_run(url) #线程系统

            time.sleep(120)
            print "==============120s==============%d"%(web_url.url_xl)
            if web_url.url_xl<1: #URL提取的数量
                time.sleep(1)
                close()  #自动重启本程序
            web_url.url_xl=0
            run1()
    except Exception,e:
        close()  #自动重启本程序
        #atexit.register(close)#自动重启本程序
        #return 1
        pass
##########################################################
def text_file(data):   #写回文件
    try:
        file_object = open('url.txt','w+')
        file_object.write(data) #成功
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        pass

def text_url():  #getURL(url)用来将HTML中的url放入urls列表中
    try:
        xxx = file('url.txt', 'r')  #读取要写入的文件
        dq_bool=1
        data=""
        data1=""
        for xxx_line in xxx.readlines():  #读取数据
            if dq_bool:
                dq_bool=0
                data1=xxx_line.strip()
            else:
                data+=str(xxx_line.strip())
                data+="\n"

        text_file(data)
        return data1.strip().lstrip().rstrip('\n')
    except Exception,e:
        pass

if __name__ == '__main__':
    print u"===========启动邮箱采集  神龙  QQ:29295842==========="

#http://www.383k.com/bbs/
#    url="http://bbs.t56.net/"
    data_url=text_url()
    if ~data_url.find("http://"):  #~取反
        url=data_url #url
        Crun()  #启动
    print u"URL地址数据异常"
    time.sleep(30)
    atexit.register(close)#自动重启本程序

