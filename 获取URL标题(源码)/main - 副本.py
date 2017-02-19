#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#获取网站标题
##################################################
#qq:29295842
#BLOG:http://hi.baidu.com/alalmn
import urllib
import re
import VVMysql
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2


class web_title:
    def __init__(self):
        self.db = VVMysql.VVMysql()
        self.db.mysql_open()
        print "go"
        self.run()

    def execute_sql(self, data):
        try:
            self.db.mysql_commit()      # 保存数据
            return self.db.mysql_insert(data)  # 添加数据
        except Exception, e:
            return 0

    def open_txt(self):
        xxx = file("links.txt", 'r')
        for xxx_line in xxx.readlines():
            try:
                data=xxx_line.lstrip().rstrip().strip().rstrip('\n')
                data_time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                data_time=time.mktime(time.strptime(data_time2,'%Y-%m-%d %H:%M:%S'))  #转化成时间戳
                sql_data="insert into url(url,time) VALUES('%s','%s');"%\
                         (str(data),data_time)
                    #print sql_data
                self.execute_sql(sql_data)
            except BaseException, e:
                print(str(e))

    def send_sql_url_ok(self):  #读取数据库
        try:
            sql_data = "select * from url where bool='ok'"
            print sql_data
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                data = row[0]   #+"|"+row[1]
                self.TXT_file("url1.txt",data)  #写入文本
                #<a href="http://www.kmpdsp.com/temp/ueod3u6/index.html" target="_blank">湖州小姐 -【同城一夜情网】</a><br>
                data='<a href="%s" target="_blank">%s</a><br>'%(row[0],row[1])
                #print "add url.txt  %s"%(data)
                self.TXT_file("url.txt",data)  #写入文本
                data = row[0]+"|"+row[1]
                self.TXT_file("url2.txt",data)  #写入文本
        except BaseException, e:
            pass

    def TXT_file(self,file_nem,data):  #写入文本
        try:
            #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
            file_object = open(file_nem,'a')
            #file_object.write(list_passwed[E])
            file_object.writelines(data)
            file_object.writelines("\n")
            file_object.close()
        except Exception,e:
            #print e
            return 0

    def open_sql_url(self):  #读取数据库
        try:
            sql_data = "select * from url where bool is null"
            print sql_data
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                url = row[0]
                s1,s2=self.url_http_200(url)
                try:
                    if s1==True:
                        sql_data = "update url set title='%s',bool='ok' where url='%s'" % (str(s2), url)
                        print sql_data
                        self.execute_sql(sql_data)
                    else:
                        sql_data = "update url set title='%s',bool='no' where url='%s'" % ("", url)
                        print sql_data
                        self.execute_sql(sql_data)
                except BaseException, e:
                    #print(str(e))
                    try:
                        sql_data = "update url set title='%s',bool='ok' where url='%s'" % (str(s2.decode("gbk")), url)
                        print sql_data
                        self.execute_sql(sql_data)
                    except BaseException, e:
                        pass
                    pass
        except BaseException, e:
            pass

    def open_sql_url_ok(self):  #读取数据库
        try:
            sql_data = "select * from url where bool='ok'"
            print sql_data
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                url = row[0]
                s1,s2=self.url_http_200(url)
                try:
                    if s1==True:
                        sql_data = "update url set title='%s',bool='ok' where url='%s'" % (str(s2), url)
                        print sql_data
                        self.execute_sql(sql_data)
                    else:
                        sql_data = "update url set title='%s',bool='no' where url='%s'" % ("", url)
                        print sql_data
                        self.execute_sql(sql_data)
                except BaseException, e:
                    #print(str(e))
                    try:
                        sql_data = "update url set title='%s',bool='ok' where url='%s'" % (str(s2.decode("gbk")), url)
                        print sql_data
                        self.execute_sql(sql_data)
                    except BaseException, e:
                        pass
                    pass
        except BaseException, e:
            pass

    def open_sql_url_no(self):  #读取数据库
        try:
            sql_data = "select * from url where bool='no'"
            print sql_data
            cursor = self.db.conn.cursor()
            n = cursor.execute(sql_data)
            cursor.scroll(0)
            for row in cursor.fetchall():
                url = row[0]
                s1,s2=self.url_http_200(url)
                try:
                    if s1==True:
                        sql_data = "update url set title='%s',bool='ok' where url='%s'" % (str(s2), url)
                        print sql_data
                        self.execute_sql(sql_data)
                    else:
                        sql_data = "update url set title='%s',bool='no' where url='%s'" % ("", url)
                        print sql_data
                        self.execute_sql(sql_data)
                except BaseException, e:
                    #print(str(e))
                    try:
                        sql_data = "update url set title='%s',bool='ok' where url='%s'" % (str(s2.decode("gbk")), url)
                        print sql_data
                        self.execute_sql(sql_data)
                    except BaseException, e:
                        pass
                    pass
        except BaseException, e:
            pass

    def url_http_200(self,url):
        try:
#            statusCode =urllib.urlopen(url).getcode()
#            #return statusCode==200  #返回 True  False
#            if statusCode==200:
#                #print "11111"
#                #local = url.split('/')[-1]
#                int_url_read=urllib.urlopen(url).read()
#                #print int_url_read
#                if len(int_url_read)>=10000:
#                    #print "url:%s   len:%d"%(url,int_url_read)
#                    p = re.compile(r'<title>(.*)</title>')
#                    sarr = p.findall(int_url_read)
#                    if len(sarr)>=1:
#                        return True,sarr[0]
#                    return True,""
#            return False,""
            req = urllib2.Request(url)
            req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
            s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
            int_url_read = s.read()
            if len(int_url_read)>=10000:
                #print "url:%s   len:%d"%(url,int_url_read)
                p = re.compile(r'<title>(.*)</title>')
                sarr = p.findall(int_url_read)
                if len(sarr)>=1:
                    return True,sarr[0]
                return True,""
            return False,""
        except BaseException, e:
            #print "xxxxxxxxxxxx",(str(e))
            return False,""

    def run(self):
        self.open_txt()  #添加到数据库
        #self.send_sql_url_ok()  #读取数据库
        while True:
            try:
                #print self.url_http_200("http://www.zhenhuashiye.com/ny75fwt/index.html")
                self.open_sql_url()  #读取数据库
                self.open_sql_url_ok()  #读取数据库
                self.open_sql_url_no()  #读取数据库
            except BaseException, e:
                print "xx",(str(e))
                pass
            # TODO 发布的时候时候一定要改为2秒
        print "sleep(2)"
        time.sleep(2)


def http_1(URL):
    try:
        req = urllib2.Request(URL)
        req.add_header('User-Agent',"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
        s = urllib2.urlopen(req,timeout=10)  # 超时10秒   #s = urllib2.urlopen(r"http://www.163.com")
        ss = s.read()
        print ss
    except BaseException, e:
        print "xx",(str(e))
        pass

if __name__=='__main__':
    #print http_1("http://www.zhenhuashiye.com/ny75fwt/index.html")
    h=web_title()



    #data=h.open_txt()

