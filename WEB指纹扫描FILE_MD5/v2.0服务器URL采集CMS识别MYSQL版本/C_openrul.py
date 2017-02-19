#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
###################################################
import urllib2,re
import threading
import time
import list
import ConfigParser  #INI读取数据
import class_Queue
import xx_com_cn_xx #对域名拆分


class CS_openurl(threading.Thread):
    def __init__(self,htint):
        threading.Thread.__init__(self)
        self.Ht=htint
        self.BOOL_com_cn=0 #0否1是 设置是否限制采集范围
        self.com_cn=".com|.cn|cc|.org|.net|.gov"
        self.BOOL_2com=0 #是否采集二级域名
        self.com_cn_lis=[]  #分成数组
        self.Server_ini()  #读取INI配置信息

    def Server_ini(self):  #读取INI配置信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            com_cn= str(config.get("DATA","com_cn"))
            self.com_cn_lis=com_cn.split("|")
            print self.com_cn_lis
            self.BOOL_2com=int(config.get("DATA","BOOL_2com")) #是否采集二级域名
            self.BOOL_com_cn=int(config.get("DATA","BOOL_com_cn")) #0否1是 设置是否限制采集范围

        except:
            self.com_cn_lis=self.com_cn.split("|")
            pass

    def bool_for_com_cn_lis(self,url): #查询域名是否正确1正确  0错误
        try:
            for B in self.com_cn_lis:
                if not B=="":
                    if url.__contains__(B):
                        return 1
            return 0
        except:
            return 0

    def run_run(self):
        try:
            self.run()
        except:
            time.sleep(2)
            self.run()

    def run(self):
        try:
            while True:
                if class_Queue.Aopenurl.qsize()>=5000: #读取
                    #需要判断下 Aopenurl 消息队列需要存储的数据过多的时候跳过这个循环
                    time.sleep(30)
                    continue   #跳过
                URL=class_Queue.Bopenurl.get(0.5)
                self.URL_DZ("http://"+URL)
                time.sleep(5)

            time.sleep(20)
            self.run_run()
        except:
            time.sleep(20)
            self.run_run()

    ######################
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
                    shref = shref[0].replace("www.","")
                    if ~self.URL_STR(shref):  #判断是否是HTTP字符
                        a1=self.URL_TQURL(shref) #URL提取URL
                        if self.BOOL_2com:#是否采集2级域名
                            if a1:
                                LS.liet_add(a1)  #添加到数组
                        else:
                            #a2=xx_com_cn_xx.get_sdomain(a1)  #获取主域名
                            #if a2:
                            if xx_com_cn_xx.www_www(a1): #过滤违规域名
                                LS.liet_add(a1)  #添加到数组

            LS.liet_lsqc() #数组列表去重复
            time.sleep(0.5)
            for i in range(len(LS.list_2)):
                if self.BOOL_com_cn: #0否1是 设置是否限制采集范围
                    if self.bool_for_com_cn_lis(LS.list_2[i]):
                        #print LS.list_2[i],"111111111"
                        class_Queue.Aopenurl.put(LS.list_2[i],0.1)
                    else:
                        class_Queue.Aopenurl.put(LS.list_2[i],0.1)
                        #print LS.list_2[i]

            print "Thread:%d--list_url:%d--url:%s--time:%s"%(self.Ht,len(LS.list_2),URL,time.strftime('%Y.%m.%d-%H.%M.%S'))
        except:
            print "Thread:%d--try-except--url:%s--time:%s"%(self.Ht,URL,time.strftime('%Y.%m.%d-%H.%M.%S'))
        return 0

################################################
if __name__=='__main__':
#    threads = []  #线程
#    for i in range(1):  #nthreads=10  创建10个线程
#        threads.append(class_Queue.Csqlite_Queue(i))
#    for t in threads:   #不理解这是什么意思    是结束线程吗
#        t.start()  #start就是开始线程
    class_Queue.Bopenurl.put("www.163.com",0.1)
    threads = []  #线程
    for i in range(1):  #nthreads=10  创建10个线程
        threads.append(CS_openurl(i))
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程
