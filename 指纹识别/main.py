#!/usr/local/bin/python
#-*- coding:UTF-8 -*-

import os
import re
import sys
import socket
import httplib
import gzip,StringIO
import Queue,threading
import time

import class_Queue  #线程处理
import class_openurl #采集URL
import Class_url_BZ #CScms
################################################
if __name__=='__main__':
    print u"爬虫指+纹识别0.1公布版本"
    print u"指纹识别库使用的御剑库"
    print u"BY:落雪 QQ:2602159946"
    print u"结果保存在目录下  CMS版本.txt"
    print u"time:2013/7/24"
    #消息处理
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(class_Queue.C_Queue(class_Queue.Aopenurl,class_Queue.Bopenurl,class_Queue.Copenurl,class_Queue.Dopenurl))
    for t in threads:
        t.start()

    #采集URL
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(class_openurl.CS_openurl(i,class_Queue.Aopenurl,class_Queue.Bopenurl,class_Queue.Copenurl))
    for t in threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(2)
        t.start()  #start就是开始线程

    #测试CScms
    threads = []  #线程
    for i in range(100):  #nthreads=10  创建10个线程
        threads.append(Class_url_BZ.Class_url_BZ(class_Queue.Copenurl,class_Queue.Dopenurl))
    for tA in threads:   #不理解这是什么意思    是结束线程吗
        time.sleep(2)
        tA.start()  #start就是开始线程