#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#qq:29295842
#BLOG:http://hi.baidu.com/alalmn
# MYSQL 添加 删除 修改  查询
import time, MySQLdb
import ConfigParser  #INI读取数据


class mysql_handle():
    def __init__(self):
        self.mysql_host="localhost"
        self.mysql_user="root"
        self.mysql_pwd="313118740"
        self.mysql_db="ftp"

    def mysql_open(self):  #连接数据库
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            self.mysql_host = str(config.get("Server","Server"))
            self.mysql_user = str(config.get("Server","Username"))
            self.mysql_pwd = str(config.get("Server","password"))
            self.mysql_db = str(config.get("Server","db"))
        except:
            print "INI except"
            self.mysql_host="localhost"
            self.mysql_user="root"
            self.mysql_pwd="313118740"
            self.mysql_db="ftp"
            #return 0
        try:
            self.conn=MySQLdb.connect(host=self.mysql_host,user=self.mysql_user,passwd=self.mysql_pwd,db=self.mysql_db,charset="utf8")
            self.cursor = self.conn.cursor()
            #print u"服务器:",Server,u"用户名:",Username,u"密码:",password,u"连接数据库:",db,u"登录服务器成功"
            #print u"mysql:---登录服务器成功"
        except:
            print "###localhost:%s Username:%s password:%sdb:%s   except###"%(self.mysql_host,self.mysql_user,self.mysql_pwd,self.mysql_db)
           # print u"###服务器连接失败:",self.mysql_host,u"用户名:",self.mysql_user,u"密码:",self.mysql_pwd,u"连接数据库:",self.mysql_db,u"登录服务器失败###"
            return 0

    def mysql_S(self):  #保存数据
        try:
            self.conn.commit()   #提交   这句害死我了
        except:
            print "NYSQL s except"
            return 0

    def mysql_close(self):  #关闭数据库
        try:
            #print u"关闭数据库"
            self.conn.close()
        except:
            print "NYSQL close except"
            return 0

    def mysql_select_B(self,b_data):  #查询表是否存在
        self.cursor=self.conn.cursor()
        try:
            sqlA="show tables"
            n = self.cursor.execute(sqlA)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                #print '%s-%s-%s'%(row[0],row[1],row[2])
                if row[0]==b_data:
                    return 1
            return 0
        except:
            return 0

    def mysql_select(self,data):  #查询数据
        self.cursor=self.conn.cursor()
        try:
            n = self.cursor.execute(data)
            self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                #print '%s-%s-%s'%(row[0],row[1],row[2])
                return row[0]
        except:
            return "null123456"
        self.cursor.close()

    def mysql_insert(self,data):  #添加数据
        try:
            return self.cursor.execute(data)
        except:
            #print u"添加数据异常%s"%(data)
            return 0


    def mysql_update(self,data):  #修改数据
        try:
            return self.cursor.execute(data)
        except:
            return 0

    def mysql_delete(self,data):  #删除数据
        try:
            return self.cursor.execute(data)
        except:
            return 0






if __name__=='__main__':
    new=mysql_handle()
    new.mysql_open()
