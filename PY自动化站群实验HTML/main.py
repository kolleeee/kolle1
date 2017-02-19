#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
import string_data #变量保存
import Cmysql #数据库操作文件
import os
import sys
import index #生成首页
import download #把数据库内容保存到本地
import chanpen #产品列表
#神龙  QQ 29295842
#全静态站群系统
################################################
def open_sql():
    try:
        sql_data="select * from url"
        cursor=Cmysql.sql.conn.cursor()
        n = cursor.execute(sql_data)
        cursor.scroll(0)
        for row in cursor.fetchall():
            index.index(row[0])         #url地址
            chanpen.index_data()   #生成文章
            download.download_index(row[4]) #
        cursor.close()
    except:
        pass

def cur_file_dir():  #获取脚本文件的当前路径
    path = sys.path[0]#获取脚本路径
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
################################################
if __name__=='__main__':
    string_data.path = cur_file_dir()
    open_sql()





