#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#生成index 首页
##################################################
import string_data #变量保存
import Cmysql #数据库操作文件
import sfile #文件操作
import os
import re
import time

def index(url):
    try:
        sql_data="select * from url where url='%s'"%(url)
        index_cursor=Cmysql.sql.conn.cursor()
        n = index_cursor.execute(sql_data)
        index_cursor.scroll(0)
        for row in index_cursor.fetchall():
            string_data.url_url=row[0]         #url地址
            string_data.url_Route=row[1]       #本地保存路径
            string_data.url_Sindex=row[2]       #模板
            string_data.url_index_data=row[3]  #首页内容
            string_data.url_download=row[4]   #保存文件
            string_data.url_chanpen=row[5]   #产品
            string_data.url_chanpen_data=row[6]   #产品模板
            string_data.url_wenzhang=row[7]   #文章
            string_data.url_wenzhang_data=row[8]   #文章模板
        index_cursor.close()

        #sfile.Route(string_data.path+string_data.url_Route)  #创建本地保存路径
        index_data()
    except:
        pass

def index_replace(strdata,name,data): #内容  替换关键字   替换内容
    try:
        strdata=strdata.replace(name,data)
        return strdata
    except:
        pass

def mysql_index(index,data):   #查询内容
    try:
        sql_data="select data from Sindex  where Sindex='%s' and name='%s'"%(index,data)
        index_cursor=Cmysql.sql.conn.cursor()
        n = index_cursor.execute(sql_data)
        index_cursor.scroll(0)
        for row in index_cursor.fetchall():
            data=row[0]
        index_cursor.close()
        return data
    except:
        return ""
        pass

def index_data():   #创建首页
    try:
        index=string_data.path+string_data.url_Route+'\index.html'
        if not os.path.exists(index):  #文件不存在就创建
            print u"首页不存在"
            Adata=string_data.url_index_data
            #print index_replace(string_data.url_index_data)
            #正则出需要喜欢的内容
            p = re.compile(r'{.*?}')
            sarr = p.findall(Adata)
            for every in sarr:
                data1=mysql_index(string_data.url_Sindex,every)   #查询内容
                #print every+"------"+data1
                if data1!="":
                    Adata=index_replace(Adata,every,data1) #内容  替换关键字   替换内容
                #time.sleep(0.5)
            #print Adata
            sfile.TXT_file(index,Adata)  #写入文本 中文
    except:
        pass



if __name__=='__main__':
    Route("9.176.89.5\wwwroot\www.123456.com")  #创建本地保存路径
    #print os.getcwd()


