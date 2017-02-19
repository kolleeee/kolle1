#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
from UImain import *
import ConfigParser  #INI读取数据
import urllib2, re, time
import thread
from ctypes import *
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库

import socket
socket.setdefaulttimeout(10)

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
        self.zhonggong = 0
        self.baidu = 0
        self.google = 0
        self.bing = 0
        self.so360 = 0
        self.sogou = 0
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        self.setWindowTitle(u'闪客库—中国第一大社工网站---社工库-----------在线查询   WEB接口Acn提供  exe编写FreebuF薛薛')  #设置标题
        self.ui.textEdit_3.setText(u"闪客库—中国第一大社工网站---社工库-----------在线查询   WEB接口Acn提供  exe编写FreebuF薛薛")  #URL
        self.ui.textEdit.setEnabled(0)  #给改成禁用
        self.ini_set() #
        #-------------------------------------
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button)  #按钮
        QtCore.QObject.connect(self.ui.tableView,QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.SJIndex)   #双击事件
        self.tab2_tableView_count(0)  #设置tableView属性  行数

    def tab2_tableView_count(self,h):  #设置tableView属性  行数
        try:
            self.model = QStandardItemModel()
            self.model.setColumnCount(3)     #列
            self.model.setRowCount(h)  #行  len(node)
            self.model.setHorizontalHeaderLabels([u'账号',u'密码',u'邮箱',u'数据来源'])
            self.ui.tableView.setModel(self.model)
            #self.ui.tableView.resizeColumnsToContents()   #由内容调整列
            self.ui.tableView.setColumnWidth(0,200)  #设置表格的各列的宽度值
            self.ui.tableView.setColumnWidth(1,200)  #设置表格的各列的宽度值
            self.ui.tableView.setColumnWidth(2,200)  #设置表格的各列的宽度值
            self.ui.tableView.setColumnWidth(3,140)  #设置表格的各列的宽度值
            for i in range(h):  #调整行高度  len(node)
                self.ui.tableView.setRowHeight(i, 20)
            self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
            self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
            self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
            self.ui.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）

        except BaseException, e:
            print(str(e))
            pass

    def SJIndex(self):  #双击事件
        try:
            index=self.ui.tableView.currentIndex().row()  #可以使用这个获取当前选择行
            print index
            model = self.ui.tableView.model()
            s0=model.data(model.index(index,0)).toString()
            s1=model.data(model.index(index,1)).toString()
            s2=model.data(model.index(index,2)).toString()
            s3=model.data(model.index(index,3)).toString()
            data=u"账号:%s密码:%s邮箱:%s数据来源:%s"%(s0,s1,s2,s3)
            self.ui.textEdit_3.setText(data)  #URL
        except BaseException, e:
            self.ui.textEdit_3.setText(u"读取失败")  #URL

    def Button(self):
        try:
            a1=self.ui.textEdit.toPlainText() #获取
            a2=self.ui.textEdit_2.toPlainText() #获取
            url="%s%s"%(a1,a2)
            self.ui.textEdit_3.setText(u"正在获取内容请等待！！！！！！！！！！！")  #URL
            self.tab2_tableView_count(0) #设置tableView属性  行数
            data=self.open_url_data(url)
            if data==0:  #读取网页内容
                self.ui.textEdit_3.setText(u"获取网页内容失败")  #URL
                time.sleep(2)
                return 0
            p1 = re.compile(r'<tr>(.+?)</tr>')  #获取大的
            p2 = re.compile(r'<td>(.+?)</td>')  #获取大的
            data=data.replace("\n", '')  #去除换行符好匹配
            IISWEB = p1.findall(data)#
            i=0
            for every1 in IISWEB:#
                IISWEB2 = p2.findall(every1)#
                if len(IISWEB2)==4:
                    self.tableView_add(i,str(IISWEB2[0]).decode('gbk'),str(IISWEB2[1]),str(IISWEB2[2]),str(IISWEB2[3]).decode('gbk'))  #添加数据
                    i+=1
        except BaseException, e:
            print "222222"
            print(str(e))
            pass

            #添加数据
    def tableView_add(self,ints,s0,s1,s2,s3):  #添加数据
        try:
            if not s0==None:
                self.model.setItem(ints, 0, QStandardItem(s0))
            if not s1==None:
                self.model.setItem(ints, 1, QStandardItem(s1))
            if not s2==None:
                self.model.setItem(ints, 2, QStandardItem(s2))
            if not s3==None:
                self.model.setItem(ints, 3, QStandardItem(s3))
            self.ui.tableView.setModel(self.model)
        except:
            pass

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            #req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            #req.add_header('User-Agent','userAgentIE9')
            req.add_header('User-Agent','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)')
            #req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def ini_set(self): #
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("server.ini"))
            URL = config.get("DATA","URL")  #测试上传文件
            self.ui.textEdit.setText(URL)  #URL
        except:
            self.ui.textEdit.setText(u"读取server.ini 配置信息失败")  #URL

import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #lang = QtCore.QTranslator()
    #lang.load("qt_zh_CN.qm")
    #app.installTranslator(lang)#载入中文字体需要从qt安装目录里复制PyQt4\translations\qt_zh_CN.qm
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())

