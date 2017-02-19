#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from PyQt4.QtGui import *
import time
import socket
#import webbrowser #访问URL
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from ctypes import *
import re
#import win32ui
#import tkFileDialog
import sys,os
#import platform
#import tkMessageBox
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:2602159946"), 0)   # 调用MessageBoxA函数
import Csqlite3  #数据库操作
import urllib #转换成网络格式
import ConfigParser  #INI读取数据
import thread
import random

class   top_1(object):
    def __init__(self,ui,model):
        self.ui=ui
        self.model=model
        #数据库链接
        self.sql3=Csqlite3.C_sqlite3()
        self.sql3.mysqlite3_open()

    #添加数据
    def tableView_add(self,ints,s1=None,s2=None,s3=None,s4=None):  #添加数据
        try:
            #红色：(255,0,0)
            #绿色：(0,255,0)
            if not s1==None:
                self.model.setItem(ints, 0, QStandardItem(s1))
            if not s2==None:
                self.model.setItem(ints, 1, QStandardItem(s2))
            if not s3==None:
                self.model.setItem(ints, 2, QStandardItem(s3))
            if not s4==None:
                self.model.setItem(ints, 3, QStandardItem(s4))

            if s3=="No" or s3=="null" or s3==None or s3=="None":  #红色  #改变背景色
                self.model.item(ints,0).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,1).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,2).setBackground(QColor(255, 0, 0))#//改变背景色
                self.model.item(ints,3).setBackground(QColor(255, 0, 0))#//改变背景色

        except BaseException, e:
            print(str(e))
            #        self.model.setSortRole(0) #排序
            #        self.model.sort(3,Qt.AscendingOrder) #排序  排序只针对INT型
        self.ui.SQLite_tableView.setModel(self.model)

    def del_tableView(self):  #清空数据
        model = self.ui.SQLite_tableView.model()
        int_id=self.ui.SQLite_tableView.model().rowCount()
        for i in range(int_id,-1,-1):
            model.removeRow(i)

    def pushButton1(self): #导入
        self.del_tableView()  #清空数据
        dlg = QFileDialog(None)
        self.saveHistoryFilename = dlg.getOpenFileName()
        from os.path import isfile
        if isfile(self.saveHistoryFilename):
            xxx = file(self.saveHistoryFilename, 'r')
            i=0
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n')
                    data_time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    data_time=time.mktime(time.strptime(data_time2,'%Y-%m-%d %H:%M:%S'))  #转化成时间戳
                    line = data.split("|")
                    if len(line)>=2:
                        sql_data="insert into url(url,gjz,time) VALUES('%s','%s','%s')"%(str(line[0]),urllib.quote(str(line[1])),data_time)
                        #print sql_data
                        self.sql3.mysqlite3_insert(sql_data)
                        data1=u"%s"%(line[0])
                        data2=u"%s"%(line[1])
                        self.tableView_add(i,data1,data2,None,data_time2)  #添加数据

                    #sql_data="insert into url(url,time) VALUES('%s','%s')"%(urllib.quote(str(data.rstrip('\n'))),data_time)
                    i+=1
                except BaseException, e:
                    print(str(e))

    def time_localtime(self,data):  #时间戳转换成日期
        try:
            #return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(line[8]))
            ltime=time.localtime(float(data))
            return time.strftime("%Y-%m-%d %H:%M:%S", ltime)
        except BaseException, e:
            #print(str(e))
            return "--"

    def SQL_Button_1(self): #全部显示
        self.del_tableView()  #清空数据
        sql_data = "select * from url"   # asc 表示升序 , desc表示降序
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            s0=u"%s"%(str(line[0]))
            s1=u"%s"%(urllib.unquote(str(line[1])))
            self.tableView_add(int_id,s0,s1,str(line[2]),self.time_localtime(line[3]))  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def SQL_Button_2(self): #显示状态OK
        self.del_tableView()  #清空数据
        sql_data = "select * from url where bool='ok' order by time DESC"   # asc 表示升序 , desc表示降序
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            s0=u"%s"%(str(line[0]))
            s1=u"%s"%(urllib.unquote(str(line[1])))
            self.tableView_add(int_id,s0,s1,str(line[2]),self.time_localtime(line[3]))  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def SQL_Button_3(self): #显示状态NO
        self.del_tableView()  #清空数据
        sql_data = "select * from url where bool is null or bool='No' order by time DESC"   # asc 表示升序 , desc表示降序
        self.sql3.conn.commit()# 获取到游标对象
        cur = self.sql3.conn.cursor()# 用游标来查询就可以获取到结果
        cur.execute(sql_data)# 获取所有结果
        res = cur.fetchall()  #从结果中取出所有记录
        int_id=0
        for line in res:
            #self.url_data=line[0]
            s0=u"%s"%(str(line[0]))
            s1=u"%s"%(urllib.unquote(str(line[1])))
            self.tableView_add(int_id,s0,s1,str(line[2]),self.time_localtime(line[3]))  #添加数据
            int_id+=1
        cur.close()  #关闭游标

    def RE_Button(self): #查询
        re_data=self.ui.re_textEdit.toPlainText() #获取内容
        config = ConfigParser.ConfigParser()
        config.readfp(open("Server.ini"))
        config.set("Server","re_data",str(re_data))  #写入配置
        config.write(open("Server.ini", "w"))  #保存配置
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        thread.start_new_thread(self.thread_RE_Button,(str(re_data),))  #测试查询

    def re_cx_data(self,re_data,data):  #正则查询内容是否存在
        p = re.compile( r'%s'%re_data )
        sarr = p.findall(data)
        if len(sarr[0])>=7:
            return True,sarr[0]
        else:
            return False,0
            #return sarr[0]

    def url_http_200(self,int_data,url):
        try:
            statusCode =urllib.urlopen(url).getcode()
            #return statusCode==200  #返回 True  False
            if statusCode==200:
                #local = url.split('/')[-1]
                int_url_read=len(urllib.urlopen(url).read())
                if int_url_read>=int_data:
                    print "url:%s   len:%d"%(url,int_url_read)
                    return True
            return False
        except BaseException, e:
            print(str(e))
            return False

    def thread_RE_Button(self,re_data):
        #print re_data
        self.ui.RE_Button.setEnabled(0)  #给改成禁用
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                if self.url_http_200(int(re_data),str(s0)):
                    sql_data="update url set bool='ok' where url='%s'"%(str(s0))
                    print sql_data
                    self.sql3.mysqlite3_update(sql_data)
                    self.tableView_add(int_index,None,None,"ok",None)  #添加数据
                else:
                    sql_data="update url set bool='No' where url='%s'"%(str(s0))
                    print sql_data
                    self.sql3.mysqlite3_update(sql_data)
                    self.tableView_add(int_index,None,None,"No",None)  #添加数据
            except BaseException, e:
                print(str(e))
                pass
                #self.ui.RE_Button.setEnabled(1)
                #return 0
        self.ui.RE_Button.setEnabled(1)

    def pushButton2(self): #导出数据
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        data=""
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                data+=s0+"|"+s1+"\n"
            except BaseException, e:
                print(str(e))
            #        print data
        data_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        dlg = QFileDialog(None)
        self.filename = dlg.getSaveFileName(None,u"保存data", u"./"+data_time+u"data.txt",u"txt (*.txt)")
        #print self.filename
        file_object = open(self.filename, 'w')
        file_object.writelines(data)
        file_object.close()

    def pushButton3(self): #删除数据
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                sql_data="delete from url where url='%s'"%(str(s0))
                self.sql3.mysqlite3_delete(sql_data)
            except BaseException, e:
                print(str(e))
        self.SQL_Button_2() #显示状态OK

    def pushButton(self): #生成链接
        config = ConfigParser.ConfigParser()
        config.readfp(open("Server.ini"))
        config.set("Server","SL",str(self.ui.spinBox.value()))  #写入配置
        config.write(open("Server.ini", "w"))  #保存配置
        #print self.ui.textEdit.toPlainText() #获取内容
        re_data=str(self.ui.textEdit_4.toPlainText()) #获取内容

        self.list=[]
        int_model = self.ui.SQLite_tableView.selectionModel()  #获取选中编号
        model = self.ui.SQLite_tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        if len(int_model.selectedRows())==0:
            user32.MessageBoxW(0,c_wchar_p(u"请选择有效内容"), c_wchar_p(u"提示"), 0)   # 调用MessageBoxA函数
            return
        for index in int_model.selectedRows():       #// 对于被选中的每一行
            try:
                int_index=index.row()#获取行号
                s0= model.data(model.index(int_index,0)).toString()
                s1= model.data(model.index(int_index,1)).toString()
                arr=[]
                arr.append(str(s0))
                arr.append(str(s1))
                self.list.append(arr)
            except BaseException, e:
                print(str(e))
                pass


        js_int=self.ui.spinBox.value()  #获取要抽取多少行
        data_3=""
        lszs=len(self.list)
        for i in range(int(js_int)):
            #data_3+=self.list[self.sjs_random(0,len(self.list))]+"\n"
            #data_3+=self.list[self.sjs_random(0,len(self.list))]+"\n"
            list2=self.list[self.sjs_random(0,lszs)]
            re_data1=re_data.replace('$url',list2[0])
            re_data1=re_data1.replace('$key',list2[1])
            data_3+=re_data1+"\n"

        data_1=self.ui.textEdit.toPlainText() #获取内容   头
        data_2=self.ui.textEdit_2.toPlainText() #获取内容 尾巴
        data_3="%s%s%s"%(data_1,data_3,data_2)
        self.ui.textEdit_3.setText(u"")
        self.ui.textEdit_3.insertPlainText(u"%s"%(data_3))
    def sjs_random(self,zd0,zd1):  #获取随机数
        return random.randint(zd0, zd1)