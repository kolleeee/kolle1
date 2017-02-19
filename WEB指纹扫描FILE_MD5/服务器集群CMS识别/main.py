#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
################################################
import class_Queue  #消息队列维护
import C_openrul  #URL采集
import time
import Class_url_cms
import Cclose_open  #结束进程  在从新开启进程

if __name__=='__main__':
    #结束进程在从新开启进程  解决MYSQL连接错误
    Cclose_open_threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        Cclose_open_threads.append(Cclose_open.CS_close_open())
    for thread in Cclose_open_threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程

    threads0 = []  #线程   消息队列维护
    for i in range(1):
        threads0.append(class_Queue.Csqlite_Queue())
    for t in threads0:
        t.start()

    threads1 = []  #线程  数据采集
    for i in range(1):
        threads1.append(C_openrul.CS_openurl(i))
    for t in threads1:
        t.start()

    #线程cms识别
    threads2 = []  #线程cms识别
    for i in range(100):  #nthreads=10  创建10个线程
        threads2.append(Class_url_cms.Class_url_cms(i))
    for tA in threads2:
        time.sleep(2)
        tA.start()  #start就是开始线程



