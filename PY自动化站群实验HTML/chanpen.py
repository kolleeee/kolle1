#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#生成产品页面
##################################################
import string_data #变量保存
import Cmysql #数据库操作文件
import sfile #文件操作
import os
import re
import time
import random
def sj(): #产生随机字符
    try:
        #seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(8):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        return salt
    except:
        pass


def index_data():   #创建文章
    try:
        index=string_data.path+string_data.url_Route+'\\chanpin\\'+sj()+'.html'
        Adata=string_data.url_chanpen_data
        #正则出需要喜欢的内容
        p = re.compile(r'{.*?}')
        sarr = p.findall(Adata)
        for every in sarr:
            data1=mysql_index(string_data.url_Sindex,every)   #查询内容
            #print every+"------"+data1
            if data1!="":
                Adata=index_replace(Adata,every,data1) #内容  替换关键字   替换内容
                    #time.sleep(0.5)
        sfile.TXT_file(index,Adata)  #写入文本 中文
        print Adata
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


