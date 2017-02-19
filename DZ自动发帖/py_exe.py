# -*- coding: utf-8 -*-
#windows  #无控制台
#console   #有控制台

from distutils.core import setup

import py2exe
import os


def list_file():
    global  file_list
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                data="%s\%s"%(root,file)
                print data[2:]
                file_list.append(data[2:])  #添加数据

if __name__=='__main__':
    global  file_list  #声明全局变量
    file_list=[]
    list_file()
    setup(version = "www.baidu.com",description = "QQ:2602159946",name = "baidu",zipfile=None,
    windows=[{"script": "main.py", "icon_resources": [(1,"App.ico")]}],
    options={"py2exe":{"dll_excludes":["MSVCP90.dll"],"includes":["sip"]}},
    includes = file_list)

