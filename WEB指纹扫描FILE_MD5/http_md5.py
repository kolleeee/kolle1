#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
import requests
import hashlib

def open_url(URL):
    try:
        response = requests.get(URL)
        return response.content
    except BaseException, e:
        #print(str(e))
        return 0

def GetFileMd5(File_data):
    file = None
    bRet = False
    strMd5 = ""
    try:
        #file = open(strFile, "rb")
        md5 = hashlib.md5()
        strRead = File_data
#        while True:
            #strRead = file.read(8096)
        if not strRead:
           return [0,""]
        md5.update(strRead)
            #read file finish
        bRet = True
        strMd5 = md5.hexdigest()
    except:
        bRet = False
    finally:
        if file:
            file.close()
    return [bRet, strMd5]


if "__main__" == __name__:
    #strPath = raw_input("please input get md5 file:")
    data=open_url("http://127.0.0.1:8888/FILE_MD5/1.ico")
    if data:
        list_feil_md5=GetFileMd5(data)
        print list_feil_md5
        if list_feil_md5[0]:
            print list_feil_md5[1]

