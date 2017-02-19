#!/usr/bin/env python
#-*- coding: UTF-8 -*-
##################################################
#qq:29295842
#BLOG:http://hi.baidu.com/alalmn
# MYSQL 添加 删除 修改  查询
#import time
import MySQLdb
import ConfigParser
#import os


class VVMysql(object):
    def __init__(self):
        self.mysql_host = "localhost"
        self.mysql_user = "root"
        self.mysql_pwd = "316118740"
        self.mysql_db = "uel"
        self.conn = None
        self.cursor = None
        self.debug_on = 1
        self._readcfg()

    def _readcfg(self):
        global cfgpath
        config = ConfigParser.ConfigParser()
        config.readfp(open("Server.ini"))
        self.mysql_host = str(config.get("Server", "Server"))
        self.mysql_user = str(config.get("Server", "Username"))
        self.mysql_pwd = str(config.get("Server", "password"))
        self.mysql_db = str(config.get("Server", "db"))
        self.debug_on = int(config.get("DEBUG", "showdetail"))

    def mysql_create_database(self):
        # 创建数据库
        try:
            self.conn = MySQLdb.connect(host=self.mysql_host, user=self.mysql_user, passwd=self.mysql_pwd,
                                        charset="utf8")
            self.cursor = self.conn.cursor()
            sql = 'CREATE DATABASE IF NOT EXISTS %s' % self.mysql_db
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception, e:
            if self.debug_on:
                print '[mysql] Fail to create database!![%s]' % e
        self.mysql_close()
        return 0

    def mysql_open(self):
        # 连接数据库
        try:
            self.conn = MySQLdb.connect(host=self.mysql_host, user=self.mysql_user, passwd=self.mysql_pwd,
                                        db=self.mysql_db, charset="utf8")
            self.cursor = self.conn.cursor()
            if self.debug_on:
                print "[mysql] Connected! link"
        except:
            if self.debug_on:
                print "[mysql] Fail:", self.mysql_host, "name:", self.mysql_user, "password:",\
                    self.mysql_pwd, "database:", self.mysql_db
                return -1
        return 0

    def mysql_close(self):
        #关闭数据库
        try:
            if self.debug_on:
                print "[mysql] Close Database"
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.conn:
                self.conn.close()
                self.conn = None
        except:
            if self.debug_on:
                print "[mysql] close except"
            return -1
        return 0

    def mysql_closecursor(self):
        try:
            if self.cursor:
                self.cursor.close()
        except:
            pass
        self.cursor = None

    def mysql_commit(self):
        #保存数据
        try:
            #提交   这句害死我了
            self.conn.commit()
        except:
            if self.debug_on:
                print "[mysql] commit except"
            return -1
        return 0

    def mysql_reopen(self):
        # 重新连接数据库
        try:
            self.mysql_close()
            self.mysql_open()
        except:
            return -1
        return 0

    def mysql_gettables(self):
        tables = []
        try:
            if not self.cursor:
                self.cursor = self.conn.cursor()
            sql = "show tables ;"
            n = self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                tables.append(str(row[0]))
        except Exception, e:
            pass
        return tables

    def mysql_table_exist(self, tablename):
        #查询表是否存在
        if not self.cursor:
            self.cursor = self.conn.cursor()
        try:
            sql = "show tables ;"
            n = self.cursor.execute(sql)
            #self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                if row[0] == tablename:
                    return 1
        except Exception, e:
            pass

    def mysql_select(self, sql):
        #查询数据
        if not self.cursor:
            self.cursor = self.conn.cursor()
        try:
            n = self.cursor.execute(sql)
            #self.cursor.scroll(0)
            for row in self.cursor.fetchall():
                return row[0]
        except:
            return "null123456"

    def mysql_insert(self, sql):
        #添加数据
        return self.mysql_exesql(sql)

    def mysql_update(self, sql):
        #修改数据
        return self.mysql_exesql(sql)

    def mysql_delete(self, sql):
        #删除数据
        return self.mysql_exesql(sql)

    def mysql_exesql(self, sql):
        if not self.cursor:
            self.cursor = self.conn.cursor()
        try:
            return self.cursor.execute(sql)
        except Exception, e:
            if str(e).find('close') >= 0:
                self.mysql_closecursor()

if __name__ == '__main__':
    db = VVMysql()
    db.mysql_create_database()
    db.mysql_open()
    db.mysql_close()

