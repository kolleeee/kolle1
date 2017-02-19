#!/usr/local/bin/python
#-*- coding: UTF-8 -*-

#i1=200
#i2=50
#
#print i1//i2
#print format(i1,str(i2))

import os,sys,string
import time

##python 实现百分比和进度条
##就是利用\r回车不换行
#def view_bar(num=1,sum=100,bar_word=":"):
#    rate=float(num)/float(sum)
#    rate_num=int(rate*100)
#    #print '\r%d%% :'%(rate_num)
#    print '\r%d'%(rate_num),
##    for i in range(0,num):
##        os.write(1,bar_word)
#    #sys.stdout.flush()
#
#if __name__ == '__main__':
#    for i in range(0,100):
#        time.sleep(0.1)
#        view_bar(i,100)

#print '\r%d',
#print '\n11111'

#def b_d_i(i1,i2):
#    try:
#        rate=float(i1)/float(i2)
#        return int(rate*100)
#    except:
#        return 0
#
#print b_d_i(0,0)

#directories   files
#DATA="34A423D6B683C97CA20EA2F9F4176B08"
#print DATA.lower() #转换成小写在比对




print bool_for_com_cn_lis("www.baidu.hh")