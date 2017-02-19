#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#把数据库内容保存起来
##################################################
import string_data #变量保存
import Cmysql #数据库操作文件
import sfile #文件操作
import base64

def URL_TQURL(url): #提取文件后辍名
    try:
        nPos =url.rfind('.') #查找字符  从尾部查找
        sStr1 = url[nPos:len(url)] #复制指定长度的字符
        return sStr1
    except:
        pass

def download_index(download):
    try:
        sql_data="select * from download where download='%s'"%(download)
        index_cursor=Cmysql.sql.conn.cursor()
        n = index_cursor.execute(sql_data)
        index_cursor.scroll(0)
        for row in index_cursor.fetchall():
            index=string_data.path+string_data.url_Route+row[1]
            jpf_gif=URL_TQURL(row[1])
            if jpf_gif==".jpg":
                sfile.wb_file(index,base64.b64decode(row[2]))  #写入文本 中文
                continue  #跳过   这一次
            if jpf_gif==".gif":
                sfile.wb_file(index,base64.b64decode(row[2]))  #写入文本 中文
                continue  #跳过   这一次
            sfile.TXT_file(index,row[2])  #写入文本 中文
        index_cursor.close()
    except:
        pass










