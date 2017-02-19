#!/usr/bin/env python
#-*- coding: UTF-8 -*-
###################################################
#  将当前目录加入系统环境
#import os
#import sys
#skyeyepath = os.path.realpath((os.path.dirname(__file__)) + "/../")
#if not skyeyepath in sys.path:
#    sys.path.append(skyeyepath)

from VVList import VVList
import VVQueue
from VVUtil import is_subdomain, trim_sdomain, get_domain_suffix, is_legal_domain

import urllib2
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
        self.urlset = VVList()
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

    def bool_for_com_cn_lis(self, url):
        # 查询域名是否正确1正确  0错误
        try:
            for b in self.com_cn_lis:
                if b:
                    try:
                        if str(url).find(b) >= 0:
                            return 1
                    except:
                        pass
        except:
            pass
        return 0

    def work_loop(self):
        try:
            if VVQueue.StoreQueue.qsize() >= 5000:
                # 需要判断下 StoreQueue 消息队列需要存储的数据过多的时候跳过这个循环
                time.sleep(5)
                return
            starturl = VVQueue.ReadQueue.get(0.5)
            if not starturl:
                return
            urlnum = self.URL_DZ('http://' + starturl)
            # 如果不是子域名的话，而且上面的没有抓取到页面，那么就可以加上www.再爬一次
            if not urlnum and not is_subdomain(starturl):
                self.URL_DZ('http://www.' + starturl)
        except:
            pass

    def run(self):
        try:
            while True:
                self.work_loop()
                time.sleep(0.02)
        except:
            pass

    def startwithhttp(self, data):
        # 判断是否是HTTP字符
        try:
            sStr2 = 'http://'
            sStr3 = 'https://'
            if data.find(sStr2) >= 0 or data.find(sStr3) >= 0:
                return 1
        except:
            pass
        return 0

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

    def URL_DZ(self, URL):
        # 遍历页里的地址
        self.urlset.clear()
        try:
            req = urllib2.Request(URL)
            req.add_header('User-Agent', "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.nml)")
            s = urllib2.urlopen(req, timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            ss = s.read()
            # 构造及编译正则表达式
            p = re.compile(r'<a[\s\S]*?href=["]([\s\S]*?)["][\s\S]*?>[\s\S]*?</a>' )
            # 找出一条一条的<a></a>标签
            sarr = p.findall(ss)
            for every in sarr:
                if self.urlset.isfull():
                    print "[Spider][Thread:%d]-openurl-[URL:%s]-[time Over:%d] URL address"%\
                          (self.n, URL, self.urlset.getitemcount())
                    break
                shref = every.replace("www.", "")
                if self.startwithhttp(shref):   # 判断是否是HTTP字符
                    newdomain = self.URL_TQURL(shref)  # URL提取URL
                    if newdomain and is_legal_domain(newdomain):   # 过滤违规域名
                        if self.bool_2com and is_subdomain(newdomain):
                            #print newdomain
                            self.urlset.add(newdomain)   # 添加到数组
                            #continue

            for n in xrange(self.urlset.getitemcount()):
                tmpdomain = self.urlset.getitem(n)
                if not tmpdomain:
                    continue
                #print tmpdomain
                if self.bool_com_cn:   # 0否1是 设置是否限制采集范围
                    if self.bool_for_com_cn_lis(tmpdomain):
                        # 存储一下，先不爬这个，优先爬下子域名
                        VVQueue.StoreQueue.put(tmpdomain, 0.1)
                        #else:
                        # 不存储，但是让爬虫爬下页面就行
                        #if VVQueue.ReadQueue.qsize() <= 14000:
                        #    VVQueue.ReadQueue.put(tmpdomain, 0.1)
                else:
                    VVQueue.StoreQueue.put(tmpdomain, 0.1)

            print "[Spider][Thread:%d]--[count url:%d]--[url:%s]--[time:%s]" %\
                  (self.n, self.urlset.getitemcount(), URL, time.strftime('%Y.%m.%d-%H.%M.%S'))
        except Exception, e:
            print "[Spider][Thread:%d]--Exception--[url:%s]--[time:%s]\n[%s]" %\
                  (self.n, URL, time.strftime('%Y.%m.%d-%H.%M.%S'), e)
            return self.urlset.getitemcount()



################################################
if __name__ == '__main__':
    VVQueue.ReadQueue.put("www.163.com", 0.1)
#    # 启动数据库
#    db = VVQueue.VVQueue(0)
#    db.start()
    threads = []  # 线程
    for i in range(1):  # nthreads=10  创建10个线程
        threads.append(VVSpider(i))
    for t in threads:   #不理解这是什么意思    是结束线程吗
        t.start()  #start就是开始线程
        t.join()
