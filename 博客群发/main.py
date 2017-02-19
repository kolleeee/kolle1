#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from uimain import *

import socket
socket.setdefaulttimeout(10)
import ConfigParser

from ctypes import *
#import win32ui
import thread
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Start(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #http://www.cnblogs.com/caomingongli/archive/2011/09/19/2181842.html    这个不错   PyQt之自定义无边框窗口遮盖任务栏显示问题
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        #self.setWindowTitle(u'')  #设置标题
        self.ini_data() #初始化数据
        #事件处理
        self.ui.messagebox.append(u"搜狐博客群发(写个练下手)")
        self.ui.messagebox.append(u"神龙  QQ:29295842")
        ##########################
        from text import text    #文件路径
        self.text=text(self.ui)
        from sc_data import sc_data   #文章生成
        self.sc_data=sc_data(self.ui)
        from Login import Login   #登陆发文章
        self.Login=Login(self.ui)

        QtCore.QObject.connect(self.ui.blog_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Login.fb_wz) #发布文章
        QtCore.QObject.connect(self.ui.Login_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Login.long) #登陆
        QtCore.QObject.connect(self.ui.cs_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.sc_data.cs_pushButton) #生成文章
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.bc_txt) #保存文章
        QtCore.QObject.connect(self.ui.avr_list1_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals1) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list2_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals2) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list3_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals3) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list4_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals4) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list5_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals5) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list6_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals6) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list7_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals7) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list8_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals8) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list9_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals9) #读取文件路径
        QtCore.QObject.connect(self.ui.avr_list10_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.avr_list_pals10) #读取文件路径

        QtCore.QObject.connect(self.ui.wz_list1_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.wz_list_pals1) #读取文件路径
        QtCore.QObject.connect(self.ui.wz_list2_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.wz_list_pals2) #读取文件路径
        QtCore.QObject.connect(self.ui.wz_list3_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.wz_list_pals3) #读取文件路径
        QtCore.QObject.connect(self.ui.wz_list4_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.wz_list_pals4) #读取文件路径
        QtCore.QObject.connect(self.ui.wz_list5_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.text.wz_list_pals5) #读取文件路径


    def open_txt(self,name):  #打开文件
        try:
            xxx = file(name, 'r')
            return xxx.read()
        except Exception, e:
            return ""

    def write2file(self, name, data):
        # 写入文本
        try:
            file_object = open(name, 'w')
            file_object.writelines(data)
            #file_object.writelines("\r\n")
            file_object.close()
        except Exception, e:
            return ""

    def bc_txt(self):  #保存文本
        try:
            Title_data=self.ui.Title_textEdit.toPlainText() #获取内容
            self.write2file("Title.txt",Title_data)
            Content_data=self.ui.Content_textEdit.toPlainText() #获取内容
            self.write2file("Content.txt",Content_data)

            self.xr_ini("DATA","avr_list1",self.ui.avr_list1_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list2",self.ui.avr_list2_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list3",self.ui.avr_list3_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list4",self.ui.avr_list4_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list5",self.ui.avr_list5_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list6",self.ui.avr_list6_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list7",self.ui.avr_list7_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list8",self.ui.avr_list8_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list9",self.ui.avr_list9_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","avr_list10",self.ui.avr_list10_textEdit.toPlainText())   #获取内容

            self.xr_ini("DATA","wz_list1",self.ui.wz_list1_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","wz_list2",self.ui.wz_list2_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","wz_list3",self.ui.wz_list3_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","wz_list4",self.ui.wz_list4_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","wz_list5",self.ui.wz_list5_textEdit.toPlainText())   #获取内容

            self.xr_ini("DATA","username",self.ui.username_textEdit.toPlainText())   #获取内容
            self.xr_ini("DATA","password",self.ui.password_textEdit.toPlainText())   #获取内容
            self.ui.messagebox.append(u"保存配置信息成功")
        except:
            pass

    def xr_ini(self,name1,name2,data):  #写入INI
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("main.ini"))
            config.set(str(name1),str(name2),str(data))  #写入配置
            config.write(open("main.ini", "w"))  #保存配置
        except:
            pass

    def ini_data(self): #初始化数据
        try:
            try:
                config = ConfigParser.ConfigParser()
                config.readfp(open("main.ini"))
                avr_list = str(config.get("DATA", "avr_list1"))
                self.ui.avr_list1_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list2"))
                self.ui.avr_list2_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list3"))
                self.ui.avr_list3_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list4"))
                self.ui.avr_list4_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list5"))
                self.ui.avr_list5_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list6"))
                self.ui.avr_list6_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list7"))
                self.ui.avr_list7_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list8"))
                self.ui.avr_list8_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list9"))
                self.ui.avr_list9_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "avr_list10"))
                self.ui.avr_list10_textEdit.setText(u"%s"%(avr_list))

                avr_list = str(config.get("DATA", "wz_list1"))
                self.ui.wz_list1_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "wz_list2"))
                self.ui.wz_list2_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "wz_list3"))
                self.ui.wz_list3_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "wz_list4"))
                self.ui.wz_list4_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "wz_list5"))
                self.ui.wz_list5_textEdit.setText(u"%s"%(avr_list))

                avr_list = str(config.get("DATA", "username"))
                self.ui.username_textEdit.setText(u"%s"%(avr_list))
                avr_list = str(config.get("DATA", "password"))
                self.ui.password_textEdit.setText(u"%s"%(avr_list))
            except:
                pass
            try:
                php_data=self.open_txt("Title.txt")
                if len(php_data)>=1:
                    data=u"%s"%(php_data)
                    self.ui.Title_textEdit.setText(data)
                else:
                    self.ui.Title_textEdit.setText(u"{avr_list1}█微信:fangliang114 QQ:120275151█{avr_list1}")
            except:
                pass
            try:
                php_data=self.open_txt("Content.txt")
                if len(php_data)>=1:
                    data=u"%s"%(php_data)
                    self.ui.Content_textEdit.setText(data)
                else:
                    self.ui.Content_textEdit.setText(u"{avr_list1}\r\n  {avr_list1}{wz_list1}\r\n{avr_list2}{wz_list2}\r\n{avr_list3}{wz_list3}\r\n{avr_list4}{wz_list4}\r\n{avr_list5}{wz_list5}\r\n{avr_list6}\r\n{avr_list7}\r\n{avr_list8}\r\n{avr_list9}\r\n{avr_list10}")
            except:
                pass
        except:
            pass



import time
from PyQt4 import QtCore, QtGui ,QtNetwork
from PyQt4.QtCore import *
#from ctypes import *
from PyQt4.QtGui import *
#import QtNetwork
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #lang = QtCore.QTranslator()
    #lang.load("qt_zh_CN.qm")
    #app.installTranslator(lang)#载入中文字体需要从qt安装目录里复制PyQt4\translations\qt_zh_CN.qm
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())


