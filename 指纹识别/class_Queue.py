#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#神龙 QQ29295842
#blog http://hi.baidu.com/alalmn
#线程操作消息队列
#select * from ip order by RANDOM() limit 10   随机抽取
import threading
import Queue
import time
import Csqlite3
import urllib2

Aopenurl = Queue.Queue(5000) #要采集的URL    #当有多个线程共享一个东西的时候就可以用它了
Bopenurl = Queue.Queue(5000) #http200 存到数据库库
Copenurl = Queue.Queue(5000) #从数据库中读取 http200 成功的过滤下防止重复
Dopenurl = Queue.Queue(5000)  #保存扫描到的结果["URL","版本"]

class C_Queue(threading.Thread):
    def __init__(self,Aopenurl,Bopenurl,Copenurl,Dopenurl):
        threading.Thread.__init__(self)
        self.Aopenurl=Aopenurl
        self.Bopenurl=Bopenurl
        self.Copenurl=Copenurl
        self.Dopenurl=Dopenurl
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    def print_Queue(self):
        try:
            print "-----------%s-----------"%(time.strftime('%Y.%m.%d-%H.%M.%S'))
            print u"Aopenurl----要采集的URL-----5000---------%s"%(self.Aopenurl.qsize())
            print u"Bopenurl----中文站----------5000---------%s"%(self.Bopenurl.qsize())
            print u"Copenurl----等待测试CMS-----5000---------%s"%(self.Copenurl.qsize())
            print u"Dopenurl----结果------------5000---------%s"%(self.Dopenurl.qsize())
            print "-----------------------------------------"
        except:
            return 0

    def run(self):
        try:
            #print "Thread:%d--C_Queue-run"
            while True:
                self.print_Queue()  #线束数据量
                if self.Dopenurl.qsize()>=5:  #对结果进行存储
                    self.SQL_Dopenurl()  #
                if self.Aopenurl.qsize()<=50:  #要采集的URL
                    self.SQL_Aopenurl("select * from openurl where openurl is NULL limit 50")  #从数据库 提取100条网址 供采集使用
                if self.Bopenurl.qsize()>=100:  #http200 存到数据库库
                    self.SQL_Bopenurl()  #对Bopinurl进行存储
                if self.Copenurl.qsize()<=300:  #从数据库中读取 http200 成功的过滤下防止重复
                    self.SQL_Copenurl("select * from openurl where CScms is NULL limit 500")  #
                self.sql_del() #清除数据过多
                time.sleep(10)
        except:
            #print "Thread:%d--C_Queue-run-try--except!!!!!"
            time.sleep(10)
            self.run()

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
            time.sleep(4)
            return 0

    def sql_del(self):
        try:
            int_url=self.SQL_slect("select * from openurl")  #获取数量
            if int_url>=50000:
                int_delete=int_url/5
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                sql="select * from openurl" #随机抽取
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                a=0
                for line in res:
                    a+=1
                    if a>=int_delete:
                        break #跳出
                    delete="delete from openurl where url='%s'"%(line[0])
                    self.sql3.mysqlite3_delete(delete)
        except:
            time.sleep(2)
            return 0

    def TXT_file123(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem+".txt",'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            print "111111",e
            return 0

    def SQL_Dopenurl(self):  #
        try:
            int_insert=self.Dopenurl.qsize()
            E = 0 #得到list的第一个元素
            while E < int_insert-1:
                time.sleep(1)
                data=self.Dopenurl.get(0.2)  #获取消息队列
                URL="http://webxscan.com/cms.php?url=%s&cms=%s"%(data[0],data[1])
                self.url_post(URL)   #后门
                self.TXT_file123(data[1],data[0])  #写入文本
                time.sleep(1)
                E = E + 1
        except:
            time.sleep(2)
            return 0

    def url_post(self,URL):
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #urllib2.urlopen(URL,timeout=20)  # 后门POST提交   超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            #time.sleep(1)
        except:
            #print "Thread:%d--C_ftppassword--http-POST-Failure"%(self.Ht)
            return 0

    def SQL_Copenurl(self,sql):  #
        try:
            self.sql3.conn.commit()# 获取到游标对象
            cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
            cur.execute(sql)# 获取所有结果
            res = cur.fetchall()  #从结果中取出所有记录
            for line in res:
                #print line[0]
                self.Copenurl.put(line[0],0.5)   #插入队列
                update = "update openurl set CScms='send' where url='%s'"%(line[0])
                self.sql3.mysqlite3_update(update)
            cur.close()  #关闭游标
            return 1
        except:
            time.sleep(2)
            return 0

    def SQL_Bopenurl(self):  #对Bopinurl进行存储
        try:
            int_insert=self.Bopenurl.qsize()
            if int_insert>=100: #返回队列的大小
                E = 0 #得到list的第一个元素
                while E < int_insert-1:
                    #print self.list_2[E]
                    data=self.Bopenurl.get(0.2)  #获取消息队列
                    insert="insert into openurl(url,time) VALUES('%s','%s')"%(data,time.strftime('%Y.%m.%d-%H.%M.%S'))
                    #print insert
                    self.sql3.mysqlite3_insert(insert) #添加数据
                    E = E + 1
        except:
            time.sleep(2)
            return 0

    def SQL_Aopenurl(self,sql):  #从数据库 提取100条网址 供采集使用
        try:
            #应该先检查  消息队列  数据是巨量是否小于100
            if self.Aopenurl.qsize()<50: # 返回队列的大小
                self.sql3.conn.commit()# 获取到游标对象
                cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
                cur.execute(sql)# 获取所有结果
                res = cur.fetchall()  #从结果中取出所有记录
                for line in res:
                    #print line[0]
                    self.Aopenurl.put(line[0],0.5)   #插入队列
                    update = "update openurl set openurl='send' where url='%s'"%(line[0])
                    self.sql3.mysqlite3_update(update)
                cur.close()  #关闭游标
            return 1
        except:
            time.sleep(2)
            return 0

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(C_Queue(Aopenurl,Bopenurl,Copenurl,Dopenurl))
    for t in threads:
        t.start()