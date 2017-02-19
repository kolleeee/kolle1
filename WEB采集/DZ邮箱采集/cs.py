#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import urllib
import re

import sys
import os
import atexit
def TXT_file_email(data):  #写入文本
    try:
        file_object = open("email\\"+"www.126.com"+"email.txt",'a+')
        file_object.writelines(data)
        file_object.writelines("\n")
        file_object.close()
    except Exception,e:
        pass


TXT_file_email("11111111111111111")