#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from ui import *
import time
from PyQt4 import QtCore, QtGui ,QtNetwork
from PyQt4.QtCore import *
from ctypes import *
from PyQt4.QtGui import *
#import QtNetwork
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import url_cms_QTX  #CMS指纹识别

#import win32ui
#user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Start(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        self.ini() #初始化

        self.threads0 = url_cms_QTX.url_cms_QTX(self.ui,self.model)   #CMS指纹识别
        self.threads0.start()

    #初始化
    def ini(self): #初始化
        self.setWindowTitle(u'CMS(KEY关键字--文件MD5)指纹识别  本程序采用单线程识别  V:1.0  BY:神龙  农民工写代码  http://www.hacked90.com/')  #设置标题
        self.model = QStandardItemModel()
        self.model.setColumnCount(4)     #列
        self.model.setRowCount(0)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'URL地址',u'CMS名称',u'识别方式',u'URL链接文件(地址)',u'关键字KEY or 文件MD5'])
        self.ui.tableView_1.setModel(self.model)
        self.ui.tableView_1.setColumnWidth(0,120)  #设置表格的各列的宽度值
        self.ui.tableView_1.setColumnWidth(1,80)  #设置表格的各列的宽度值
        self.ui.tableView_1.setColumnWidth(2,60)  #设置表格的各列的宽度值
        self.ui.tableView_1.setColumnWidth(3,150)  #设置表格的各列的宽度值
        self.ui.tableView_1.setColumnWidth(4,200)  #设置表格的各列的宽度值
        for i in range(0):  #调整行高度  len(node)
            self.ui.tableView_1.setRowHeight(i, 20)
        self.ui.tableView_1.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.ui.tableView_1.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        self.ui.tableView_1.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.ui.tableView_1.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        #self.ui.tableView_1.verticalHeader().hide() #隐藏行头
        #self.ui.messagebox_textEdit.setEnabled(0)  #给改成禁用
        self.ui.messagebox_textEdit.append(u"CMS(KEY关键字--文件MD5)\n指纹识别  V:1.0 \nTIME:%s"%(time.strftime('%Y.%m.%d-%H.%M.%S')))
        self.ui.webView.setUrl(QtCore.QUrl("http://hi.baidu.com/alalmn"))
        self.ui.progressBar.setValue(0)  #设置进度

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #lang = QtCore.QTranslator()
    #lang.load("qt_zh_CN.qm")
    #app.installTranslator(lang)#载入中文字体需要从qt安装目录里复制PyQt4\translations\qt_zh_CN.qm
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())

