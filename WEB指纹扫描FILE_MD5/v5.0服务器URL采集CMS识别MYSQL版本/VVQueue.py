#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###################################################
import VVMysql
import VVUtil, VVList
import threading
import Queue
import time
import ConfigParser
import random

# 存储用的域名消息队列
StoreQueue = Queue.Queue(15000)
# 从数据库中读取域名消息队列
ReadQueue = Queue.Queue(15000)
# 需要cms识别的域名
#CmsQueue = Queue.Queue(15000)
www_Cms_Queue = Queue.Queue(15000)  #主域名
re_www_Cms_Queue = Queue.Queue(15000) #二级域名
# 识别超时的时间
Cms_timeoutout = 500
#设置采集域名类型
Domain_Type = "com"

www_CMS=0
www2_CMS=0



class VVQueue(threading.Thread):
    # 队列消息管理类
    def __init__(self, n=0):
        threading.Thread.__init__(self)
        self.db = VVMysql.VVMysql()
        # 尝试创建数据库，如果存在则会忽略
        self.db.mysql_create_database()
        self.db.mysql_open()
        self.index = n
        self.domain_list = None
        #self.curdomain = None
        self.debug_on = 1
        self.autoinc = 0
        #self.tablelist = VVList.VVList()

        self.readcfg()


    def readcfg(self):
        # 读取INI配置信息
        global Cms_timeout, Domain_Type
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            Cms_timeout = int(config.get("DATA", "cms_time"))  # CMS识别超时,秒
            Domain_Type = str(config.get("DATA", "mysql_bm"))  # 设置采集表
            self.domain_list = Domain_Type.split("|")
            self.debug_on = int(config.get("DEBUG", "showdetail"))
        except:
            Cms_timeout = 300
            self.domain_list = Domain_Type.split("|")

    def s_j_s(self,int1):  #抽取随机数
        try:
            return random.randint(0,int1)
        except:
            return 0

    def str_com_cn_lis(self): #获取随机值 表名
        global Domain_Type
        try:
            while 10:
                mysql_bm_data=self.domain_list[self.s_j_s(len(self.domain_list))]
                if self.db.mysql_select_B(mysql_bm_data):  #查询表明是否存在:#判断表是否有存在1有0无
                    Domain_Type=mysql_bm_data
                    break #跳出
            if Domain_Type=="":
                Domain_Type="com"
        except:
            Domain_Type="com"

    def randnum(self, maxnum):
        # 抽取随机数
        try:
            return random.randint(0, maxnum)
        except:
            pass
        return 0

#    def get_random_domain(self):   #这个是随机设置采集范围了   有明显问题
#        # 获取随机值 表名
#        try:
#            if self.tablelist.getitemcount() > 0:
#                self.curdomain = self.tablelist.getitem(self.autoinc % self.tablelist.getitemcount())
#                self.autoinc += 1
#        except Exception, e:
#            pass
#        if not self.curdomain:
#                self.curdomain = "com"

    def print_queue(self):
        global StoreQueue, ReadQueue, CmsQuwww_Cms_Queueeue, Cms_timeout,www_CMS,www2_CMS
        try:
            print "-----------------------------------------"
            print "------V:5.0---2014.8.8---Thread:%d--------"%(self.index)
            print "StoreQueue>>>>>>>>>%d"%(StoreQueue.qsize())
            print "ReadQueue<<<<<<<<<<%d"%(ReadQueue.qsize())
            print "www_Cms_Queue------%d"%(www_Cms_Queue.qsize())
            print "2_Cms_Queue------%d"%(re_www_Cms_Queue.qsize())
            print "CmsTimeout----%d"%(Cms_timeout)
            print "mysql link form     %s"%(Domain_Type)
            print "---------E-mail:29295842@qq.com----------"
            print "ok CMS    www_CMS:%d"%(www_CMS)
            print "ok CMS      2_CMS:%d"%(www2_CMS)
            print "-----------------------------------------"
        except:
            pass

    def run(self):
        tables = self.db.mysql_gettables()
        if tables:
            print "[Queue]: mysql form[%d]: %s" % (len(tables), ','.join(tables))
#            for item in tables:   不明白写这个有啥用啊
#                self.tablelist.add(item)
        while True:
            try:
                self.print_queue()   # 显示消息队列状态
                self.update_queue()  # 对数据进行存贮
                #self.print_queue()   # 显示消息队列状态
            except:
                pass
            # TODO 发布的时候时候一定要改为2秒
            time.sleep(2)

    def update_queue(self):  #
        global StoreQueue, ReadQueue, www_Cms_Queue
        try:
            if StoreQueue.qsize() > 0:  # 判断队列是否为空不为空  保存数据到数据库
                self.storespider()
                #print "111111111111"
            if ReadQueue.qsize()<=300: #读取 采集
                self.readspider()
                #print "222222222222"
            if www_Cms_Queue.qsize()<=1500: #读取 CMS识别
                self.readwww_Cms_Queue()
                #print "333333333333"
            if ReadQueue.empty():   # 如果读取的队列为空很可能断网了，此时应该休息5秒钟，免得数据库受不了
                self.add_BQueue()   # 添加数据到消息队列
                #print "444444444444"
                time.sleep(10)
        except:
            pass

    def add_BQueue(self):  #添加数据到消息队列
        try:
            #当网络掉线时  会把数据库吃光的
            #解决方法  当消息队列为B空时  自动向消息队列中插入一个URL    在清空整个表  等于从新采集
            #delete from data
            ReadQueue.put("www.microsoft.com",0.5)
            ReadQueue.put("www.baidu.com",0.5)
            ReadQueue.put("www.google.com",0.5)
            ReadQueue.put("www.YouTube.com",0.5)
            ReadQueue.put("www.Facebook.com",0.5)
            ReadQueue.put("www.yahoo.com",0.5)
            ReadQueue.put("www.hao123.com",0.5)
        except:
            return 0

    def execute_sql(self, data):
        try:
            self.db.mysql_commit()      # 保存数据
            return self.db.mysql_insert(data)  # 添加数据

        except Exception, e:
            return 0

    def mysql_czb(self, com):
        # 创建表
        try:
            sql = r"CREATE TABLE IF NOT EXISTS `%s` (" \
                  "`url` varchar(100) NOT NULL default ''," \
                  "`open_send` varchar(100) default NULL," \
                  "`cms_send` varchar(100) default NULL," \
                  "`time` varchar(100) default NULL," \
                  "PRIMARY KEY  (`url`)" \
                  ") ENGINE=InnoDB DEFAULT CHARSET=utf8;" % com
            self.db.mysql_insert(sql)  # 添加表数
            self.db.mysql_commit()  # 保存数据
        except Exception, e:
            pass

    def mysql_czb_2(self, com):
        # 创建表
        try:
            sql = r"CREATE TABLE IF NOT EXISTS `%s` ("\
                  "`url` varchar(100) NOT NULL default '',"\
                  "PRIMARY KEY  (`url`)"\
                  ") ENGINE=InnoDB DEFAULT CHARSET=utf8;" % com
            self.db.mysql_insert(sql)  # 添加表数
            self.db.mysql_commit()  # 保存数据
        except Exception, e:
            pass

    def storespider(self):
        # 储存域名
        global StoreQueue, ReadQueue, www_Cms_Queue, Cms_timeout
        try:
            int_insert = StoreQueue.qsize()  # 返回大小
            if int_insert <= 0:
                return
            for n in xrange(int_insert):
                self.tmphost = StoreQueue.get(0.2)   # 获取消息队列
                if not self.tmphost:
                    continue
                #print self.tmphost
                if VVUtil.is_subdomain(self.tmphost):  #判断域名是否是二级域名 1是0否
#                    a1=VVUtil.trim_sdomain(self.tmphost)  #解析主域名
#                    StoreQueue.put(a1, 0.1)  #URL提取URL  在添加到数组
                    #二级域名
                    tmpcom = VVUtil.get_domain_suffix(self.tmphost)  # 解析域名后辍名
                    tmpcom = tmpcom.replace(".", "_")  # 数据表名不支持. 替换下
                    if not self.db.mysql_table_exist("2_"+tmpcom):
                        # 查询表明是否存在:#判断表是否有存在1有0无
                        self.mysql_czb_2("2_"+tmpcom)  # 创建表
                    sql_data = "insert into %s(url) VALUES('%s') ;" %\
                               ("2_"+tmpcom, self.tmphost)
                    if re_www_Cms_Queue.qsize()<=3000: #读取 CMS识别
                        if self.execute_sql(sql_data): #查看SQL语句是否执行成功
                            re_www_Cms_Queue.put(self.tmphost, 0.1)
#                        print "add ok ",self.tmphost
#                    else:
#                        print "add no ",self.tmphost

                else:
                    #主域名
                    tmpcom = VVUtil.get_domain_suffix(self.tmphost)  # 解析域名后辍名
                    tmpcom = tmpcom.replace(".", "_")  # 数据表名不支持. 替换下
                    if not self.db.mysql_table_exist(tmpcom):
                        # 查询表明是否存在:#判断表是否有存在1有0无
                        self.mysql_czb(tmpcom)  # 创建表
                    #self.tablelist.add(tmpcom)
                    sql_data = "insert into %s(url,time) VALUES('%s','%s') ;" % \
                               (tmpcom, self.tmphost, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                    self.execute_sql(sql_data)
                    #存在一个问题当表添加完后再保存数据  数据无法保存上
        except:
            pass

    def readspider(self):
        # 从数据库 读取URL
        global StoreQueue, ReadQueue, www_Cms_Queue, Cms_timeout
        try:
            self.str_com_cn_lis() #获取随机值 表名
            # 一次读取100个，别读取太多，假如程序重启的话，会有许多标记为已经爬取，但是实际上没有爬取
            sql_data = "select * from %s where open_send is null order by rand() limit 0,300;" % Domain_Type
            #print sql_data
            #查询open_send字段为空随机抽取500条
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                url = row[0]
                sql_data = "update %s set open_send='send' where url='%s'" % (Domain_Type, url)
                self.execute_sql(sql_data)
                ReadQueue.put(url, 0.1)
        except:
            pass

    def readwww_Cms_Queue(self):

        # 从数据库读取需要CMS识别的URL
        global StoreQueue, ReadQueue, www_Cms_Queue, Cms_timeout
        try:
            self.str_com_cn_lis() #获取随机值 表名
            #查询open_send字段为空随机抽取100条
            sql_data = "select * from %s where cms_send is null order by rand() limit 0,300;" % Domain_Type
            #print sql_data
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                # print '%s-%s-%s'%(row[0],row[1],row[2])
                url = row[0]
                sql_data = "update %s set cms_send='send' where url='%s'" % (Domain_Type, url)
                self.execute_sql(sql_data)
                www_Cms_Queue.put(url, 0.5)
        except:
            pass



################################################
if __name__ == '__main__':
    threads = []
    threadcount = 1
    for i in xrange(threadcount):
        threads.append(VVQueue(i))
    for t in threads:
        t.start()
        t.join()

