#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import web_url
from class_Queue import C_Queue  #消息队列

import class_Queue  #消息队列
url_root1 = class_Queue.url_root1  #要采集的URL
if __name__ == '__main__':

    threads = []  #线程
    for i in range(1):
        threads.append(C_Queue())
    for t in threads:
        t.start()

    url="http://www.92sk.com" #url
    url_root1.put(url,0.5)   #插入队列
    th=5 #线程
    max=5 #深度
    threads = []  #线程
    for i in range(10):  #nthreads=10  创建10个线程
        threads.append(web_url.web_url(url,th,max))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程