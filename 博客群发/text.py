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
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数

class   text(object):
    def __init__(self,ui):
        self.ui=ui

    def open_pals(self):
        try:
            dlg = QFileDialog(None)
            self.saveHistoryFilename = dlg.getOpenFileName()
            from os.path import isfile
            if isfile(self.saveHistoryFilename):
                return u"%s"%(self.saveHistoryFilename)
            return "null"
        except Exception, e:
            return ""

    def avr_list_pals1(self): #读取路径
#        Title_data=self.ui.Title_textEdit.toPlainText() #获取内容
#        avr_list1_textEdit
#        self.ui.avr_list1_textEdit.setText(data)
        self.ui.avr_list1_textEdit.setText(self.open_pals())
    def avr_list_pals2(self): #读取路径
        self.ui.avr_list2_textEdit.setText(self.open_pals())
    def avr_list_pals3(self): #读取路径
        self.ui.avr_list3_textEdit.setText(self.open_pals())
    def avr_list_pals4(self): #读取路径
        self.ui.avr_list4_textEdit.setText(self.open_pals())
    def avr_list_pals5(self): #读取路径
        self.ui.avr_list5_textEdit.setText(self.open_pals())
    def avr_list_pals6(self): #读取路径
        self.ui.avr_list6_textEdit.setText(self.open_pals())
    def avr_list_pals7(self): #读取路径
        self.ui.avr_list7_textEdit.setText(self.open_pals())
    def avr_list_pals8(self): #读取路径
        self.ui.avr_list8_textEdit.setText(self.open_pals())
    def avr_list_pals9(self): #读取路径
        self.ui.avr_list9_textEdit.setText(self.open_pals())
    def avr_list_pals10(self): #读取路径
        self.ui.avr_list10_textEdit.setText(self.open_pals())

    def wz_list_pals1(self): #读取路径
        self.ui.wz_list1_textEdit.setText(self.open_pals())
    def wz_list_pals2(self): #读取路径
        self.ui.wz_list2_textEdit.setText(self.open_pals())
    def wz_list_pals3(self): #读取路径
        self.ui.wz_list3_textEdit.setText(self.open_pals())
    def wz_list_pals4(self): #读取路径
        self.ui.wz_list4_textEdit.setText(self.open_pals())
    def wz_list_pals5(self): #读取路径
        self.ui.wz_list5_textEdit.setText(self.open_pals())
    #def avr_list_bc(self,i):   #保存配置信息