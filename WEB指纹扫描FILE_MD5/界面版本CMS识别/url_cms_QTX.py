#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
################################################
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from threading import Thread
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
import list
import time
import hashlib
import urllib2
import httplib
import socket
socket.setdefaulttimeout(10)
import Class_url_cms  #CMS识别类
#import win32ui
#user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import os
import Queue
cms_url = Queue.Queue() #需要CMS识别
Q_message = Queue.Queue() #需要CMS识别
Q_update = Queue.Queue() #更新URL ["url地址","CMS名称","识别方式","识别URL链接文件","关键字ORMD5"]
S_suliang=0  #扫描完成的数量
Z_suliang=0  #总数量
cms_time=0  #扫描超时时间
OK_CMS=0  #已经识别出来的RUL个数
class url_cms_QTX(QtCore.QThread):
    def __init__(self,ui,model):
        QtCore.QThread.__init__(self)
        self.ui=ui
        self.model=model
        self.connect(self, SIGNAL("J_D_T"),self.J_D_T)  #创建信号
        self.connect(self, SIGNAL("tableView_add_0"),self.tableView_add_0)  #创建信号
        self.connect(self, SIGNAL("tableView_del"),self.tableView_del)  #创建信号
        self.connect(self, SIGNAL("tableView_update"),self.tableView_update)  #创建信号
        self.connect(self, SIGNAL("gx_text"),self.gx_text)  #创建信号
        self.connect(self, SIGNAL("messagebox_textEdit_add"),self.messagebox_textEdit_add)  #创建信号
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button) #创建消息  导入URL
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button_2) #创建消息  开始CMS识别
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button_3) #创建消息  倒出数据
        QtCore.QObject.connect(self.ui.tableView_1, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.SJIndex)   #双击事件
        t1 = Thread(target=self.Q_message_tableView)#指定目标函数，传入参数，这里参数也是元组
        t1.start()  #启动线程
        t2 = Thread(target=self.Q_update_tableView)#指定目标函数，传入参数，这里参数也是元组
        t2.start()  #启动线程

    def gx_text(self): #更新
        try:
            global Z_suliang,S_suliang,OK_CMS
            data=u"<html><head/><body><p align=\"center\">共:%d条URL/扫描完成:%d/已识别出来CMS:%d</p></body></html>"%\
                 (Z_suliang,S_suliang,OK_CMS)
            self.ui.label_2.setText(data)
        except:
            pass

    def SJIndex(self, index):  #双击事件
        try:
            #print self.ui.tab3_tableView_1.currentIndex().row()  可以使用这个获取当前选择行
            model = self.ui.tableView_1.model()
            url=model.data(model.index(index.row(),0)).toString()
            print url
            os.startfile(str(url))
        except BaseException, e:
            print(str(e))
            pass

    def Button_3(self):
        try:
            file_data=str(QtGui.QFileDialog.getExistingDirectory(None,u"数据另存为",".."))
#            print file_data+"\\"
#            name="%s/%s.txt"%(file_data,"xxx")
            if file_data:
                int_View=self.ui.tableView_1.model().rowCount()   #获取共多少行
                model = self.ui.tableView_1.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
                for index in range(int_View):
                    s0= model.data(model.index(index,0)).toString()   #url
                    s1= model.data(model.index(index,1)).toString()   #cms
                    if s1:
                        name="%s/%s.txt"%(file_data,str(s1))
                        self.TXT_file_add(name,str(s0))  #写入文本
        except:
            pass

    def TXT_file_add(self,name,url):  #写入文本
        try:
            file_object = open(name,'a')
            file_object.writelines(url)
            #file_object.write(url.encode("utf-8")) #成功
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            print name,"TXT except",url,e
            return 0

    def b_d_i(self,i1,i2):  #print b_d_i(10,100)
        try:
            rate=float(i1)/float(i2)
            return int(rate*100)
        except:
            return 0

    def J_D_T(self):  #进度条
        try:
            global S_suliang,Z_suliang
            jdt=self.b_d_i(S_suliang,Z_suliang)
            self.ui.progressBar.setValue(int(jdt))  #设置进度
        except:
            pass

    def tableView_add_0(self,s0):
        try:
            ints=self.ui.tableView_1.model().rowCount()   #获取共多少行
            if not s0==None:
                self.model.setItem(ints, 0, QStandardItem(s0))
        except:
            pass
        self.ui.tableView_1.setModel(self.model)

    def tableView_del(self):  #清空全部数据
        try:
            int_View=self.ui.tableView_1.model().rowCount()   #获取共多少行
            for index in range(int_View):
                self.model.removeRow(index)
            self.ui.tableView_1.setModel(self.model)
        except:
            self.ui.tableView_1.setModel(self.model)
            pass

    def messagebox_textEdit_add(self,data):
        try:
            self.ui.messagebox_textEdit.append(data)
        except:
            pass

    def Button(self): #导入URL地址
        try:
            #            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt File (*.txt)|*.txt|All files|*.*")
            #        #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            #            dlg.DoModal()
            #            fname = dlg.GetPathName() # 获取选择的文件名称
            fName=str(QtGui.QFileDialog.getOpenFileName(None,u"打开文件","",u"txt File (*.txt)"))
            #fname = "net.txt"
            if fName:
                t1 = Thread(target=self.ofr_file,args=(fName,))#指定目标函数，传入参数，这里参数也是元组
                t1.start()  #启动线程
        except:
            pass

    def ofr_file(self,file_name):
        try:
            self.emit(SIGNAL("tableView_del"))  #清空全部数据
            LS1 = list.Clist()  #初始化类
            LS1.list_del()  #清空list列表
            xxx = file(file_name, 'r')
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n')
                    LS1.liet_add(data)  #添加数据
                except:
                    pass
            LS1.liet_lsqc() #数组列表去重复
            self.emit(SIGNAL("messagebox_textEdit_add"), u"导入URL列表\n原数据量:%d\n去除重复后:%d\n开始导入"%(len(LS1.list),len(LS1.list_2))) #发送信号
            for url in LS1.list_2:  #读取数据
                self.emit(SIGNAL("tableView_add_0"),url) #发送信号
            self.emit(SIGNAL("messagebox_textEdit_add"), u"导入完成")
        except:
            pass

    def Queue_del(self): #清空数组
        try:
            if cms_url.empty():   #判断队列是否为空
                return 0
            url_int=cms_url.qsize()  #获取总数量
            for i in range(int(url_int)):
                cms_url.get(0.1)  #get()方法从队头删除并返回一个项目
        except:
            pass

    def Button_2(self):
        try:
            global Z_suliang,cms_time
            self.Queue_del() #清空数组
            int_View=self.ui.tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tableView_1.model()
            for index in range(int_View):
                s0= model.data(model.index(index,0)).toString()
                cms_url.put(str(s0),1)
            Z_suliang=cms_url.qsize()  #总数量
            self.emit(SIGNAL("messagebox_textEdit_add"), u"需要扫描%d URL"%(cms_url.qsize()))
            T_X=self.ui.spinBox.text()  #获取线程数
            cms_time_data=int(self.ui.spinBox_2.text())  #获取线程数
            if cms_time_data<=10:
                cms_time_data=100
            cms_time=cms_time_data
            threads = []  #线程
            self.emit(SIGNAL("gx_text"))  #更新 文本
            for i in range(int(T_X)):  #nthreads=10  创建10个线程 int(T_X)
                threads.append(Class_url_cms.Class_url_cms(i))

            for t in threads:   #不理解这是什么意思    是结束线程吗
                t.start()  #start就是开始线程
        except:
            pass
    ########################################################
    def Q_message_tableView(self):
        try:
            while True:
                if Q_message.empty():   #判断队列是否为空
                    time.sleep(3)
                    continue  #跳过
                url_int=Q_message.qsize()  #获取总数量
                for i in range(int(url_int)):
                    self.message = Q_message.get(0.5)  #get()方法从队头删除并返回一个项目
                    if self.message=="":
                        time.sleep(1)
                        continue  #跳过
                    self.emit(SIGNAL("J_D_T"))  #进度条
                    self.emit(SIGNAL("gx_text"))  #更新 文本
                    self.emit(SIGNAL("messagebox_textEdit_add"),self.message)
                    time.sleep(0.01)
                time.sleep(1)
        except:
            pass

    def tableView_update(self,url_list):
        try:
            global OK_CMS
            int_View=self.ui.tableView_1.model().rowCount()   #获取共多少行
            model = self.ui.tableView_1.model()
            for index in range(int_View):
                s0= model.data(model.index(index,0)).toString()
                if s0.replace(" ", "") ==url_list[0].replace(" ", ""):
                    OK_CMS+=1  #已经识别出来的RUL个数
                    if not url_list[1]==None:
                        self.model.setItem(index, 1, QStandardItem(url_list[1]))
                    if not url_list[2]==None:
                        self.model.setItem(index, 2, QStandardItem(url_list[2]))
                    if not url_list[3]==None:
                        self.model.setItem(index, 3, QStandardItem(url_list[3]))
                    if not url_list[4]==None:
                        self.model.setItem(index, 4, QStandardItem(url_list[4]))
                    break #跳出
            self.emit(SIGNAL("gx_text"))  #更新 文本
        except BaseException, e:
            print(str(e))
        self.ui.tableView_1.setModel(self.model)

    def Q_update_tableView(self):
        try:
            while True:
                if Q_update.empty():   #判断队列是否为空
                    time.sleep(3)
                    continue  #跳过
                url_int=Q_update.qsize()  #获取总数量
                for i in range(int(url_int)):
                    self.update = Q_update.get(0.5)  #get()方法从队头删除并返回一个项目
                    if self.update=="":
                        time.sleep(1)
                        continue  #跳过
                    self.emit(SIGNAL("J_D_T"))  #进度条
                    self.emit(SIGNAL("tableView_update"),self.update)
                    self.emit(SIGNAL("gx_text"))  #更新 文本
                    time.sleep(0.01)
                time.sleep(1)
        except:
            pass



