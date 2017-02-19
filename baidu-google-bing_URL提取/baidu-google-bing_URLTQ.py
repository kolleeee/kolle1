#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#采集baidu-google-bing_URL地址  落雪--灰帽SEO   QQ2602159946
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
import cookielib
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
            #self.baidu_KZ_URL("http://www.baidu.com/s?wd=poweredbydedecms&pn=0&rn=10&usm=1") #提取baidu  URL
            #print self.open_url_data("http://www.baidu.com/s?wd=powered by dedecms&pn=0&rn=10&usm=1")
#            print self.open_url_data("http://www.google.com.hk/search?q=inurl:admin/user.asp&start=10") #提取google  URL
#            self.bing_TQ_URL("http://cn.bing.com/search?q=inurl:admin/user.asp&go=&first=10") #提取bing  URL


            if self.Aopenurl.empty():   #判断队列是否为空
                print u"扫描列表为空"
                time.sleep(60)
                self.run()
            self.Chost = self.Aopenurl.get(0.5)  #get()方法从队头删除并返回一个项目
            if self.Chost=="":
                time.sleep(10)
                self.run()

            self.Chost.rstrip('\n')
            self.Chost.strip() #去空格
            self.Chost.lstrip()

            self.LS.list_del()  #清空list列表
            self.a=0
            self.for_url(self.Chost)
            #dataA="----------data_url:%s----------"%(self.Chost)
            #self.TXT_file(dataA)  #写入文本
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
        b=350
        try:
            while self.a<=b:
                url_data="http://www.baidu.com/s?wd=%s&pn=%d&rn=10&usm=1"%(data,self.a)
                self.URL_TQ(url_data) #提取baidu  URL
                url_data="http://www.google.com.hk/search?q=%s&start=%d"%(data,self.a)
                self.URL_TQ(url_data) #提取google  URL
                url_data="http://cn.bing.com/search?q=%s&go=&first=%d"%(data,self.a)
                self.URL_TQ(url_data) #提取bing  URL
                self.a+=10
                self.LS.liet_lsqc() #数组列表去重复
                print u"------当前数据量:%s:%s---ID:%d---%s"%(len(self.LS.list),len(self.LS.list_2),self.a,time.strftime('%H.%M.%S'))
                time.sleep(0.5)
            print u"------结束扫描%s------%s"%(data,time.strftime('%Y.%m.%d-%H.%M.%S'))
        except:
            print "Thread:%d--for_url---try--except!!!!!"%(self.Ht)
            return 0

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
            print "Thread:%d-CS_openurl-Extract URL:%s URL error"%\
                  (self.Ht,data)

    def URL_TQ(self,URL): #提取  URL
        try:
            ss=self.open_url_data(URL)
            if ss==0:  #读取网页内容
                print u"%s：URL无返回内容"%(URL)
                time.sleep(2)
                return 0
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
                        if ~self.URL_STR(shref):
                            a1=self.URL_TQURL(shref) #URL提取URL
                            #self.LS.liet_add(a1)  #添加到数组
                            #print "URL:",a1
                            skl=0
                            for A in ["http:",";","&","="]:
                                if str(a1).__contains__(A):
                                    skl=1
                            for B in ["baidu","google","bing"]:
                                if str(a1).__contains__(B):
                                    skl=1
                            if not a1 == None:
                                if not skl:
                                    self.LS.liet_add(a1)  #添加到数组
                                    print "URL:",a1
        except BaseException, e:
            print "11111111",e
            #print "--Thread:%d--baidu_KZ_URL-url:%s--try--except!!--"%(self.Ht,URL)
            return 0

    ####################################################################

if __name__=='__main__':
    print u"---------url地址采集   baidu-google-bing_URL--------"
    print u"--           软件目录下data.txt是扫描内容           --"
    print u"--------- BLOG:http://hi.baidu.com/alalmn  --------"
#    #time.sleep(5)
    try:
        xxx = file('data.txt', 'r')
        for xxx_line in xxx.readlines():
        #如果输入的内容读取有回车符号，可以用strip来消除，可得到完美的输出
            url=urllib.quote(xxx_line.strip())  #url编码
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
