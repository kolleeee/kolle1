#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
###################################################
import time
import class_Queue  #消息队列维护
import C_openrul  #采集URL
import Class_url_cms #cms识别
import ConfigParser  #INI读取数据
import Cclose_open  #结束进程  在从新开启进程

INT_TX_Queue=1 #消息队列维护线程
INT_TX_cms=100 #cms识别线程
INT_TX_openrul=2 #设置采集线程
if __name__=='__main__':
    #global INT_TX_Queue
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open("Server.ini"))
        INT_TX_Queue = int(config.get("DATA","TX_Queue"))  #消息队列维护线程
        INT_TX_cms = int(config.get("DATA","TX_cms"))  #cms识别线程
        INT_TX_openrul = int(config.get("DATA","TX_openrul"))  #设置采集线程
    except:
        pass

    #结束进程在从新开启进程  解决MYSQL连接错误
    Cclose_open_threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        Cclose_open_threads.append(Cclose_open.CS_close_open())
    for thread in Cclose_open_threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程

    threads0 = []  #线程   消息队列维护
    for i in range(INT_TX_Queue):
        threads0.append(class_Queue.Csqlite_Queue(i))
    for t in threads0:
        time.sleep(1)
        t.start()

    threads1 = []  #线程  数据采集
    for i in range(INT_TX_openrul):
        threads1.append(C_openrul.CS_openurl(i))
    for t in threads1:
        time.sleep(1)
        t.start()

    #线程cms识别
    threads2 = []  #线程cms识别
    for i in range(INT_TX_cms):  #nthreads=10  创建10个线程
        threads2.append(Class_url_cms.Class_url_cms(i))
    for tA in threads2:
        time.sleep(1)
        tA.start()  #start就是开始线程

    #class_Queue.Aopenurl.put("www.baidu.com",0.1)
    #class_Queue.Aopenurl.put("www.120.com",0.1)