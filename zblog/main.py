#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

from UIzblog import *
import ConfigParser  #INI读取数据
import urllib2, re, time
import thread
import random #抽取随机数
from ctypes import *
#import win32ui
#user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
import base64
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
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.s0=[]   #标题
        self.s1=[]   #别名
        self.s2=[]   #正文
        self.s3=[]   #链接

        self.p1=[]   #评论 用户名
        self.p2=[]   #评论 内容

        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        self.ui.textEdit.setText("time.txt")  #标题
        self.ui.textEdit_2.setText("time.txt")  #别名
        self.ui.textEdit_3.setText("wz.txt")  #正文
        self.ui.textEdit_9.setText("lj.txt")  #链接
        self.ui.textEdit_4.setText("2")  #几篇文章

        self.ui.textEdit_5.setText("admin.txt")  #用户名
        self.ui.textEdit_6.setText("wz.txt")  #内容
        self.ui.textEdit_7.setText("5")  #评论数
        self.ui.textEdit_8.setText("3")  #留言数
        #-------------------------------------
        self.model = QStandardItemModel()
        self.model.setColumnCount(0)     #列
        self.model.setRowCount(0)  #行  len(node)
        self.model.setHorizontalHeaderLabels([u'URL',u'状态'])
        self.ui.tableView.setModel(self.model)
        #self.ui.tableView.resizeColumnsToContents()   #由内容调整列
        self.ui.tableView.setColumnWidth(0,500)  #设置表格的各列的宽度值
        self.ui.tableView.setColumnWidth(1,130)  #设置表格的各列的宽度值
        for i in range(0):  #调整行高度  len(node)
            self.ui.tableView.setRowHeight(i,20)
        self.ui.tableView.setEditTriggers(QTableWidget.NoEditTriggers)  #设置表格的单元为只读属性，即不能编辑
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectRows) #点击选择是选择行//设置选中时为整行选中
        self.ui.tableView.setAlternatingRowColors(True)  #还是只可以选择单行（单列）
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button) #标题
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button2) #别名
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button3) #正文
        QtCore.QObject.connect(self.ui.pushButton_9,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button9) #链接

        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button4) #开始发布

        QtCore.QObject.connect(self.ui.pushButton_5,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button5) #用户名
        QtCore.QObject.connect(self.ui.pushButton_6,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button6) #内容

        QtCore.QObject.connect(self.ui.pushButton_7,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button7) #开始发布评论
        QtCore.QObject.connect(self.ui.pushButton_8,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button8) #开始发布留言
        self.dl_file()  #导入文件

    def Button8(self):  #开始发布留言
        try:
            if len(self.p1)<=1:
                file_name1=self.ui.textEdit_5.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择用户名文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.p1,file_name1)  #把文件导入到数组里
            if len(self.p2)<=1:
                file_name2=self.ui.textEdit_6.toPlainText() #
                if file_name2=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择内容文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.p2,file_name2)  #把文件导入到数组里
            int_model = self.ui.tableView.selectionModel()  #获取选中编号
            int_id=0
            for index in int_model.selectedRows():       #// 对于被选中的每一行
                int_id+=1
            if int_id<1:
                user32.MessageBoxW(0,c_wchar_p(u"提示:请选择要更新的URL"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                return 0
            ps=self.ui.textEdit_8.toPlainText()
            if int(ps)<1: #
                user32.MessageBoxW(0,c_wchar_p(u"提示:更新留言数少于1"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                return 0
            thread.start_new_thread(self.BLOG_LY,(int(ps),))  #更新留言
        except:
            pass

    def BLOG_LY(self,IX):
        try:
            int_model = self.ui.tableView.selectionModel()  #获取选中编号
            model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in int_model.selectedRows():       #// 对于被选中的每一行
                int_index=index.row()#获取行号
                sA= model.data(model.index(int_index,0)).toString()
                for i in range(IX):
                    try:
                        as1=base64.b64encode(self.p1[random.randint(0,len(self.p1))])
                        as2=base64.b64encode(self.p2[random.randint(0,len(self.p2))])
                        url="%s&ly=1&s1=%s&s2=%s"%(sA,as1,as2)
                        #print url
                        if self.open_url3(url):  #提交参数
                            self.tableView_add(int_index,None,u"更新留言成功")  #添加数据
                        else:
                            self.tableView_add(int_index,None,u"更新留言失败")  #添加数据
                            self.tableView_RGB(int_index)  #RGB
                        time.sleep(0.3)
                    except:
                        time.sleep(0.5)
                        pass
        except BaseException, e:
            print(str(e))
            return 0

    def Button7(self):  #开始发布评论
        try:
            if len(self.p1)<=1:
                file_name1=self.ui.textEdit_5.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择用户名文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.p1,file_name1)  #把文件导入到数组里
            if len(self.p2)<=1:
                file_name2=self.ui.textEdit_6.toPlainText() #
                if file_name2=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择内容文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.p2,file_name2)  #把文件导入到数组里
            int_model = self.ui.tableView.selectionModel()  #获取选中编号
            int_id=0
            for index in int_model.selectedRows():       #// 对于被选中的每一行
                int_id+=1
            if int_id<1:
                user32.MessageBoxW(0,c_wchar_p(u"提示:请选择要更新的URL"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                return 0
            ps=self.ui.textEdit_7.toPlainText()
            if int(ps)<1: #
                user32.MessageBoxW(0,c_wchar_p(u"提示:更新评论数少于1"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                return 0
            thread.start_new_thread(self.WZ_PL,(int(ps),))  #更新文章评论
        except:
            pass

    def WZ_PL(self,IX):
        try:
            int_model = self.ui.tableView.selectionModel()  #获取选中编号
            model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in int_model.selectedRows():       #// 对于被选中的每一行
                int_index=index.row()#获取行号
                sA= model.data(model.index(int_index,0)).toString()
                for i in range(IX):
                    try:
                        as1=base64.b64encode(self.p1[random.randint(0,len(self.p1))])
                        as2=base64.b64encode(self.p2[random.randint(0,len(self.p2))])
                        url="%s&pl=1&s1=%s&s2=%s"%(sA,as1,as2)
                        #print url
                        if self.open_url2(url):  #提交参数
                            self.tableView_add(int_index,None,u"更新评论成功")  #添加数据
                        else:
                            self.tableView_add(int_index,None,u"更新评论失败")  #添加数据
                            self.tableView_RGB(int_index)  #RGB
                        time.sleep(0.3)
                    except:
                        time.sleep(0.5)
                        pass
        except BaseException, e:
            print(str(e))
            return 0

    def lis(self,ls,file_name):  #把文件导入到数组里
        try:
            xxx = file(file_name, 'r')
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n') #urllib.quote(
                    #data.replace(""," ")  #替换空格
                    if data!="":
                        ls.append(data.decode('gbk'))  #添加数据
                except:
                    pass
        except:
            user32.MessageBoxW(0,c_wchar_p(u"导入 url.txt 文件失败"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
            pass

    def Button4(self):  #开始发布  文章
        try:
            #print self.s0[random.randint(0,len(self.s0))]
            if len(self.s0)<=1:
                file_name0=self.ui.textEdit.toPlainText() #
                if file_name0=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择标题文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.s0,file_name0)  #把文件导入到数组里
            if len(self.s1)<=1:
                file_name1=self.ui.textEdit_2.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择别名文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.s1,file_name1)  #把文件导入到数组里
            if len(self.s2)<=1:
                file_name2=self.ui.textEdit_3.toPlainText() #
                if file_name2=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择正文文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.s2,file_name2)  #把文件导入到数组里
            if len(self.s3)<=1:
                file_name3=self.ui.textEdit_9.toPlainText() #
                if file_name3=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择链接文件"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                self.lis(self.s3,file_name3)  #把文件导入到数组里
            int_model = self.ui.tableView.selectionModel()  #获取选中编号
            int_id=0
            for index in int_model.selectedRows():       #// 对于被选中的每一行
                int_id+=1
            if int_id<1:
                user32.MessageBoxW(0,c_wchar_p(u"提示:请选择要更新的URL"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                return 0
            ps=self.ui.textEdit_4.toPlainText()
            if int(ps)<1: #
                user32.MessageBoxW(0,c_wchar_p(u"提示:更新文章篇数少于1"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
                return 0
            thread.start_new_thread(self.GX_wz,(int(ps),))  #更新文章
        except:
            return 0

    def open_url3(self,URL):  #提交参数
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            #print ss
            if "oksqlite3ly" in ss:
                return 1
            return 0
        except:
            return 0
            pass

    def open_url2(self,URL):  #提交参数
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            #print ss
            if "oksqlite3pl" in ss:
                return 1
            return 0
        except:
            return 0
            pass

    def open_url1(self,URL):  #提交参数
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            #print ss
            if "oksqlite3wz" in ss:
                return 1
            return 0
        except:
            return 0
            pass

    def GX_wz(self,IX):
        try:
            int_model = self.ui.tableView.selectionModel()  #获取选中编号
            model = self.ui.tableView.model()#index = model.index(3,1)#data = model.data(index)#print data.toString()
            for index in int_model.selectedRows():       #// 对于被选中的每一行
                int_index=index.row()#获取行号
                sA= model.data(model.index(int_index,0)).toString()
                for i in range(IX):
                    try:
                        as0=base64.b64encode(self.s0[random.randint(0,len(self.s0))])
                        as1=base64.b64encode(self.s1[random.randint(0,len(self.s1))])
                        ak47="%s%s"%(self.s2[random.randint(0,len(self.s2))],self.s3[random.randint(0,len(self.s3))])
                        as2=base64.b64encode(ak47)

                        url="%s&wz=1&s0=%s&s1=%s&s2=%s"%(sA,as0,as1,as2)
                        if self.open_url1(url):  #提交参数
                            self.tableView_add(int_index,None,u"更新文章成功")  #添加数据
                        else:
                            self.tableView_add(int_index,None,u"更新文章失败")  #添加数据
                            self.tableView_RGB(int_index)  #RGB
                        time.sleep(0.3)
                    except:
                        time.sleep(0.5)
                        pass
        except BaseException, e:
            print(str(e))
            return 0

    def Button6(self):
        try:
            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            fname = dlg.GetPathName() # 获取选择的文件名称
            self.ui.textEdit_6.setText(fname.decode('gbk'))  #转化下防止中文路径
        except:
            return 0

    def Button5(self):
        try:
            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            fname = dlg.GetPathName() # 获取选择的文件名称
            self.ui.textEdit_5.setText(fname.decode('gbk'))  #转化下防止中文路径
        except:
            return 0

    def Button9(self):
        try:
            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            fname = dlg.GetPathName() # 获取选择的文件名称
            self.ui.textEdit_9.setText(fname.decode('gbk'))  #转化下防止中文路径
        except:
            return 0

    def Button3(self):
        try:
            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            fname = dlg.GetPathName() # 获取选择的文件名称
            self.ui.textEdit_3.setText(fname.decode('gbk'))  #转化下防止中文路径
        except:
            return 0

    def Button2(self):
        try:
            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            fname = dlg.GetPathName() # 获取选择的文件名称
            self.ui.textEdit_2.setText(fname.decode('gbk'))  #转化下防止中文路径
        except:
            return 0

    def Button(self):
        try:
            dlg = win32ui.CreateFileDialog(1, "*.txt", None, 0, u"txt 文本 (*.txt)|*.txt|All files|*.*")
            #dlg.SetOFNInitialDir('E:/Python') # 设置打开文件对话框中的初始显示目录
            dlg.DoModal()
            fname = dlg.GetPathName() # 获取选择的文件名称
            self.ui.textEdit.setText(fname.decode('gbk'))  #转化下防止中文路径
        except:
            return 0

    #RGB
    def tableView_RGB(self,ints):  #RGB
        try:
            self.model.item(ints,0).setBackground(QColor(255,0,0))#//改变背景色
            self.model.item(ints,1).setBackground(QColor(255,0,0))#//改变背景色
            #self.model.item(ints,1).setForeground(QBrush(QColor(210,105,30 )))  #//设置字符颜色

            self.ui.tableView.setModel(self.model)
        except:
            pass

    #添加数据
    def tableView_add(self,ints,s0,s1):  #添加数据
        try:
            if not s0==None:
                self.model.setItem(ints, 0, QStandardItem(s0))
            if not s1==None:
                self.model.setItem(ints, 1, QStandardItem(s1))
            self.ui.tableView.setModel(self.model)
        except:
            pass

    def dl_file(self):  #导入文件
        try:
            xxx = file("url.txt", 'r')
            i=0
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n') #urllib.quote(
                    if data!="":
                        self.tableView_add(i,data,None)  #添加数据
                except:
                    pass
                i+=1
        except:
            user32.MessageBoxW(0,c_wchar_p(u"导入 url.txt 文件失败"), c_wchar_p(u"神马站群"), 0)   # 调用MessageBoxA函数
            pass

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

