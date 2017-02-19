#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
###################################################
import os
import sys
print sys.path
skyeyepath = os.path.realpath((os.path.dirname(__file__)) + "/../")  #将当前的路径加入path
if not skyeyepath in sys.path:
    sys.path.append(skyeyepath)

from util import VVQueue
from spider import VVSpider
from cms import VVCms
from util.VVUtil import cfgpath

import time
import ConfigParser  #INI读取数据


INT_TX_Queue = 1  # 消息队列维护线程
INT_TX_cms = 5    # cms识别线程 建议一个CPU 10个线程 n*10
INT_TX_spider = 2  # 设置采集线程

if __name__ == '__main__':
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open(cfgpath))
        INT_TX_Queue = int(config.get("DATA", "TX_Queue"))  # 消息队列维护线程
        INT_TX_cms = int(config.get("DATA", "TX_cms"))      # cms识别o线程
        INT_TX_spider = int(config.get("DATA", "TX_openrul"))  # 设置采集线程
    except:
        pass

    # 启动数据库,只能用一个实例，不然数据库压力他打
    dbinstance = VVQueue.VVQueue(0)
    dbinstance.start()

    # 启动爬虫
    spiderthreads = []  #线程  数据采集
    for i in xrange(INT_TX_spider):
        t = VVSpider.VVSpider(i)
        spiderthreads.append(t)
        time.sleep(0.01)
        t.start()

    # 线程cms识别
    cmsthreads = []  # 线程cms识别
    for i in xrange(INT_TX_cms):  # nthreads=10  创建10个线程
        t = VVCms.VVCms(i)
        cmsthreads.append(t)
        time.sleep(0.01)
        t.start()


    # 等待
    # 给一个初始的域名
    VVQueue.ReadQueue.put('www.sina.com.cn')
    VVQueue.ReadQueue.put('www.163.com')
    VVQueue.CmsQueue.put('zysd.com.cn')
    VVQueue.CmsQueue.put('www.baidu.com')
    VVQueue.CmsQueue.put('domeng.cn')
    VVQueue.CmsQueue.put('soxan.cn')
    VVQueue.CmsQueue.put('chinahanhai.net')
    #dbinstance.join()
    while True:
        time.sleep(0.5)



