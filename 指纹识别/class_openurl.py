#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#采集URL地址
################################################
import urllib2, re, time
import socket
import threading
socket.setdefaulttimeout(10)  #设置了全局默认超时时间
import thread
import list
import unicodedata
import class_Queue  #消息队列

class CS_openurl(threading.Thread):
    def __init__(self,htint,Aopenurl,Bopenurl,Copenurl):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.Aopenurl=Aopenurl  #要采集的URL
        self.Bopenurl=Bopenurl  ##http200 链接成功的网站放这
        self.Copenurl=Copenurl

    def run(self):
        try:
            if self.Aopenurl.empty():   #判断队列是否为空
                print "Thread:%d--CS_openurl-data Aopenurl  null"%(self.Ht)
                time.sleep(30)
                self.run()
            self.Chost = self.Aopenurl.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(30)
                self.run()

            #print "1111111111111111111%s",(self.Chost)
            self.URL_DZ("http://"+self.Chost) #遍历页里的地址
            time.sleep(2)
            self.run()
        except:
            #print "Thread:%d--CS_openurl---run-try--except!!!!!"%(self.Ht)
            time.sleep(60)
            self.run()
    ####################################################################
    def URL_STR(self,data):#判断是否是HTTP字符
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
            if data.find(sStr2) and data.find(sStr3):
                return 1 #print "没有找到"
            else:
                return 0 #print "查找到了"
        except:
            return 1

    def URL_TQURL(self,data): #URL提取URL
        try:
            data +="/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if ~data.find("http://"):  #~取反
                data=data[7:] #字符串删除
                nPos = data.index('/') #查找字符        #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1

            if ~data.find("https://"):  #~取反
                data=data[8:] #字符串删除
                nPos = data.index('/') #查找字符
                #print nPos
                sStr1 = data[0:nPos] #复制指定长度的字符
                return sStr1
        except:
            return 0
            #print "Thread:%d-CS_openurl-Extract URL:%s URL error"%\
            #      (self.Ht,data)

    def URL_DZ(self,URL):  #遍历页里的地址
        try:
            LS = list.Clist()  #初始化类
            LS.list_del()  #清空list列表
            req = urllib2.Request(URL)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            p = re.compile( r'<a.+?href=.+?>.+?</a>' )
            pname = re.compile( r'(?<=>).*?(?=</a>)' )
            phref = re.compile( r'(?<=href\=\").*?(?=\")')
            #构造及编译正则表达式
            sarr = p.findall(ss)#找出一条一条的<a></a>标签   #这添加到数组在过滤重复值减少mysql压力

            i=0
            for every in sarr:
                if i>=3000:
                    print "Thread:%d-CS_openurl-URL:%s-Over 3000 URL address\n"%\
                          (self.Ht,URL)
                    break
                else:
                    i+=1
                sname = pname.findall( every )
                if sname:
                    sname = sname[0]
                    shref = phref.findall( every )
                if shref:
                    shref = shref[0]
                    #print shref #获取URL
                    if ~self.URL_STR(shref):
                        a1=self.URL_TQURL(shref) #URL提取URL
                        LS.liet_add(a1)  #添加到数组

            LS.liet_lsqc() #数组列表去重复
            time.sleep(0.5)
            #能访问到说明有效添加到
#            if ~self.Bopenurl.full(): #如果队列满了  取反
#                add_url=URL[7:]  #替换http://字符串
#                self.Bopenurl.put(add_url,1) ##http200 链接成功的网站放这
            E = 0 #得到list的第一个元素
            while E < len(LS.list_2):
                #print LS.list_2[E]
                E = E + 1
#                if ~self.Aopenurl.full(): #如果队列满了  取反
#                    self.Aopenurl.put(LS.list_2[E],0.1)
                try:
                    thread.start_new_thread(self.host_RUL_200,(LS.list_2[E],))
                    time.sleep(0.1) #确保先运行Seeker中的方法
                except BaseException, e:
                    #print e
                    return 0

            self.run()  #读取URL
            # 上面是将每条<a></a>里面的内容和地址给匹配出来
        except:
            #print "--Thread:%d--CS_openurl-url:%s--try--except!!--"%(self.Ht,URL)
            time.sleep(3)
            self.run()

    def open_url_data(self,url):  #读取网页内容
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            #req.add_header('User-Agent','userAgentIE9')
            #req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)")
            s = urllib2.urlopen(req,timeout=20)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            return s.read()
        except:
            return 0

    def has_hz(self,text):  #判断是否包含中文
        try:
            hz_yes = False
            for ch in text:
                if isinstance(ch, unicode):
                    if unicodedata.east_asian_width(ch)!= 'Na':
                        hz_yes = True
                        break
                else:
                    continue
            return hz_yes
        except:
            return 0

    def host_RUL_200(self,host):  #测试URL FTP是否开放
        try:
            ss=self.open_url_data("http://"+host)
            if ss==0:  #读取网页内容
                return 0
            data=ss[0:400]
            if self.has_hz(data.strip().decode("gbk")):  #site.decode("utf8")
                #print "open gbk url:%s"%(host)
                self.Bopenurl.put(host,0.1)
                return 0
            if self.has_hz(data.strip().encode('gb2312')):
                #print "open gb2312 url%s"%(host)
                self.Bopenurl.put(host,0.1)
                return 0
        except:
            return 0






################################################
if __name__=='__main__':
    threads = []  #线程
    nthreads=1
    class_Queue.Aopenurl.put("163.com",0.3)   #插入队列
    class_Queue.Aopenurl.put("baidu.com",0.3)   #插入队列
    for i in range(nthreads):  #nthreads=10  创建10个线程
        threads.append(CS_openurl(i,class_Queue.Aopenurl,class_Queue.Bopenurl,class_Queue.Copenurl))

    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程

