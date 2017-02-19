#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#把图片写入MYSQL  在读取出来
#存储字段 mediumblob
#########################################
import Cmysql #数据库操作文件
import MySQLdb as mdb
import MySQLdb
import base64
def open_jpg(name):   #打开图片
    try:
        fin = open(name,'rb')
        img = fin.read()
        fin.close()

        #sql_data="insert into download(download,name,data) VALUES('str_1,'%s','%s')"%("\\"+name,mdb.escape_string(img))
        sql_data="insert into download(download,name,data) VALUES('str_1','%s','%s')"%(name,base64.b64encode(img))
        print sql_data
        Cmysql.sql.mysql_insert(sql_data)
        Cmysql.sql.mysql_S()  #保存数据
    except BaseException, e:
        print u"打开图片失败",(str(e))
        pass

def URL_TQURL(url): #提取文件后辍名
    try:
        nPos =url.rfind('.') #查找字符  从尾部查找
        sStr1 = url[nPos:len(url)] #复制指定长度的字符
        return sStr1
    except:
        pass

import os
def list_file():
    for root, dirs, files in os.walk('.'):
        for file in files:
            jpf_gif=URL_TQURL(file)
            if jpf_gif==".jpg":
                open_jpg(file)
            if jpf_gif==".gif":
                open_jpg(file)

if __name__=='__main__':
    list_file()
#    open_jpg("menu_r_bg.gif")
#    open_jpg("menu.jpg")
#    open_jpg("menu_h.jpg")

#    data="C:\\Users\Administrator.YKE5DH373UVCX0W\\Desktop\\HTML\\69.176.89.5\\wwwroot\\www.123456.com\\index.jpg"
#    print URL_TQURL(data)


