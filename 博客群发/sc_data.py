#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from PyQt4.QtGui import *
import time
import socket
#import webbrowser #访问URL
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
from ctypes import *
import re
import random
#import win32ui
#import tkFileDialog
import sys,os
#import platform
#import tkMessageBox
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数

class   sc_data(object):
    def __init__(self,ui):
        self.ui=ui
        self.avr_list1=[]  #关键字链接
        self.avr_list2=[]  #关键字链接
        self.avr_list3=[]  #关键字链接
        self.avr_list4=[]  #关键字链接
        self.avr_list5=[]  #关键字链接
        self.avr_list6=[]  #关键字链接
        self.avr_list7=[]  #关键字链接
        self.avr_list8=[]  #关键字链接
        self.avr_list9=[]  #关键字链接
        self.avr_list10=[]  #关键字链接

        self.wz_list1=[]  #文章内容
        self.wz_list2=[]  #文章内容
        self.wz_list3=[]  #文章内容
        self.wz_list4=[]  #文章内容
        self.wz_list5=[]  #文章内容
        self.open_txt()   #读取



    def open_txt(self):   #读取
        self.avr_list1=[]  #关键字链接
        self.avr_list2=[]  #关键字链接
        self.avr_list3=[]  #关键字链接
        self.avr_list4=[]  #关键字链接
        self.avr_list5=[]  #关键字链接
        self.avr_list6=[]  #关键字链接
        self.avr_list7=[]  #关键字链接
        self.avr_list8=[]  #关键字链接
        self.avr_list9=[]  #关键字链接
        self.avr_list10=[]  #关键字链接

        self.wz_list1=[]  #文章内容
        self.wz_list2=[]  #文章内容
        self.wz_list3=[]  #文章内容
        self.wz_list4=[]  #文章内容
        self.wz_list5=[]  #文章内容
        try:
            xxx = file(u"%s"%(self.ui.avr_list1_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list1.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list1)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list1_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list1_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list2_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list2.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list2)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list2_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list2_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list3_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list3.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list3)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list3_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list3_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list4_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list4.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list4)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list4_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list4_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list5_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list5.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list5)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list5_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list5_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list6_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list6.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list6)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list6_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list6_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list7_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list7.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list7)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list7_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list7_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list8_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list8.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list8)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list8_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list8_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list9_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list9.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list9)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list9_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list9_textEdit.toPlainText()))
            pass
        try:
            xxx = file(u"%s"%(self.ui.avr_list10_textEdit.toPlainText()), 'r')  #关键字
            for xxx_line in xxx.readlines():
                self.avr_list10.append(xxx_line.strip().lstrip())  #添加数据+"\r\n"
            random.shuffle(self.avr_list10)   #打算数组原有排序方式
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.avr_list10_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.avr_list10_textEdit.toPlainText()))
            pass

        try:
            file_object = open(u"%s"%(self.ui.wz_list1_textEdit.toPlainText()))  #内容
            try:
                self.htm_html_text = file_object.read()
                self.htm_html_text=self.open_file_null(self.htm_html_text).replace('。','.')  #清除空行
                self.wz_list1 = self.htm_html_text.split(".")
                random.shuffle(self.wz_list1)   #打算数组原有排序方式
            finally:
                file_object.close()
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.wz_list1_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.wz_list1_textEdit.toPlainText()))
            pass
        try:
            file_object = open(u"%s"%(self.ui.wz_list2_textEdit.toPlainText()))  #内容
            try:
                self.htm_html_text = file_object.read()
                self.htm_html_text=self.open_file_null(self.htm_html_text).replace('。','.')  #清除空行
                self.wz_list2 = self.htm_html_text.split(".")
                random.shuffle(self.wz_list2)   #打算数组原有排序方式
            finally:
                file_object.close()
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.wz_list2_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.wz_list2_textEdit.toPlainText()))
            pass
        try:
            file_object = open(u"%s"%(self.ui.wz_list3_textEdit.toPlainText()))  #内容
            try:
                self.htm_html_text = file_object.read()
                self.htm_html_text=self.open_file_null(self.htm_html_text).replace('。','.')  #清除空行
                self.wz_list3 = self.htm_html_text.split(".")
                random.shuffle(self.wz_list3)   #打算数组原有排序方式
            finally:
                file_object.close()
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.wz_list3_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.wz_list3_textEdit.toPlainText()))
            pass
        try:
            file_object = open(u"%s"%(self.ui.wz_list4_textEdit.toPlainText()))  #内容
            try:
                self.htm_html_text = file_object.read()
                self.htm_html_text=self.open_file_null(self.htm_html_text).replace('。','.')  #清除空行
                self.wz_list14= self.htm_html_text.split(".")
                random.shuffle(self.wz_list4)   #打算数组原有排序方式
            finally:
                file_object.close()
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.wz_list4_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.wz_list4_textEdit.toPlainText()))
            pass
        try:
            file_object = open(u"%s"%(self.ui.wz_list5_textEdit.toPlainText()))  #内容
            try:
                self.htm_html_text = file_object.read()
                self.htm_html_text=self.open_file_null(self.htm_html_text).replace('。','.')  #清除空行
                self.wz_list5 = self.htm_html_text.split(".")
                random.shuffle(self.wz_list5)   #打算数组原有排序方式
            finally:
                file_object.close()
        except Exception, e:
            #print u"读取文件 %s 异常"%(self.ui.wz_list5_textEdit.toPlainText())
            self.ui.messagebox.append(u"读取文件 %s 异常"%(self.ui.wz_list5_textEdit.toPlainText()))
            pass

    def open_file_null(self,file_data):  #清除空行
        data=""
        p = re.compile( r'.+?\n')
        sarr = p.findall(file_data)
        for every in sarr:
            if every.split():
                data+=every.lstrip().rstrip().strip().rstrip('\n')
        return data

    ###########################
    def cx_re_sl(self,data,re_data):  #查询数量
        try:
            p = re.compile( r'%s'%(re_data))
            sarr = p.findall(data)
            return len(sarr)
        except Exception, e:
            #print e
            return 0

    def sj_lis(self,lis_data):  #获取随机内容
        try:
            return lis_data[random.randint(1,len(lis_data))]
        except Exception, e:
            return "pass"
            #return random.randint(zd0, zd1)
    #内容的生成
    def sc_data(self,html_data):  #生成内容
        list1 = self.cx_re_sl(html_data,'{avr_list1}')  #查询数量
        if not list1==0:
            for i in range(list1):
                avr_list1 = str(self.sj_lis(self.avr_list1))
                html_data = html_data.replace('{avr_list1}',avr_list1,1)  #替换内容

        list2 = self.cx_re_sl(html_data,'{avr_list2}')  #查询数量
        if not list2==0:
            for i in range(list2):
                avr_list2 = str(self.sj_lis(self.avr_list2))
                html_data = html_data.replace('{avr_list2}',avr_list2,1)  #替换内容

        list3 = self.cx_re_sl(html_data,'{avr_list3}')  #查询数量
        if not list3==0:
            for i in range(list3):
                avr_list3 = str(self.sj_lis(self.avr_list3))
                html_data = html_data.replace('{avr_list3}',avr_list3,1)  #替换内容

        list4 = self.cx_re_sl(html_data,'{avr_list4}')  #查询数量
        if not list4==0:
            for i in range(list4):
                avr_list4 = str(self.sj_lis(self.avr_list4))
                html_data = html_data.replace('{avr_list4}',avr_list4,1)  #替换内容

        list5 = self.cx_re_sl(html_data,'{avr_list5}')  #查询数量
        if not list5==0:
            for i in range(list5):
                avr_list5 = str(self.sj_lis(self.avr_list5))
                html_data = html_data.replace('{avr_list5}',avr_list5,1)  #替换内容

        list6 = self.cx_re_sl(html_data,'{avr_list6}')  #查询数量
        if not list6==0:
            for i in range(list6):
                avr_list6 = str(self.sj_lis(self.avr_list6))
                html_data = html_data.replace('{avr_list6}',avr_list6,1)  #替换内容

        list7 = self.cx_re_sl(html_data,'{avr_list7}')  #查询数量
        if not list7==0:
            for i in range(list7):
                avr_list7 = str(self.sj_lis(self.avr_list7))
                html_data = html_data.replace('{avr_list7}',avr_list7,1)  #替换内容

        list8 = self.cx_re_sl(html_data,'{avr_list8}')  #查询数量
        if not list8==0:
            for i in range(list8):
                avr_list8 = str(self.sj_lis(self.avr_list8))
                html_data = html_data.replace('{avr_list8}',avr_list8,1)  #替换内容

        list9 = self.cx_re_sl(html_data,'{avr_list9}')  #查询数量
        if not list9==0:
            for i in range(list9):
                avr_list9 = str(self.sj_lis(self.avr_list9))
                html_data = html_data.replace('{avr_list9}',avr_list9,1)  #替换内容

        list10 = self.cx_re_sl(html_data,'{avr_list10}')  #查询数量
        if not list10==0:
            for i in range(list10):
                avr_list10 = str(self.sj_lis(self.avr_list10))
                html_data = html_data.replace('{avr_list10}',avr_list10,1)  #替换内容

        #{wz_list1}：
        wz_list1 = self.cx_re_sl(html_data,'{wz_list1}')  #查询数量
        if not wz_list1==0:
            for i in range(wz_list1):
                th=str(self.sj_lis(self.wz_list1)+"。")  #文章
                html_data = html_data.replace('{wz_list1}',th,1)

        wz_list2 = self.cx_re_sl(html_data,'{wz_list2}')  #查询数量
        if not wz_list2==0:
            for i in range(wz_list2):
                th=str(self.sj_lis(self.wz_list2)+"。")  #文章
                html_data = html_data.replace('{wz_list2}',th,1)

        wz_list3 = self.cx_re_sl(html_data,'{wz_list3}')  #查询数量
        if not wz_list3==0:
            for i in range(wz_list3):
                th=str(self.sj_lis(self.wz_list3)+"。")  #文章
                html_data = html_data.replace('{wz_list3}',th,1)

        wz_list4 = self.cx_re_sl(html_data,'{wz_list4}')  #查询数量
        if not wz_list4==0:
            for i in range(wz_list4):
                th=str(self.sj_lis(self.wz_list4)+"。")  #文章
                html_data = html_data.replace('{wz_list4}',th,1)

        wz_list5 = self.cx_re_sl(html_data,'{wz_list5}')  #查询数量
        if not wz_list5==0:
            for i in range(wz_list5):
                th=str(self.sj_lis(self.wz_list5)+"。")  #文章
                html_data = html_data.replace('{wz_list5}',th,1)

        return html_data
    ###############################

    def cs_pushButton(self):  #生成文章
        #self.open_txt()   #读取

        Title_data=self.ui.Title_textEdit.toPlainText()  #读取内容
        self.ui.cs_Title_textEdit.setText(u"%s"%(self.sc_data(u"%s"%(Title_data))))  #写入内容

        Content_data=self.ui.Content_textEdit.toPlainText()  #读取内容
        self.ui.cs_Content_textEdit.setText(u"%s"%(self.sc_data(u"%s"%(Content_data))))  #写入内容









