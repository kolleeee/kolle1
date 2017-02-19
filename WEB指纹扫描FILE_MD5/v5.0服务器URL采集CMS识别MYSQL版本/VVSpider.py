#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###################################################

from VVList import VVList
import VVQueue
from VVUtil import is_subdomain, trim_sdomain, get_domain_suffix, is_legal_domain
import list

import urllib2
import httplib
import re
import threading
import time
import ConfigParser

class VVSpider(threading.Thread):
    # 爬虫，专门来爬去URL，用来和搜集域名
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
        self.bool_com_cn = 0  # 0否1是 设置是否限制采集范围
        self.com_cn = ".com|.cn|cc|.org|.net|.gov"
        self.bool_2com = 0    # 是否采集二级域名
        self.com_cn_lis = []  # 分成数组
        #self.urlset = VVList()
        self.LS = list.Clist()  #初始化类
        self.readcfg()

    def readcfg(self):
        # 读取INI配置信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            com_cn = str(config.get("DATA", "com_cn"))
            self.com_cn_lis = com_cn.split("|")
            self.bool_2com = int(config.get("DATA", "BOOL_2com"))      # 是否采集二级域名
            self.bool_com_cn = int(config.get("DATA", "BOOL_com_cn"))  # 0否1是 设置是否限制采集范围
        except:
            self.com_cn_lis = self.com_cn.split("|")

    def bool_for_com_cn_lis(self,url): #查询域名是否正确1正确  0错误
        try:
            for B in self.com_cn_lis:
                if not B=="":
                    if url.__contains__(B):
                        return 1
            return 0
        except:
            return 0

    def open_url_200(self,url): # 判断URL是否能打开
        try:
            headers = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
            conn = httplib.HTTPConnection(url)
            conn.request('GET', "", None, headers)
            httpres = conn.getresponse()
            if httpres.status == 200:
                return 1
            return 0
        except Exception, e:
            return 0

    def work_loop(self):
        try:
            if VVQueue.StoreQueue.qsize() >= 5000:
                # 需要判断下 StoreQueue 消息队列需要存储的数据过多的时候跳过这个循环
                time.sleep(5)
                return 0
            starturl = VVQueue.ReadQueue.get(0.5)
            if not starturl:
                return 0

            if not self.open_url_200(starturl):  #判断网站是否能打开  可以快点采集
                print "[Spider][Thread:%d]--http_200--NO--[url:%s]--[time:%s]" %\
                      (self.n, starturl, time.strftime('%Y.%m.%d-%H.%M.%S'))
                time.sleep(0.1)
                return 0
            urlnum = self.URL_DZ('http://' + starturl)
            # 如果不是子域名的话，而且上面的没有抓取到页面，那么就可以加上www.再爬一次
            if not urlnum and not is_subdomain(starturl):
                self.URL_DZ('http://www.' + starturl)

            return 0
        except:
            pass

    def run(self):
        try:
            while True:
                self.work_loop()
                time.sleep(1)
        except:
            pass

    def startwithhttp(self, data):
        # 判断是否是HTTP字符
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
#            if data.find(sStr2) >= 0 or data.find(sStr3) >= 0:
#                return 1
            if data.find(sStr2) and data.find(sStr3):
                return 1 #print "没有找到"
            else:
                return 0 #print "查找到了"
        except:
            #pass
            return 1

    def URL_TQURL(self, data):
        # URL提取URL
        try:
            data += "/"      #data ="https://www.baidu.com/cache/sethelp/index.html"
            if data.find("http://") == 0:
                data = data[7:] #字符串删除
                nPos = data.index('/') # 查找字符
                return data[0:nPos]   # 复制指定长度的字符
            if data.find("https://") == 0:
                data = data[8:]  # 字符串删除
                nPos = data.index('/') #查找字符
                return data[0:nPos] #复制指定长度的字符
        except:
            print "[Spider][Thread:%d]-CS_openurl-Extract [URL:%s] URL error" % (self.n, data)
            pass

    def URL_CMS(self, data):  #cms	匹配    bbs.3drrr.com
        try:
            p = re.compile(r'<meta name="generator" content="(.*?)" />' )
            sarr = p.findall(data)
            if len(sarr)>=1:
                if not sarr[0]=="":
                    return sarr[0]
            else:
                return ""
        except:
            return ""

    def url_post(self, url):
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',
                "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req, timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        except:
            pass

    def get_url_lis1(self,url):
        try:
            self.list=[]  #self.list.append(data)  #添加数据
            req = urllib2.Request(url)
            req.add_header('User-Agent', "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.nml)")
            s = urllib2.urlopen(req, timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()

            ##################
            #CMS另类识别
            data_cms=self.URL_CMS(ss)
            if len(data_cms)>=1:
                hm_url = "http://webxscan.com/url_cms.php?url=%s&cms=%s" % (url, data_cms)
                self.url_post(hm_url)   # 神龙后门
                print "[Spider][Thread:%d]-openurl  cms-[URL:%s]-[cms:%s]"%\
                      (self.n, url, data_cms)
            ##################
            # 构造及编译正则表达式
            p = re.compile(r'<a[\s\S]*?href=["]([\s\S]*?)["][\s\S]*?>[\s\S]*?</a>' )
            # 找出一条一条的<a></a>标签
            sarr = p.findall(ss)
            for every in sarr:
                if not every:
                    continue
                shref = every.replace("www.","")
                if not self.startwithhttp(shref):   # 判断是否是HTTP字符
                    shref = self.URL_TQURL(shref)  # URL提取URL
                    if is_legal_domain(shref):   # 过滤违规域名
                        if self.bool_2com:# 是否采集二级域名
                            if is_subdomain(shref):  #判断域名是否是二级域名 1是0否
                                self.list.append(shref)  #添加到数组

                                a1=trim_sdomain(shref)  #解析主域名
                                self.list.append(a1)   # 添加到数组
                            else:
                                self.list.append(shref)  #添加数据
                        else:
                            self.list.append(shref)  #添加数据
            if len(self.list)>=1:
                return set(s.strip() for s in self.list)
            return 0
        except Exception,e:
            return 0

    def URL_DZ(self, URL):
        try:
            data=self.get_url_lis1(URL)
            #print len(data)
            if data:
                for data_url in data:
                    if not data_url:
                        continue
                    if self.bool_com_cn:   # 0否1是 设置是否限制采集范围
                        if self.bool_for_com_cn_lis(data_url):  #限制采集范围
                            VVQueue.StoreQueue.put(data_url, 0.1)
                    else:
                        VVQueue.StoreQueue.put(data_url, 0.1)

            try:
                print "[Spider][Thread:%d]--[count url:%d]--[url:%s]--[time:%s]" %\
                  (self.n, len(data), URL, time.strftime('%Y.%m.%d-%H.%M.%S'))
                return 1
            except Exception, e:
                return 1
        except Exception, e:
            print "[Spider][Thread:%d]--Exception--[url:%s]--[time:%s]\n[%s]" %\
                  (self.n, URL, time.strftime('%Y.%m.%d-%H.%M.%S'), e)
            return 0

################################################
if __name__ == '__main__':
    VVQueue.ReadQueue.put("bbs.3drrr.com", 0.1)
#    # 启动数据库
#    db = VVQueue.VVQueue(0)
#    db.start()
    threads = []  # 线程
    for i in range(1):  # nthreads=10  创建10个线程
        threads.append(VVSpider(i))
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程
        t.join()
