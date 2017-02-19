#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#链接整理器    主要是做灰帽SEO使用的
#挂载链接的时候不知道哪些链接存在哪些不存在 批量整理下  检测网页时候是否存在  提供SEO效果
#自动从存在的链接中  随机组合抽取  组合成要挂载的链接
#落雪技术支持  QQ:2602159946   落雪技术支持  http://2602159946.lofter.com/
from uimain import *

import socket
socket.setdefaulttimeout(10)

from ctypes import *
#import win32ui
import thread
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:23456789"), 0)   # 调用MessageBoxA函数
import ConfigParser  #INI读取数据
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
#        flags = 0  #设置禁止最大化
#        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
#        self.setWindowFlags(flags)  #设置禁止最大化
        #self.setWindowTitle(u'')  #设置标题
        self.ini() #初始化
        config = ConfigParser.ConfigParser()
        config.readfp(open("Server.ini"))
        re_data= str(config.get("Server","re_data"))  #读取配置
        SL= int(config.get("Server","SL"))  #读取配置
        self.ui.re_textEdit.setText(u"%s"%(re_data))
        self.ui.spinBox.setValue(SL)
        data1="""<div id="mydiv" style="position:absolute;display:none;">
友情链接："""
        #print data1
        self.ui.textEdit.insertPlainText(u"%s"%(data1))
        #self.ui.textEdit.setText(u"%s"%(data1))
        data2="""</div>"""
        self.ui.textEdit_2.insertPlainText(u"%s"%(data2))
        #事件处理
        ##########################
        from class_top1 import top_1
        self.top_1=top_1(self.ui,self.model)
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.pushButton1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton1) #导入
        QtCore.QObject.connect(self.ui.SQL_Button_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQL_Button_1) #全部显示
        QtCore.QObject.connect(self.ui.SQL_Button_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQL_Button_2) #显示状态OK
        QtCore.QObject.connect(self.ui.SQL_Button_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.SQL_Button_3) #显示状态NO
        QtCore.QObject.connect(self.ui.RE_Button, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.RE_Button) #查询
        QtCore.QObject.connect(self.ui.pushButton2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton2) #导出数据
        QtCore.QObject.connect(self.ui.pushButton3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton3) #删除数据

        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.top_1.pushButton) #生成链接
    #初始化200
    def ini(self): #初始化
        self.model = QStandardItemModel()
        self.model.setColumnCount(3)     #列
        self.model.setRowCount(0)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'链接地址',u'状态',u'最新操作时间'])
        self.ui.SQLite_tableView.setModel(self.model)
        #self.tableView.resizeColumnsToContents()   #由内容调整列
        self.ui.SQLite_tableView.setColumnWidth(0,610)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(1,50)  #设置表格的各列的宽度值
        self.ui.SQLite_tableView.setColumnWidth(2,170)  #设置表格的各列的宽度值
        for i in range(0):  #调整行高度  len(node)
            self.ui.SQLite_tableView.setRowHeight(i, 20)
        self.ui.SQLite_tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.ui.SQLite_tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        #self.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.ui.SQLite_tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        #self.tableView.verticalHeader().hide() #隐藏行头

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


