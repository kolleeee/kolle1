#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#生成目录   和文件
##################################################
import os
import sys   #设置默认编码时使用
import time
reload(sys)
sys.setdefaultencoding('utf8')
import base64

def Route(d_url):   #创建目录
    try:
        if not os.path.isdir(str(d_url)):
            os.makedirs(str(d_url)) #创建子目录
            print u"创建文件夹成功",(d_url)
            return 1
    except:
        print u"创建文件夹失败",(d_url)
        return 0
        pass

def wb_file(name,data):  #写入图片
    try:
        if not os.path.exists(name):  #文件不存在就创建
            fout = open(name,'wb')
            fout.write(data)
            fout.close()
            print u"创建图片成功",(name)
    except:
        print u"创建图片失败",(name)
        aurl=mulu(name)
        if aurl:   #获取目录
            if Route(aurl):   #创建目录
                TXT_file2(name,data)  #写入文本 中文
                time.sleep(1)
        pass

def TXT_file(name,data):  #写入文本 中文
    try:
        if not os.path.exists(name):  #文件不存在就创建
            file_object = open(name,'w')
            file_object.write(data) #成功
            #file_object.writelines("\n")
            file_object.close()
            print u"创建文件成功",(name)
    except BaseException,e:
        print u"创建文件失败",(name)
        aurl=mulu(name)
        if aurl:   #获取目录
            if Route(aurl):   #创建目录
                TXT_file2(name,data)  #写入文本 中文
                time.sleep(1)
        pass

def TXT_file2(name,data):  #写入文本 中文
    TXT_file(name,data)  #写入文本 中文

def mulu(ml):   #获取目录
    try:
        nPos =ml.rfind('\\') #查找字符  从尾部查找
        sStr1 = ml[0:nPos] #复制指定长度的字符
        return sStr1
    except BaseException, e:
        print u"获取目录失败",(str(e))
        return 0
        pass

if __name__=='__main__':
    TXT_file("C:\\Users\\Administrator.YKE5DH373UVCX0W\\Desktop\HTML\\69.176.89.5\\wwwroot\\www.123456.com\\index.html","11223344")  #写入文本 中文

