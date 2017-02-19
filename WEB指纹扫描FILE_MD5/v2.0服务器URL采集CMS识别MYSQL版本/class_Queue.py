#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
###################################################
import threading
import Queue
import time
import Cmysql #数据库操作文件
import xx_com_cn_xx #对域名拆分

Aopenurl = Queue.Queue(15000)  #存贮
Bopenurl = Queue.Queue(15000)  #读取
CMS_URL= Queue.Queue(15000)  #需要识别的CMS
cms_time=500 #超时/s   CMS识别超时
mysql_bm="com" #设置采集表
import ConfigParser #INI读取数据
import random

class Csqlite_Queue(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.sql=Cmysql.mysql_handle()
        self.sql.mysql_open()
        self.TX_I=i
        self.com_cn_lis=[]  #分成数组
        self.Server_ini()  #读取INI配置信息

    def Server_ini(self):  #读取INI配置信息
        global cms_time,mysql_bm
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            cms_time= int(config.get("DATA","cms_time")) #超时/s   CMS识别超时
            mysql_bm=str(config.get("DATA","mysql_bm")) #设置采集表
            self.com_cn_lis=mysql_bm.split("|")
        except:
            cms_time=300
            self.com_cn_lis=mysql_bm.split("|")
            pass

    def s_j_s(self,int1):  #抽取随机数
        try:
            return random.randint(0,int1)
        except:
            return 0

    def str_com_cn_lis(self): #获取随机值 表名
        global mysql_bm
        try:
            while 10:
                mysql_bm_data=self.com_cn_lis[self.s_j_s(len(self.com_cn_lis))]
                if self.sql.mysql_select_B(mysql_bm_data):  #查询表明是否存在:#判断表是否有存在1有0无
                    mysql_bm=mysql_bm_data
                    break #跳出
            if mysql_bm=="":
                mysql_bm="com"
        except:
            mysql_bm="com"

    def print_Queue(self):
        global Aopenurl,Bopenurl,CMS_URL,cms_time
        try:
            print "--------V:2.0------Thread:%d-------------"%(self.TX_I)
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

            time.sleep(20)
            self.run_run()
        except:
            print "=================CMYsql_Queue---run  try  except================="
            time.sleep(20)
            self.run_run()

    def open_sqlite(self):  #
        global Aopenurl,Bopenurl,CMS_URL
        try:
            #if Aopenurl.qsize()>=100: #存贮
            if not Aopenurl.empty():   #判断队列是否为空不为空  保存数据到数据库
                self.Aurl()
            if Bopenurl.qsize()<=300: #读取 采集
                self.Burl()
            if CMS_URL.qsize()<=500: #读取 CMS识别
                self.CMS_URL()
            if Bopenurl.empty():   #如果B为空很可能断网了
                self.add_BQueue()  #添加数据到消息队列
            time.sleep(5)
        except:
            return 0

    def add_MYsql(self,data):
        try:
            self.sql.mysql_insert(data)  #添加数据
            self.sql.mysql_S()  #保存数据
        except:
            return 0

    def CMS_URL(self):  #从数据库读取需要CMS识别的URL
        try:
            self.str_com_cn_lis() #获取随机值 表名
            sql_data="select * from %s where cms_send is null order by rand() limit 500"%(mysql_bm)
            #查询open_send字段为空随机抽取500条
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql_data)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                #print '%s-%s-%s'%(row[0],row[1],row[2])
                url=row[0]
                sql_data="update %s set cms_send='send' where url='%s'"%(mysql_bm,url)
                self.add_MYsql(sql_data)
                CMS_URL.put(url,0.1)
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
        except:
            return 0

    def mysql_czb(self,com):  #创建表
        try:
            EXISTS="DROP TABLE IF EXISTS `%s`;"\
                   "CREATE TABLE `%s` ("\
                   "`url` varchar(100) NOT NULL default '',"\
                   "`open_send` varchar(100) default NULL,"\
                   "`cms_send` varchar(100) default NULL,"\
                   "`time` varchar(100) default NULL,"\
                   "PRIMARY KEY  (`url`)"\
                   ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"\
                   ""%(com,com)
            self.sql.mysql_insert(EXISTS)  #添加表数
            self.sql.mysql_S()  #保存数据
            print "MYSQL FORM %s OK"%(com)
        except:
            pass

    def Aurl(self):  #储存域名
        global SQL_WWW
        try:
            int_insert=Aopenurl.qsize()  #返回大小
            for i in range(int_insert):
                self.host_www=Aopenurl.get(0.2)  #获取消息队列
                if xx_com_cn_xx.xxx_www(self.host_www):  #判断域名是否是二级域名 1是0否
                    CMS_URL.put(self.host_www,0.1)
                else:
##                self.host_www=Aopenurl.get(0.2)  #获取消息队列
                    self.com=xx_com_cn_xx.www_com(self.host_www)  #解析域名后辍名
                    self.com=self.com.replace(".", "_")  #数据表名不支持. 替换下
                    #print self.host_www,"--------",self.com
                    #sql="SHOW TABLES LIKE '%%%s%%'"%(self.com)
                    if not self.sql.mysql_select_B(self.com):  #查询表明是否存在:#判断表是否有存在1有0无
                        self.mysql_czb(self.com)  #创建表
                        sql_data="insert into %s(url,time) VALUES('%s','%s')"%(self.com,self.host_www,time.strftime('%Y-%m-%d',time.localtime(time.time())))
                        self.add_MYsql(sql_data)
                        #存在一个问题当表添加完后再保存数据  数据无法保存上
                    else:
                        sql_data="insert into %s(url,time) VALUES('%s','%s')"%(self.com,self.host_www,time.strftime('%Y-%m-%d',time.localtime(time.time())))
                        self.add_MYsql(sql_data)
        except:
            return 0

    def Burl(self):  #从数据库 读取URL
        try:
            self.str_com_cn_lis() #获取随机值 表名
            sql_data="select * from %s where open_send is null order by rand() limit 500"%(mysql_bm)
            #查询open_send字段为空随机抽取500条
            self.cursor=self.sql.conn.cursor()
            n = self.cursor.execute(sql_data)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                #print '%s-%s-%s'%(row[0],row[1],row[2])
                url=row[0]
                sql_data="update %s set open_send='send' where url='%s'"%(mysql_bm,url)
                self.add_MYsql(sql_data)
                Bopenurl.put(url,0.1)
                if CMS_URL.qsize()<=2000: #读取 CMS识别
                    #要判断下这个是否CMS识别过 以免重复识别
                    if not row[2]=="send":
                        sql_data="update %s set cms_send='send' where url='%s'"%(mysql_bm,url)
                        self.add_MYsql(sql_data)
                        CMS_URL.put(url,0.1)
        except:
            return 0

################################################
if __name__=='__main__':
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(Csqlite_Queue(i))
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程

