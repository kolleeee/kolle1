#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
###################################################
import threading
import Queue
import time
import Csqlite3

Aopenurl = Queue.Queue(15000)  #存贮
Bopenurl = Queue.Queue(15000)  #读取
CMS_URL= Queue.Queue(15000)  #需要识别的CMS
cms_time=500 #超时/s   CMS识别超时
import ConfigParser  #INI读取数据

class Csqlite_Queue(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()
        self.Server_ini()  #读取INI配置信息

    def Server_ini(self):  #读取INI配置信息
        global cms_time
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            cms_time= int(config.get("DATA","cms_time"))
        except:
            cms_time=300
            pass

    def print_Queue(self):
        global Aopenurl,Bopenurl,CMS_URL,cms_time
        try:
            print "-----------------------------------------"
            print "   http://hi.baidu.com/alalmn           "
            print "Aopenurl>>>>>>>>>%s"%(Aopenurl.qsize())
            print "Bopenurl<<<<<<<<<%s"%(Bopenurl.qsize())
            print "CMS_URL----%s----cms_time----%d"%(CMS_URL.qsize(),cms_time)
            print "-----------------------------------------"
        except:
            return 0

    def run_run(self):
        try:
            self.run()
        except:
            time.sleep(2)
            self.run()

    def run(self):
        try:
            while True:
                self.print_Queue()  #显示消息队列状态
                self.open_sqlite()  #对数据进行存贮
        except:
            print u"=================Csqlite_Queue---run异常！！！！！================="
            time.sleep(20)
            self.run_run()

    def open_sqlite(self):  #
        global Aopenurl,Bopenurl,CMS_URL
        try:
            #if Aopenurl.qsize()>=100: #存贮
            if not Aopenurl.empty():   #判断队列是否为空不为空  保存数据到数据库
                self.Aurl()
            if Bopenurl.qsize()<=500: #读取 采集
                self.Burl()
            if CMS_URL.qsize()<=500: #读取 CMS识别
                self.CMS_URL()
            if Bopenurl.empty():   #如果B为空很可能断网了
                self.add_BQueue()  #添加数据到消息队列
            self.delete_SQL()  #删除数据
            time.sleep(5)
        except:
            return 0

    def CMS_URL(self):  #从数据库读取需要CMS识别的URL
        try:
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            sql_data="select * from www where cms_send is null order by RANDOM() limit 800"
            #查询字段open_send为空   随机取200行
            cur.execute(sql_data)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                data=line[0]
                sql_data="update www set cms_send='send' where url='%s'"%(data)
                self.add_sqlite(sql_data)
                CMS_URL.put(data,0.1)
        except:
            pass

    def add_BQueue(self):  #添加数据到消息队列
        try:
            #当网络掉线时  会把数据库吃光的
            #解决方法  当消息队列为B空时  自动向消息队列中插入一个URL    在清空整个表  等于从新采集
            #delete from data
            Bopenurl.put("www.microsoft.com",0.5)
            Bopenurl.put("www.baidu.com",0.5)
            Bopenurl.put("www.google.com",0.5)
            Bopenurl.put("www.YouTube.com",0.5)
            Bopenurl.put("www.Facebook.com",0.5)
            Bopenurl.put("www.yahoo.com",0.5)
            Bopenurl.put("www.hao123.com",0.5)
            sql_data="delete from www"
            self.add_sqlite(sql_data)
        except:
            return 0

    def add_sqlite(self,data):
        try:
            return self.sql3.mysqlite3_insert(data) #添加数据
        except:
            return 0

    def Aurl(self):  #存贮URL地址
        try:
            int_insert=Aopenurl.qsize()  #返回大小
            for i in range(int_insert):
                data=Aopenurl.get(0.2)  #获取消息队列
                sql_data="insert into www(url,time) VALUES('%s','%s')"%(data,time.strftime('%Y.%m.%d-%H.%M.%S'))
                self.add_sqlite(sql_data)
        except:
            return 0

    def Burl(self):  #从数据库 读取URL
        try:
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            sql_data="select * from www where open_send is null order by RANDOM() limit 800"
            #查询字段open_send为空   随机取200行
            cur.execute(sql_data)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                data=line[0]
                sql_data="update www set open_send='send' where url='%s'"%(data)
                self.add_sqlite(sql_data)
                Bopenurl.put(data,0.1)
                if CMS_URL.qsize()<=2000: #读取 CMS识别
                    #要判断下这个是否CMS识别过 以免重复识别
                    if not line[2]=="send":
                        sql_data="update www set cms_send='send' where url='%s'"%(data)
                        self.add_sqlite(sql_data)
                        CMS_URL.put(data,0.1)
        except:
            return 0

    def SQL_slect(self,sql):  #获取数量
        try:
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            cur.close()  #关闭游标
            #print len(res)
            return len(res)
        except:
            return 0

    def delete_SQL(self):  #删除数据
        try:
            #清除已经识别过的CMS
            int_url=self.SQL_slect("select * from www where cms_send='send'")  #获取数量
            if int_url>=2000:
                delete="delete from www where cms_send='send'"
                self.add_sqlite(delete)
            ##############
            #清除采集
            int_url=self.SQL_slect("select * from www where open_send='send'")  #获取数量
            if int_url>=4000:
                delete="delete from www where open_send='send'"
                self.add_sqlite(delete)
            ##############
            int_url=self.SQL_slect("select * from www")  #获取数量
            if int_url>=50000:
                int_delete=int_url/4
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                sql="select * from www order by RANDOM() limit %d"%(int_delete-1) #随机抽取
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    delete="delete from www where url='%s'"%(line[0])
                    self.add_sqlite(delete)
        except:
            return 0

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Csqlite_Queue())
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程

