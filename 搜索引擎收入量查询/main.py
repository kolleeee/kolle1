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
        self.setWindowTitle(u'神马站群 搜索引擎收入量查询工具V0.1  SEO技术、站群交流 QQ群：40518379    BY:小龙')  #设置标题
        #-------------------------------------
        self.model = QStandardItemModel()
        self.model.setColumnCount(3)     #列
        self.model.setRowCount(0)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'查询内容',u'www.baidu.com',u'www.google.com.hk',u'cn.bing.com',u'so.360.cn',u'www.sogou.com'])
        self.ui.tableView.setModel(self.model)
        #self.ui.tableView.resizeColumnsToContents()   #由内容调整列
        self.ui.tableView.setColumnWidth(0,270)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(1,110)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(2,140)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(3,90)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(4,70)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(5,110)  #设置表格的各列的宽度值
        for i in range(0):  #调整行高度  len(node)
            self.ui.tableView.setRowHeight(i, 20)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        self.ui.tableView.setSelectionMode(QTableWidget.SingleSelection)  #禁止多行选择
        self.ui.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        #-------------------------------------
        self.ui.checkBox_2.setEnabled(0)  #给改成禁用
        #                      控件                                                       响应函数
        QtCore.QObject.connect(self.ui.checkBox_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox1)  #复选框
        QtCore.QObject.connect(self.ui.checkBox_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox2)  #复选框
        QtCore.QObject.connect(self.ui.checkBox_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox3)  #复选框
        QtCore.QObject.connect(self.ui.checkBox_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox4)  #复选框
        QtCore.QObject.connect(self.ui.checkBox_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox5)  #复选框

        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button)  #按钮
        QtCore.QObject.connect(self.ui.tableView, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.SJIndex)   #双击事件
        #-------------------------------------
        self.dl_file() #导入文件
        self.ini_get() #初始化


    def SJIndex(self, index):  #双击事件
        try:
            model = self.ui.tableView.model()
            s0=model.data(model.index(index.row(),0)).toString()

            url="http://www.baidu.com/baidu?tn=monline_5_dg&ie=utf-8&wd=%s"%(str(s0))
            os.startfile(str(url))
            time.sleep(0.5)
            url="http://www.google.com.hk/search?q=%s&start=0"%(str(s0))
            os.startfile(str(url))
            time.sleep(0.5)
            url="http://cn.bing.com/search?q=%s&go=&first=0"%(str(s0))
            os.startfile(str(url))
            time.sleep(0.5)
            url="http://www.so.com/s?ie=utf-8&src=360sou_home&q=%s"%(str(s0))
            os.startfile(str(url))
            time.sleep(0.5)
            url="http://www.sogou.com/web?query=%s"%(str(s0))
            os.startfile(str(url))
            time.sleep(0.5)
        except BaseException, e:
            pass

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            #req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            #req.add_header('User-Agent','userAgentIE9')
            req.add_header('User-Agent','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)')
            #req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def url_data_re(self,url):
        try:
            ss=self.open_url_data(url)
            if ss==0:  #读取网页内容
                print u"获取内容失败"
                time.sleep(2)
                return 0
            #print ss
            p = re.compile(r"百度为您找到相关结果约(.*?)个")
            sarr = p.findall(ss)#找出一条百度
            if len(sarr) >0:  #None 也是假。
                return str(sarr[0]).strip().lstrip().replace(',','')

            p = re.compile(r"百度为您找到相关结果(.*?)个")
            sarr = p.findall(ss)#找出一条百度
            if len(sarr) >0:
                return str(sarr[0]).strip().lstrip().replace(',','')
            #=====goog.hk  获取不到数据

            p = re.compile(r'<span class="sb_count" id="count">(.*?)条结果</span>')
            sarr = p.findall(ss)#找出一条bing
            if len(sarr) >0:
                return str(sarr[0]).strip().lstrip().replace(',','')

            p = re.compile(r"找到相关结果约(.*?)个")
            sarr = p.findall(ss)#找出一条so360
            if len(sarr) >0:
                return str(sarr[0]).strip().lstrip().replace(',','')

            p = re.compile(r'找到约 <span id="scd_num">(.*?)</span>')
            sarr = p.findall(ss)#找出一条sogou
            if len(sarr) >0:
                return str(sarr[0]).strip().lstrip().replace(',','')

            return "0"
        except:
            pass

    def Button(self): #按钮
        try:
            self.baidu = 0
            self.google = 0
            self.bing = 0
            self.so360 = 0
            self.sogou = 0
            thread.start_new_thread(self.open_tableView,())  #
#            threads = []  #线程
#            for i in range(int(1)):  #nthreads=10  创建10个线程 int(T_X)
#                threads.append(self.open_tableView())
#            for t in threads:   #不理解这是什么意思    是结束线程吗
#                t.start()  #start就是开始线程
            #print self.url_data_re("http://www.baidu.com/baidu?tn=monline_5_dg&ie=utf-8&wd=12345678","百度为您找到相关结果约(.*?)个")
            #print self.url_data_re("http://www.google.com.hk/search?q=123456&start=0","找到约(.*?)条结果")
            #print self.url_data_re("http://cn.bing.com/search?q=123456&go=&first=0","<span class=\"sb_count\" id=\"count\">(.*?)条结果</span>")
            #print self.url_data_re("http://www.so.com/s?ie=utf-8&src=360sou_home&q=123456","找到相关结果约(.*?)个")
            #print self.url_data_re("http://www.sogou.com/web?query=123456&_asf=www.wumeitehui.com","找到约 <span id=\"scd_num\">(.*?)</span>")
        except ConfigParser.NoOptionError, e:
            user32.MessageBoxW(0,c_wchar_p(u"写入 server.ini 文件读取失败"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
            pass

    def open_tableView(self):   #添加数据到消息队列
#        global baidu,google,bing,so360,sogou
        int_View=self.ui.tableView.model().rowCount()   #获取共多少行
        model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
        for index in range(int_View):
            s0= model.data(model.index(index,0)).toString()
            if self.ui.checkBox_1.isChecked():
                url="http://www.baidu.com/baidu?tn=monline_5_dg&ie=utf-8&wd=%s"%(str(s0))
                sl=self.url_data_re(url)
                self.tableView_add(index,None,sl,None,None,None,None)  #添加数据
                self.baidu += int(sl)
                if int(sl) <=0:
                    self.tableView_RGB(index,"1","0","0","0","0")  #RGB
            else:
                self.tableView_add(index,None,"",None,None,None,None)  #添加数据

            #goog.hk  无法实现self.google += int(sl)
            self.tableView_add(index,None,None,"NULL",None,None,None)  #添加数据
            if self.ui.checkBox_3.isChecked():
                url="http://cn.bing.com/search?q=%s&go=&first=0"%(str(s0))
                sl=self.url_data_re(url)
                self.tableView_add(index,None,None,None,sl,None,None)  #添加数据
                self.bing += int(sl)
                if int(sl) <=0:
                    self.tableView_RGB(index,"0","0","1","0","0")  #RGB
            else:
                self.tableView_add(index,None,None,None,"",None,None)  #添加数据

            if self.ui.checkBox_4.isChecked():
                url="http://www.so.com/s?ie=utf-8&src=360sou_home&q=%s"%(str(s0))
                sl=self.url_data_re(url)
                self.tableView_add(index,None,None,None,None,sl,None)  #添加数据
                self.so360 += int(sl)
                if int(sl) <=0:
                    self.tableView_RGB(index,"0","0","0","1","0")  #RGB
            else:
                self.tableView_add(index,None,None,None,None,"",None)  #添加数据

            if self.ui.checkBox_5.isChecked():
                url="http://www.sogou.com/web?query=%s"%(str(s0))
                sl=self.url_data_re(url)
                self.tableView_add(index,None,None,None,None,None,sl)  #添加数据
                self.sogou += int(sl)
                if int(sl) <=0:
                    self.tableView_RGB(index,"0","0","0","0","1")  #RGB
            else:
                self.tableView_add(index,None,None,None,None,None,"")  #添加数据
            time.sleep(0.5)
            self.label() #更新内容

    def checkBox1(self):  #百度
        if self.ui.checkBox_1.isChecked():
            self.ini_set("baidu","1")
        else:
            self.ini_set("baidu","0")

    def checkBox2(self):  #谷歌
        if self.ui.checkBox_2.isChecked():
            self.ini_set("google","1")
        else:
            self.ini_set("google","0")

    def checkBox3(self):  #微软
        if self.ui.checkBox_3.isChecked():
            self.ini_set("bing","1")
        else:
            self.ini_set("bing","0")

    def checkBox4(self):  #360
        if self.ui.checkBox_4.isChecked():
            self.ini_set("360","1")
        else:
            self.ini_set("360","0")

    def checkBox5(self):  #搜狗
        if self.ui.checkBox_5.isChecked():
            self.ini_set("sogou","1")
        else:
            self.ini_set("sogou","0")

    def ini_set(self,data1,data2): #
        try:
            conf=ConfigParser.ConfigParser()
            CONFIGNAME = 'server.ini'
            if os.path.isfile(CONFIGNAME):
                conf.read(CONFIGNAME)
                conf.sections()
                try:
                    conf.set("DATA",data1,data2)
                    conf.write(open(CONFIGNAME, 'w'))
                except ConfigParser.NoOptionError, e:
                    user32.MessageBoxW(0,c_wchar_p(u"写入 server.ini 文件读取失败"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                    pass
        except:
            user32.MessageBoxW(0,c_wchar_p(u"写入 server.ini 文件读取失败"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
            pass

    def ini_get(self): #初始化
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("server.ini"))
            if int(config.get("DATA","baidu")):
                self.ui.checkBox_1.setChecked( 1 )    #设置复选框为选择状态
            else:
                self.ui.checkBox_1.setChecked( 0 )

            if int(config.get("DATA","google")):
                self.ui.checkBox_2.setChecked( 1 )    #设置复选框为选择状态
            else:
                self.ui.checkBox_2.setChecked( 0 )

            if int(config.get("DATA","bing")):
                self.ui.checkBox_3.setChecked( 1 )    #设置复选框为选择状态
            else:
                self.ui.checkBox_3.setChecked( 0 )

            if int(config.get("DATA","360")):
                self.ui.checkBox_4.setChecked( 1 )    #设置复选框为选择状态
            else:
                self.ui.checkBox_4.setChecked( 0 )

            if int(config.get("DATA","sogou")):
                self.ui.checkBox_5.setChecked( 1 )    #设置复选框为选择状态
            else:
                self.ui.checkBox_5.setChecked( 0 )
        except:
            user32.MessageBoxW(0,c_wchar_p(u"读取 server.ini 文件读取失败"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
            pass

    #RGB
    def tableView_RGB(self,ints,s1,s2,s3,s4,s5):  #RGB
        try:
            if s1=="1":
                self.model.item(ints,1).setBackground(QColor(255,0,0))#//改变背景色
                #self.model.item(ints,1).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色
            if s3=="1":
                self.model.item(ints,3).setBackground(QColor(255,0,0))#//改变背景色
            if s4=="1":
                self.model.item(ints,4).setBackground(QColor(255,0,0))#//改变背景色
            if s5=="1":
                self.model.item(ints,5).setBackground(QColor(255,0,0))#//改变背景色
            self.ui.tableView.setModel(self.model)
        except:
            pass
    #添加数据
    def tableView_add(self,ints,s0,s1,s2,s3,s4,s5):  #添加数据
        try:
            if not s0==None:
                self.model.setItem(ints, 0, QStandardItem(s0))
            if not s1==None:
                self.model.setItem(ints, 1, QStandardItem(s1))
            if not s2==None:
                self.model.setItem(ints, 2, QStandardItem(s2))
            if not s3==None:
                self.model.setItem(ints, 3, QStandardItem(s3))
            if not s4==None:
                self.model.setItem(ints, 4, QStandardItem(s4))
            if not s5==None:
                self.model.setItem(ints, 5, QStandardItem(s5))
            self.ui.tableView.setModel(self.model)
        except:
            pass

    def label(self): #更新内容
        try:
            data4=u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"> \
            查询内容总数:%d--百度收入:%d--谷歌收入:%d--微软收入:%d--360搜索收入:%d--搜狗收入:%d</span></p></body></html>"%(self.zhonggong,self.baidu,self.google,self.bing,self.so360,self.sogou)
            self.ui.label.setText(data4)
        except:
            pass

    def dl_file(self):
        try:
            xxx = file("url.txt", 'r')
            i=0
            for xxx_line in xxx.readlines():
                try:
                    data=urllib.quote(xxx_line.strip().lstrip().rstrip('\n')) #urllib.quote(
                    self.tableView_add(i,data,None,None,None,None,None)  #添加数据
                except:
                    pass
                i+=1
            self.zhonggong = i
            self.label() #更新内容
        except:
            user32.MessageBoxW(0,c_wchar_p(u"导入 url.txt 文件失败"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
            pass

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

