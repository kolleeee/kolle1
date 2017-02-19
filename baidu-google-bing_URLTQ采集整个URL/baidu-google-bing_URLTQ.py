#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#采集baidu-google-bing_URL地址
################################################
#读取TXT 内容   导入到消息队列里
#每扫描过1个就添加到TXT文本
#
#baidu 方法先遍历出快照地址   在从快照中读取URL地址
import urllib2, re, time
import urllib
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import list
import Queue
Aopenurl = Queue.Queue(4000) #要采集的关键字

class baidu_google_bing(threading.Thread):
    def __init__(self,htint,Aopenurl):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.Aopenurl=Aopenurl
        self.LS = list.Clist()  #初始化类
        self.a=0
    def run(self):
        try:
            #self.baidu_KZ_URL("http://www.baidu.com/s?wd=powered by dedecms&pn=0&rn=10&usm=1") #提取baidu  URL
            #print self.open_url_data("http://www.baidu.com/s?wd=powered by dedecms&pn=0&rn=10&usm=1")
#            self.google_TQ_URL("http://www.google.com.hk/search?q=inurl:admin/user.asp&start=10") #提取google  URL
#            self.bing_TQ_URL("http://cn.bing.com/search?q=inurl:admin/user.asp&go=&first=10") #提取bing  URL


            if self.Aopenurl.empty():   #判断队列是否为空
                print u"扫描列表为空"
                time.sleep(20)
                self.run()
            self.Chost = self.Aopenurl.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(20)
                self.run()

#            self.Chost.rstrip('\n')
#            self.Chost.strip() #去空格
#            self.Chost.lstrip()

            self.LS.list_del()  #清空list列表
            self.a=0
            self.for_url(self.Chost)
            dataA="----------data_url:%s----------"%(self.Chost)
            self.TXT_file(dataA)  #写入文本
            self.list_text()  #将数组中文件导入到TXT
            time.sleep(10)
            self.run()
        except:
            print "Thread:%d--baidu_google_bing---run-try--except!!!!!"%(self.Ht)
            time.sleep(10)
            self.run()

    def list_text(self):  #将数组中文件导入到TXT
        try:
            E = 0 #得到list的第一个元素
            while E < len(self.LS.list_2):
                self.TXT_file(self.LS.list_2[E])  #写入文本
                time.sleep(0.1)
                E +=1
        except:
            return 0

    def TXT_file(self,data):  #写入文本
        try:
            file_nem=time.strftime('%Y.%m.%d')
            file_object = open(file_nem+".txt",'a+')
            file_object.writelines("\r\n")
            file_object.writelines(data)
            file_object.close()
            print u"%s"%(data)
        except:
            print "--TXT_file--%s--try--except!!!!!"%(data)
            return 0

    def for_url(self,data):  #循环查找
        print u"------开始扫描%s------%s"%(data,time.strftime('%Y.%m.%d-%H.%M.%S'))
        b=300
        try:
            while self.a<=b:
                url_data="http://www.baidu.com/s?wd=%s&pn=%d&rn=10&usm=1"%(data,self.a)
                self.baidu_KZ_URL(url_data) #提取baidu  URL
                url_data="http://www.google.com.hk/search?q=%s&start=%d"%(data,self.a)
                self.google_TQ_URL(url_data) #提取google  URL
                url_data="http://cn.bing.com/search?q=%s&go=&first=%d"%(data,self.a)
                self.bing_TQ_URL(url_data) #提取bing  URL
                self.a+=10
                self.LS.liet_lsqc() #数组列表去重复
                print u"------当前数据量:%s---ID:%d---%s"%(len(self.LS.list_2),self.a,time.strftime('%H.%M.%S'))
                time.sleep(1)
            print u"------结束扫描%s------%s"%(data,time.strftime('%Y.%m.%d-%H.%M.%S'))
        except:
            print "Thread:%d--for_url---try--except!!!!!"%(self.Ht)
            return 0

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0
    ####################################################################
    def bing_TQ_URL(self,URL): #提取bing  URL
        try:
            ss=self.open_url_data(URL)
            if ss==0:  #读取网页内容
                time.sleep(2)
                return 0
            p = re.compile( r'<h3><a href="(.*?)" target="_blank"')
            sarr = p.findall(ss)
            i=0
            for every in sarr:
                if i>=3000:
                    print "Thread:%d-CS_openurl-URL:%s-Over 3000 URL address\n"%\
                          (self.Ht,URL)
                    break
                else:
                    i+=1
                if every:
                    #print "--",every #获取URL
                    self.LS.liet_add(every)  #添加到数组
        except:
            #print "--Thread:%d--bing_TQ_URL-url:%s--try--except!!--"%(self.Ht,URL)
            return 0
    ####################################################################
    def google_TQ_URL(self,URL): #提取google  URL
        try:
            ss=self.open_url_data(URL)
            if ss==0:  #读取网页内容
                time.sleep(2)
                return 0
            p = re.compile( r'<h3 class="r"><a href="/url.q=(.*?)&amp;')
            sarr = p.findall(ss)

            i=0
            for every in sarr:
                if i>=3000:
                    print "Thread:%d-CS_openurl-URL:%s-Over 3000 URL address\n"%\
                          (self.Ht,URL)
                    break
                else:
                    i+=1
                if every:
                    #print "--",every #获取URL
                    self.LS.liet_add(every)  #添加到数组

        except:
            #print "--Thread:%d--google_TQ_URL-url:%s--try--except!!--"%(self.Ht,URL)
            return 0
    ####################################################################
    def baidu_KZ_URL(self,URL): #提取百度快照  URL
        try:
            ss=self.open_url_data(URL)
            if ss==0:  #读取网页内容
                time.sleep(2)
                return 0
            p = re.compile( r'data-nolog href="(.+?)"  target="_blank"  class="m">')
            #data-nolog href=.(.+?).target="_blank"  class="m">
            #(data-nolog href=.*?)(.+?)(.*?target="_blank"  class="m">)
            #构造及编译正则表达式
            sarr = p.findall(ss)
            i=0
            for every in sarr:
                if i>=3000:
                    print "Thread:%d-CS_openurl-URL:%s-Over 3000 URL address\n"%\
                          (self.Ht,URL)
                    break
                else:
                    i+=1
                if every:
                    #print "--",every #获取URL
                    self.baidu_QU_KZ_URL(every) #提取百度快照  URL
        except:
            #print "--Thread:%d--baidu_KZ_URL-url:%s--try--except!!--"%(self.Ht,URL)
            return 0

    def baidu_QU_KZ_URL(self,URL): #提取百度快照  URL
        try:
            ss=self.open_url_data(URL)
            if ss==0:  #读取网页内容
                time.sleep(10)
                return 0
            p = re.compile( r'<div id="bd_snap_note">.*?<a.*?href=.(.+?)">.*?<\/a>')
            #<div id="bd_snap_note">.*?<a.*?href=.(.+?)>.*?<\/a>  #结果['http://www.isc.org.cn/zxzx/hlwzl/listinfo-4628.html"']
            sarr = p.findall(ss)
            if sarr[0]:  #判断是否为空数据
                #print sarr[0]
                self.LS.liet_add(sarr[0])  #添加到数组
        except:
            #print "Thread:%d--baidu_QU_KZ_URL-%s--try--except!!!!!"%(self.Ht,URL)
            return 0
    ####################################################################

if __name__=='__main__':
    print u"---------url地址采集   baidu-google-bing_URL--------"
    print u"--           软件目录下data.txt是扫描内容           --"
    print u"--------- BLOG:http://hi.baidu.com/alalmn  --------"
    #time.sleep(5)
    try:
        xxx = file('data.txt', 'r')
        for xxx_line in xxx.readlines():
        #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            url=urllib.quote(xxx_line.strip())
            Aopenurl.put(url,0.5)   #插入队列
            print u"%s"%(url)
        xxx.close()
        print u"---------采集内容 %s 条--------"%(Aopenurl.qsize())
    except:
        print u"软件目录下肯能找到不到data.txt文件"
        time.sleep(1000)
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(baidu_google_bing(i,Aopenurl))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程
