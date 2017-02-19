#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
import Class_url_cms #cms识别
import class_Queue #消息队列维护
import time
import sys
import list
#

def add_Queue(TXT_file):  #添加到消息队列
    LS = list.Clist()  #初始化类
    LS.list_del()  #清空list列表
    xxx = file(TXT_file, 'r')
    for xxx_line in xxx.readlines():  #读取数据
        LS.liet_add(xxx_line.strip())  #添加数据
    LS.liet_lsqc() #数组列表去重复
    print "list:%d list:%d"%(len(LS.list),len(LS.list_2))
    for url in LS.list_2:  #读取数据
        class_Queue.cms_url.put(url,1)
    class_Queue.Z_suliang=class_Queue.cms_url.qsize()  #总数量

if "__main__" == __name__:
    print "------------------------------------------------"
    print "                URL  CMS(KEY--MD5)              "
    print "                main.exe url.txt                "
    print "             http://www.hacked90.com/           "
    print "         BY:http://hi.baidu.com/alalmn/         "
    print "               BY:QQ:29295842                   "
    print "----------------time:---2014.2.25---------------"
    print "------------------------------------------------"

    #TXT_file ="123456789.txt"
    if len(sys.argv) < 2:
        print "main.exe [feil URL]                "
        print "cmd                "
        print "main.exe url.txt                "
        time.sleep(300)
    add_Queue(sys.argv[1])  #添加到消息队列
    #消息队列
    class_Queue_threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        class_Queue_threads.append(class_Queue.C_Queue())
    for t0 in class_Queue_threads:   #不理解这是什么意思    是结束线程吗
        t0.start()  #start就是开始线程
    time.sleep(2)  #把数据都读取出来

    #线程cms识别
    threads = []  #线程cms识别
    for i in range(100):  #nthreads=10  创建10个线程
        threads.append(Class_url_cms.Class_url_cms(i))
    for tA in threads:
        time.sleep(2)
        tA.start()  #start就是开始线程
