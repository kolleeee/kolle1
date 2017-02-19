#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
##################################################
#结束进程  在从新开启进程
import time
import threading
import ConfigParser  #INI读取数据
import sys
import os

class CS_close_open(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.close_open=100
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            self.close_open = int(config.get("DATA","close_open"))
        except:
            print "INI   try--except   close_open"
        #self.data=__file__  #完整路径
        #self.run()

    def run_run(self):
        try:
            self.run()
        except:
            time.sleep(2)
            self.run()

    def run(self):
        try:
            for i in range(self.close_open):
                delete="#################main.exe run  %d--%d  min#################"%(i,self.close_open)
                print delete
                time.sleep(60)
                if i>=self.close_open-1:
                    print "main.exe run"
                    #关闭重启本身
                    self.restart_program()
                    break     #在需要时终止for循环
            time.sleep(60)
            self.run_run()
        except:
            time.sleep(60)
            self.run_run()

    def restart_program(self): #重启自身
        python = sys.executable
        os.execl(python, python, * sys.argv)

if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_close_open())

    for thread in threads:   #不理解这是什么意思    是结束线程吗
        thread.start()  #start就是开始线程



