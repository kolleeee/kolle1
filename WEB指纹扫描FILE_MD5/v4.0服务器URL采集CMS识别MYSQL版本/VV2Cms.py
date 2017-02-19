#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import os


from VVList import VVList
import VVQueue
from VVUtil import is_subdomain
import re
import socket
import httplib
import threading
import time

import hashlib
import urllib2
import ConfigParser
socket.setdefaulttimeout(10)

class CrackWorker(object):
    def __init__(self, furl, flist):
        self.url = furl
        self.urllist = flist
        self.bwritefile = 0                 # 设置CMS识别出来的数据是否写入到本地
        self.starttime = int(time.time())  # 计时
        self.post_url = "http://webxscan.com/cms.php"  # 神龙的后门
        self.cmstype = ""
        self.readcfg()

    def readcfg(self):
        # 读取INI配置信息
        try:
            config = ConfigParser.ConfigParser()
            config.readfp(open("Server.ini"))
            self.post_url = str(config.get("DATA", "post_url"))
            self.bwritefile = int(config.get("DATA", "BOOL_file")) # 设置CMS识别出来的数据是否写入到本地
        except:
            pass

    def reset(self):
        self.cmstype = ""
        self.starttime = int(time.time())  # 计时
        self.url = ""

    def run(self):
        try:
            self.for_list()
        except:
            pass

    def write2file(self, name, url):
        # 写入文本
        try:
            file_object = open(name, 'a')
            file_object.writelines(url)
            file_object.writelines("\r\n")
            file_object.close()
        except Exception, e:
            print "[CrackWorker] Fail to write file,%s,%s,%s" %( name, url, e)

    def getcmstype(self):
        if self.cmstype:
            return self.cmstype
        return '-'

    def url_post(self, url):
        try:
            req = urllib2.Request(url)
            req.add_header('User-Agent',
                           "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            urllib2.urlopen(req, timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        except:
            pass

    def text_cms(self, url2, cms):
        # CMS 处理方式
        try:
            url = "http://webxscan.com/cms.php?url=%s&cms=%s" % (url2, cms)
            self.url_post(url)   # 神龙后门
            if self.bwritefile:
                name="www/%s.txt"%(cms)
                self.write2file(name, url2)  # 写入文本
        except:
            pass

    def for_list(self):
        try:
            for i in self.urllist.urllist:
                #print i #URL链接文件(地址)|CMS名称|关键字|文件MD5
                try:
                    # TODO 发布时，将这些注释代码取消注释
                    if (int(time.time())-self.starttime) >= VVQueue.Cms_timeoutout:
                        print "CMS scan:%s CMS>=time overtime:%d S" % (self.url, VVQueue.Cms_timeoutout)
                        break
                    # 网址  URL链接文件(地址)
                    data = self.open_url(self.url, i[0])
                    if not data:
                        continue
                    if i[2]:  # 关键字
                        pname = re.compile(i[2])
                        sarr = pname.findall(data)
                        if sarr:
                            self.text_cms(self.url, i[1]) # 神龙的后门
                            post_data = "%s?url=%s&cms=%s&hand_url=%s&KEY_MD5=%s" % \
                                        (self.post_url, self.url, i[1], i[0], i[2])
                            self.cmstype = i[1]
                            self.url_post(post_data)   # 提交远程集群
                            break  # 跳出整个循环
                    if i[3]:  # 文件MD5
                        list_feil_md5 = self.getfilemd5(data)
                        if list_feil_md5[0]:
                            if str(i[3]).lower() == str(list_feil_md5[1]).lower():  # 转换成小写在比对
                                self.text_cms(self.url, i[1])   # 神龙的后门
                                post_data = "%s?url=%s&cms=%s&hand_url=%s&KEY_MD5=%s" % \
                                            (self.post_url, self.url, i[1], i[0], i[3])
                                self.cmstype = i[1]
                                self.url_post(post_data)   # 提交远程集群
                                break  # 跳出整个循环
                except Exception, e:
                    pass
        except Exception, e:
            pass

    def open_url(self, url, hand_url):  # 获取URL内容
        headers = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        try:
            conn = httplib.HTTPConnection(url)
            conn.request('GET', hand_url, None, headers)
            httpres = conn.getresponse()
            if httpres.status == 200:
                return httpres.read()
        except Exception, e:
            pass

    def getfilemd5(self, filedata):
        if not filedata:
            return [0, ""]
        bres = False
        strmd5 = ""
        try:
            md5 = hashlib.md5()
            md5.update(filedata)
            strmd5 = md5.hexdigest()
            bres = True
        except:
            pass
        return [bres, strmd5]

class VVCms(threading.Thread):
    # 指纹识别
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.n = n
        self.urllist = VVList()    # 初始化类VVList()
        self.worker = CrackWorker("", self.urllist)
        self.open_file()           # 读取CMS
        print "[2_CMS][Thread:%d] run  cms:%s" % (self.n,len(self.urllist.urllist))

    def work_loop(self):
        newhost = ""
        try:
            if VVQueue.re_www_Cms_Queue.qsize() <= 0:        # 判断队列是否为空
                time.sleep(5)
                return

            newhost = VVQueue.re_www_Cms_Queue.get(0.5)  # get()方法从队头删除并返回一个项目
            if not newhost:
                return

            print "[2_CMS][Thread:%d] [url:%s] run cms starting..." % (self.n, newhost)
            cmstmp = ''
            if self.open_url_200(newhost):
                # 测试url地址  CMS
                cmstmp = self.CS_cms(newhost)
                return
            else:
                print "[2_CMS][Thread:%d] [url:%s] NO DATA RETURN!" % (self.n, newhost)

            # 如果页面无法访问，而且不是子域名的话，就检查一下(www.)domain.cn
            if not is_subdomain(newhost):
                newhost = 'www.' + newhost
                print "[2_CMS][Thread:%d] [url:%s] www run cms starting..." % (self.n, newhost)
                if self.open_url_200(newhost):
                    # 测试url地址  CMS
                    cmstmp = self.CS_cms(newhost)
                else:
                    print "[2_CMS][Thread:%d] [url:%s]--www NO DATA RETURN!" % (self.n, newhost)
        except Exception, e:
            print "[2_CMS][Thread:%d] [url:%s] Exception:[%s]" % (self.n, newhost, e)

    def run(self):
        try:
            while True:
                self.work_loop()
                time.sleep(0.02)
        except:
            pass

    def open_url_200(self, url):
        # 判断URL是否能打开
        headers = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        try:
            conn = httplib.HTTPConnection(url)
            conn.request('GET', "", None, headers)
            httpres = conn.getresponse()
            if httpres.status == 200:
                return httpres.read()
        except Exception, e:
            pass

    def open_file(self):
        #合并字典
        #dicpath = os.path.abspath(skyeyepath+'/cms/dic/')
        #doclist = os.listdir(dicpath)
        doclist = os.listdir(os.getcwd()+r'\cms')
        doclist.sort()
        for filename in doclist:
            try:
                for url in open('cms/'+filename,'r'):
                    data = url.strip().decode("gbk")
                    self.file_add(data)
            except Exception, e:
                print e

    def file_add(self, data):
        # 添加数组
        try:
            if "#" in data:
                return 0
            ss = data.split("|")
            self.urllist.add(ss)
        except Exception, e:
            print e

    def CS_cms(self, url):
        # 遍历页里的地址
        nstart = int(time.time())  # 计时
        self.worker.reset()
        self.worker.url = url
        self.worker.run()
        print "[2_CMS][Thread:%d] [url:%s] [CMS:%s] [time:%d /s]" % \
              (self.n, url, self.worker.getcmstype(), (int(time.time())-nstart))
        return self.worker.getcmstype()



if __name__ == '__main__':
    VVQueue.re_www_Cms_Queue.put('zysd.com.cn')
    VVQueue.re_www_Cms_Queue.put('www.baidu.com')
    VVQueue.re_www_Cms_Queue.put('domeng.cn')
    VVQueue.re_www_Cms_Queue.put('soxan.cn')
    VVQueue.re_www_Cms_Queue.put('chinahanhai.net')
    VVQueue.re_www_Cms_Queue.put('icitu.com')
    VVQueue.re_www_Cms_Queue.put('www.jike521.com')

    threads = []
    threadcount = 1
    for i in xrange(threadcount):
        threads.append(VVCms(i))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    #VVQueue.CmsQueue.push('www.baidu.com')