#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#requests 模拟提交表单登陆DZ BBS  发帖  回帖 QQ29295842
################################################
from dz_bbsui import *

from ctypes import *
#import win32ui
user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
import thread
import random #抽取随机数
#user32.MessageBoxW(0,c_wchar_p("1111111"), c_wchar_p("QQ:29295842"), 0)   # 调用MessageBoxA函数
import mechanize
import re, time
#                time.sleep(time1)
import sys
reload(sys)
import socket
socket.setdefaulttimeout(10)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Start(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()

        self.s8=[]   #标题：
        self.s9=[]   #内容：
        self.s10=[]   #链接：

        self.s12=[]   #评论：
        self.s13=[]   #链接：

        self.ui.setupUi(self)
        #-------------------------------
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)   # no robots
        self.br.set_handle_refresh(False)  # can sometimes hang without this
        self.br.set_handle_equiv(True)
        #br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        #-------------------------------
        #http://www.cnblogs.com/caomingongli/archive/2011/09/19/2181842.html    这个不错   PyQt之自定义无边框窗口遮盖任务栏显示问题
        flags = 0  #设置禁止最大化
        flags|= Qt.WindowMinimizeButtonHint  #设置禁止最大化
        self.setWindowFlags(flags)  #设置禁止最大化
        self.setWindowTitle(u'discuzX BBS  批量/群发/发帖/回帖  V:0.1  QQ:29295842   BY:神龙')  #设置标题
        self.messbx(u'discuzX BBS  批量/群发/发帖/回帖  V:0.1  QQ:29295842  BY:神龙')
        #self.ini() #初始化
        self.ui.textEdit.setText("http://www.laiwusheying.com/forum.php")  #登陆网址
        self.ui.textEdit_2.setText("sunfeng27")  #用户名
        self.ui.textEdit_3.setText("sunfeng")  #密码
        self.ui.textEdit_4.setText(u"用户组")  #登陆成功\n关键字：
        self.ui.textEdit_5.setText("http://www.laiwusheying.com/forum.php?mod=post&action=newthread&fid=18")  #批量发\n布帖子：
        self.ui.textEdit_15.setText("3")  #发布帖子数量
        self.ui.textEdit_6.setText("http://www.laiwusheying.com/forum.php?mod=forumdisplay&fid=18")  #批量发\n布评论：
        self.ui.textEdit_16.setText("5")  #发布评论数量
        self.ui.textEdit_7.setText("130")  #延时\n秒/S：
        #帖子/随机抽取/一行一条
        self.ui.textEdit_8.setText("title.txt")  #标题：
        self.ui.textEdit_9.setText("nr.txt")  #内容：
        self.ui.textEdit_10.setText("lj.txt")  #链接：
        self.ui.textEdit_11.setText("5")  #内容插入\n链接条数：
        #评论/随机抽取/一行一条
        self.ui.textEdit_12.setText("nr.txt")  #评论：
        self.ui.textEdit_13.setText("lj.txt")  #链接：
        self.ui.textEdit_14.setText("3")  #评论插入\n链接条数：
        #事件处理
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button)  #登陆网站
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button_2)  #发布帖子
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL(_fromUtf8("clicked()")),self.Button_3)  #回帖子
        ##########################

    def Button_3(self):    #回帖子
        try:
            if len(self.s12)<=1:  #评论：
                file_name1=self.ui.textEdit_12.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择评论文件"), c_wchar_p(u"QQ:29295842"), 0)   # 调用MessageBoxA函数
                self.lis(self.s12,file_name1)  #把文件导入到数组里
            if len(self.s13)<=1:  #链接：
                file_name1=self.ui.textEdit_13.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择链接文件"), c_wchar_p(u"QQ:29295842"), 0)   # 调用MessageBoxA函数
                self.lis(self.s13,file_name1)  #把文件导入到数组里
            url=self.ui.textEdit_6.toPlainText()    #批量发\n布评论：
            sl=self.ui.textEdit_16.toPlainText()    #发布评论数量
            time1=self.ui.textEdit_7.toPlainText()    #延时\n秒/S：
            thread.start_new_thread(self.bbs_pinglun,(str(url),int(sl),int(time1),))  #更新文章评论
        except BaseException, e:
            print(str(e))
            self.messbx(u'回帖异常')
            pass

    def bbs_sed_message(self,url):  #回帖
        try:
            self.br.open(url)
            #for f in br.forms():##有的页面有很多表单，你可以通过来查看
            #    print f
            data=self.s12[random.randint(0,len(self.s12))]
            SL=self.ui.textEdit_14.toPlainText()    #内容插入\n链接条数：
            aa=self.file_data(int(SL),data)   #内容附加外链
            self.br.select_form(nr=2)##选择表单1，
            self.br.form['message'] = aa.decode('utf8').encode('gbk')
            response = self.br.submit()
            #print response.read().decode('gbk')
            if response.read().decode('gbk').find(u'回帖后跳转到最后一页')>-1:
                self.messbx(u'%s--回帖成功'%url)
            else:
                self.messbx(u'%s--回帖失败'%url)
        except BaseException, e:
            print(str(e))
            pass

    def bbs_pinglun(self,url,sl,time1):  #更新文章评论
        try:
            response=self.br.open(url)
            data=response.read().decode('gbk')
            #print data
            #p = re.compile(r'<th class=\"common\">(.+?)</th>')
            p = re.compile( r'<a href=\"(.*?)\" onclick=\"atarget\(this\)\" class=\"s xst\">')
            #data=data.replace("\n", '')  #去除换行符好匹配
            sarr = p.findall(data)
            url=self.URL_TQURL(url) #URL提取URL
            i=0
            for every in sarr:
                if i<=sl:
                    url2="%s%s"%(url,every)
                    #print url2
                    self.bbs_sed_message(url2)  #回帖
                    i+=1
                    time.sleep(time1)
        except BaseException, e:
            print(str(e))
            self.messbx(u'回帖异常')
            pass

    def Button_2(self):  #发布帖子
        try:
            if len(self.s8)<=1:  #标题：
                file_name1=self.ui.textEdit_8.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择标题文件"), c_wchar_p(u"QQ:29295842"), 0)   # 调用MessageBoxA函数
                self.lis(self.s8,file_name1)  #把文件导入到数组里
            if len(self.s9)<=1:  #内容：
                file_name1=self.ui.textEdit_9.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择内容文件"), c_wchar_p(u"QQ:29295842"), 0)   # 调用MessageBoxA函数
                self.lis(self.s9,file_name1)  #把文件导入到数组里
            if len(self.s10)<=1:  #链接：
                file_name1=self.ui.textEdit_10.toPlainText() #
                if file_name1=="":
                    user32.MessageBoxW(0,c_wchar_p(u"请选择链接文件"), c_wchar_p(u"QQ:29295842"), 0)   # 调用MessageBoxA函数
                self.lis(self.s10,file_name1)  #把文件导入到数组里
            url=self.ui.textEdit_5.toPlainText()
            time1=self.ui.textEdit_7.toPlainText()
            sl=self.ui.textEdit_15.toPlainText()    #发布帖子数量
            thread.start_new_thread(self.bbs_fatie,(str(url),int(sl),int(time1),))  #更新文章评论
        except BaseException, e:
            print(str(e))
            self.messbx(u'发布帖子异常')
            pass

    def URL_TQURL(self,url): #URL提取URL
        try:
            #查看字符串结尾是否是/是就直接返回  http://www.383k.com/bbs/
            data=url[len(url)-1:len(url)]
            if data=="/":
                return url
                #截取字符串 http://www.383k.com/bbs/forum-4-1.html   http://www.383k.com/bbs/
            nPos =url.rfind('/') #查找字符  从尾部查找
            sStr1 = url[0:nPos+1] #复制指定长度的字符
            return sStr1
        except:
            pass

    def file_data(self,n,data):   #内容附加外链
        data2=""
        try:
            intn=len(data)/n
            for i in range(n):
            #if len(data)>=intn:
                data2+=data[0:intn]  #复制指定长度的字符
                data2+=self.s10[random.randint(0,len(self.s10))]+" "
                data=data[intn:] #字符串删除
            return data2
        except BaseException, e:
            print(str(e))
            return data2

    def bbs_fatie(self,url,sl,time1):  #发帖
        try:
            for i in range(sl):
                name=self.s8[random.randint(0,len(self.s8))]
                data=self.s9[random.randint(0,len(self.s9))]
                SL=self.ui.textEdit_11.toPlainText()    #内容插入\n链接条数：
                aa=self.file_data(int(SL),data)   #内容附加外链
                print aa
                self.br.open(url)
#                for frm in self.br.forms():##有的页面有很多表单，你可以通过来查看
#                    print frm
#                    print frm.attrs["id"]=="postform"
                try:
                    formcount=0
                    for frm in self.br.forms():
                        if str(frm.attrs["id"])=="postform":
                            break
                        formcount=formcount+1
                    self.br.select_form(nr=formcount)
                    #self.br.select_form(nr=0)##选择表单1，
                    self.br.form['subject'] = name.decode('utf8').encode('gbk')
                    self.br.form['message'] = aa.decode('utf8').encode('gbk')
                except:
                    pass
                response = self.br.submit()  #提交表单
                data=response.read().decode('gbk')
                #print data
                #thread_url: 'http://bbs.sandaha.com/thread-291356-1-1.html',    新帖子的位置
                p = re.compile( r'thread_url: \'(.*?)\',' )
                sarr = p.findall(data)
                if str(sarr[0]).find('http')>-1:
                    self.messbx(u'%s--发帖成功'%str(sarr[0]))
                else:
                    self.messbx(u'发帖失败')
                time.sleep(time1)
        except BaseException, e:
            print(str(e))
            self.messbx(u'发布帖子异常')
            pass

    def Button(self):  #登陆网站
        try:
            url=self.ui.textEdit.toPlainText() #
            username=self.ui.textEdit_2.toPlainText() #
            password=self.ui.textEdit_3.toPlainText() #
            key=self.ui.textEdit_4.toPlainText() #
            self.br.open(str(url))  #登陆网址
            self.br.select_form(nr=0)##选择表单1，
            self.br.form['username'] = str(username)
            self.br.form['password'] = str(password)
            response = self.br.submit()  ##提交表单
            #print response.read().decode('gbk')
            if response.read().decode('gbk').find(str(key))>-1:
                self.messbx(u'%s--登录成功'%str(url))
            else:
                self.messbx(u'%s--登录失败'%str(url))
        except BaseException, e:
            print(str(e))
            self.messbx(u'登录异常')
            pass

    def lis(self,ls,file_name):  #把文件导入到数组里
        try:
            xxx = file(file_name, 'r')
            for xxx_line in xxx.readlines():
                try:
                    data=xxx_line.strip().lstrip().rstrip('\n') #urllib.quote(
                    #data.replace(""," ")  #替换空格
                    if len(data)>4:
                        ls.append(data.decode('gbk'))  #添加数据
                except:
                    pass
        except:
            pass

    def messbx(self,data):
        self.ui.messagebox.append(data)

import time
from PyQt4 import QtCore, QtGui ,QtNetwork
from PyQt4.QtCore import *
from ctypes import *
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
