#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

import threading
import Queue
import time
import Csqlite3
#url  关键字
#cj  采集
#openurl  URL地址
url_root1 = Queue.Queue()  #要读取的URL
url_root2 = Queue.Queue()  #要储存的URL
#url_close = Queue.Queue() #数据库被清空
url_close = 0   #数据库被清空  多次没读取到数据
url_int= 0  #防止读取的数据量过大

class C_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.del_openurl()   #清空表

    def del_openurl(self):   #清空表
        try:
            update = "delete from openurl"
            self.sql3.mysqlite3_delete(update)
            print u"已经清空 openurl 表"
        except:
            pass

    def print_Queue(self):
        try:
            print u"\n-----------------------------------------"
            print u"要读取的URL--------%s个"%(url_root1.qsize())
            print u"要储存的URL--------%s个"%(url_root2.qsize())
            print u"-----------------------------------------"
        except:
            pass

    def run1(self):
        try:
            self.run()
        except Exception,e:
            self.run()
            pass
    def run(self):
        try:
            global url_int  #防止读取的数据量过大
            while True:
                self.print_Queue()
                self.url_url_root2()  #要储存的URL
                #self.url_url_root1()  #要读取的URL
                self.SQL_select_NULL()  #查看数据库剩余要采集的
                if url_root1.qsize()<=50:  #要采集的URL
                    self.SQL_Aopenurl("select * from openurl where cj is NULL limit 300")  #
                    url_int+= 300  #防止读取的数据量过大
                time.sleep(5)
                self.run1()
        except Exception,e:
            print "C_Queue---",e
            time.sleep(5)
            self.run1()

    def SQL_select_NULL(self):  #查看数据库剩余要采集的
        try:
            global url_close
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute("select * from openurl where cj is NULL")# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            if len(res)<=5:
                url_close+=url_close
                #url_close.put(self.close,0.5)   #插入队列
        except Exception,e:
            pass

    def url_url_root2(self):  #要储存的URL
        try:
            global url_root2
            if url_root2.empty():   #判断队列是否为空
                time.sleep(10)
                return 0
            int_exp=int(url_root2.qsize())
            for i in range(int(int_exp)):
                self.Chost = url_root2.get(0.1)  #get()方法从队头删除并返回一个项目
                #print "采集到的URL:",self.Chost
                #储存url   cj    openurl
                insert="insert into openurl(url) VALUES('%s')"%(self.Chost)
                #print insert
                self.sql3.mysqlite3_insert(insert) #添加数据
                #time.sleep(0.01)
        except Exception,e:
            print "---url_url_root2---",e
            return 0

    def SQL_Aopenurl(self,sql):  #从数据库 提取100条网址 供采集使用
        try:
            global url_root1
#            #应该先检查  消息队列  数据是巨量是否小于100
#            if url_root1.qsize()<50: # 返回队列的大小
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                #print line[0]
                url_root1.put(line[0],0.2)   #插入队列
                update = "update openurl set cj='send' where url='%s'"%(line[0])
                self.sql3.mysqlite3_update(update)
            cur.close()  #关闭游标
            return 1
        except:
            time.sleep(2)
            return 0



