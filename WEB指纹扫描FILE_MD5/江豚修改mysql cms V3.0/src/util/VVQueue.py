#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###################################################
# 将当前目录加入系统环境
import os
import sys
skyeyepath = os.path.realpath((os.path.dirname(__file__)) + "/../")
if not skyeyepath in sys.path:
    sys.path.append(skyeyepath)
#print sys.path
# 优先导入自己的包，然后再导入系统包
from database import VVMysql
from util import VVUtil, VVList
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
CmsQueue = Queue.Queue(15000)
# 识别超时的时间
Cms_timeoutout = 500
#设置采集域名类型
Domain_Type = "com"



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
        self.curdomain = None
        self.debug_on = 1
        self.autoinc = 0
        self.tablelist = VVList.VVList()
        self.readcfg()

    def readcfg(self):
        # 读取INI配置信息
        global Cms_timeout, Domain_Type
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            Cms_timeout = int(config.get("DATA", "Cms_timeout"))  # CMS识别超时,秒
            Domain_Type = str(config.get("DATA", "Domain_Type"))  # 设置采集表
            self.domain_list = Domain_Type.split("|")
            self.debug_on = int(config.get("DEBUG", "showdetail"))
        except:
            Cms_timeout = 300
            self.domain_list = Domain_Type.split("|")

    def randnum(self, maxnum):
        # 抽取随机数
        try:
            return random.randint(0, maxnum)
        except:
            pass
        return 0

    def get_random_domain(self):
        # 获取随机值 表名
        try:
            if self.tablelist.getitemcount() > 0:
                self.curdomain = self.tablelist.getitem(self.autoinc % self.tablelist.getitemcount())
                self.autoinc += 1
        except Exception, e:
            pass
        if not self.curdomain:
                self.curdomain = "com"

    def print_queue(self):
        global StoreQueue, ReadQueue, CmsQueue, Cms_timeout
        try:
            print "!!!![Queue][%d] StoreQueue:[%d], ReadQueue:[%d],CmsQueue:[%d],CmsTimeout:[%d]!!!!" % \
                  (self.index, StoreQueue.qsize(), ReadQueue.qsize(), CmsQueue.qsize(), Cms_timeout)
        except:
            pass

    def run(self):
        tables = self.db.mysql_gettables()
        if tables:
            print "[Queue]: Found tables[%d]: %s" % (len(tables), ','.join(tables))
            for item in tables:
                self.tablelist.add(item)
        while True:
            try:
                self.print_queue()   # 显示消息队列状态
                self.update_queue()  # 对数据进行存贮
                self.print_queue()   # 显示消息队列状态
            except:
                pass
            # TODO 发布的时候时候一定要改为2秒
            time.sleep(3)

    def update_queue(self):  #
        global StoreQueue, ReadQueue, CmsQueue
        try:
            if StoreQueue.qsize() > 0:  # 判断队列是否为空不为空  保存数据到数据库
                self.storespider()
            if ReadQueue.qsize() <= 0:  # 读取 采集
                self.readspider()
            if CmsQueue.qsize() <= 0:  # 读取 CMS识别
                self.readCmsQueue()
            if ReadQueue.empty():   # 如果读取的队列为空很可能断网了，此时应该休息5秒钟，免得数据库受不了
                #self.add_BQueue()   # 添加数据到消息队列
                time.sleep(5)
        except:
            pass

    def execute_sql(self, data):
        try:
            self.db.mysql_insert(data)  # 添加数据
            self.db.mysql_commit()      # 保存数据
        except Exception, e:
            pass

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

    def storespider(self):
        # 储存域名
        global StoreQueue, ReadQueue, CmsQueue, Cms_timeout
        try:
            int_insert = StoreQueue.qsize()  # 返回大小
            if int_insert <= 0:
                return
            for n in xrange(int_insert):
                tmphost = StoreQueue.get(0.2)   # 获取消息队列
                if not tmphost:
                    continue

                tmpcom = VVUtil.get_domain_suffix(tmphost)  # 解析域名后辍名
                tmpcom = tmpcom.replace(".", "_")  # 数据表名不支持. 替换下
                if not self.db.mysql_table_exist(tmpcom):
                    # 查询表明是否存在:#判断表是否有存在1有0无
                    self.mysql_czb(tmpcom)  # 创建表
                self.tablelist.add(tmpcom)
                sql_data = "insert into %s(url,time) VALUES('%s','%s') ;" % \
                           (tmpcom, tmphost, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                self.execute_sql(sql_data)
                #存在一个问题当表添加完后再保存数据  数据无法保存上
        except:
            pass

    def readspider(self):
        # 从数据库 读取URL
        global StoreQueue, ReadQueue, CmsQueue, Cms_timeout
        try:
            self.get_random_domain()  # 获取随机值 表名
            # 一次读取100个，别读取太多，假如程序重启的话，会有许多标记为已经爬取，但是实际上没有爬取
            sql_data = "select * from %s where open_send is null order by rand() limit 0,100;" % self.curdomain
            #查询open_send字段为空随机抽取500条
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                url = row[0]
                sql_data = "update %s set open_send='send' where url='%s'" % (self.curdomain, url)
                self.execute_sql(sql_data)
                ReadQueue.put(url, 0.1)
        except:
            pass

    def readCmsQueue(self):
        # 从数据库读取需要CMS识别的URL
        global StoreQueue, ReadQueue, CmsQueue, Cms_timeout
        try:
            self.get_random_domain()  # 获取随机值 表名
            #查询open_send字段为空随机抽取100条
            sql_data = "select * from %s where cms_send is null order by rand() limit 0,100;" % self.curdomain
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                # print '%s-%s-%s'%(row[0],row[1],row[2])
                url = row[0]
                sql_data = "update %s set cms_send='send' where url='%s'" % (self.curdomain, url)
                self.execute_sql(sql_data)
                CmsQueue.put(url, 0.5)
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

