#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#线程操作消息队列
#select * from ip order by RANDOM() limit 10   随机抽取
import threading
import Queue
import time

cms_url = Queue.Queue() #需要CMS识别
S_suliang=0  #扫描完成的数量
Z_suliang=0  #总数量
cms_time=500  #扫描超时时间
OK_CMS=0  #已经识别出来的RUL个数
class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def b_d_i(self,i1,i2):  #print b_d_i(10,100)
        try:
            rate=float(i1)/float(i2)
            return int(rate*100)
        except:
            return 0

    def print_Queue(self):
        try:
            print "\n-----------------------------------------"
            print "cms_url--------%s"%(cms_url.qsize())
            print "Z:%d S:%d OK_CMS:%d"%(Z_suliang,S_suliang,OK_CMS)
            print "-------------------%d%%-------------------"%(self.b_d_i(S_suliang,Z_suliang))
            print "-----------------------------------------"
        except:
            return 0

    def run_run(self):
        try:
            self.run()
        except:
            time.sleep(3)
            self.run()

    def run(self):
        try:
            while True:
                self.print_Queue()  #线束数据量
                time.sleep(10)
        except:
            time.sleep(10)
            self.run_run()

