#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#mechanize 模拟提交表单登陆DZ BBS  QQ：29295842  希望技术交流     采集群发就看大家自己的了
#文档：http://wwwsearch.sourceforge.net/mechanize/
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import mechanize
import re, time

br = mechanize.Browser()
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
URL='http://bbs.sandaha.com/forum.php'

def bbs_long(url,username,password):
    try:
        br.open(url)  #登陆网址
        br.select_form(nr=0)##选择表单1，
        br.form['username'] = username
        br.form['password'] = password
        response = br.submit()  ##提交表单
        if response.read().decode('gbk').find(u'用户组')>-1:
            print u'登录成功'
        else:
            print u'登录失败'
    except:
        pass

def URL_TQURL(url): #URL提取URL
    try:
        #查看字符串结尾是否是/是就直接返回  http://www.383k.com/bbs/
        data=url[len(url)-1:len(url)]
        if data=="/":
            return url
        #截取字符串 http://www.383k.com/bbs/forum-4-1.html   http://www.383k.com/bbs/
        nPos =url.rfind('/') #查找字符  从尾部查找
        sStr1 = url[0:nPos+1] #复制指定长度的字符
        return sStr1
    except:
        pass

def bbs_sed_message(url):  #回帖
    try:
        br.open(url)
        #for f in br.forms():##有的页面有很多表单，你可以通过来查看
        #    print f
        br.select_form(nr=2)##选择表单1，
        br.form['message'] = 'ppppppppppppppppppppppppppppppppppppppppppppppppppp'
        response = br.submit()
        #print response.read().decode('gbk')
        if response.read().decode('gbk').find(u'回帖后跳转到最后一页')>-1:
            print u'回帖成功',url
        else:
            print u'回帖失败',url
    except:
        pass

def bbs_list(url):   #查询帖子列表
    try:
        response=br.open(url)
        data=response.read().decode('gbk')
        #print data
        p = re.compile( r'<a href=\"(.*?)\" onclick=\"atarget\(this\)\" class=\"s xst\">' )
        sarr = p.findall(data)
        url=URL_TQURL(url) #URL提取URL
        #for every in sarr:
        url2="%s%s"%(url,sarr[0])
        bbs_sed_message(url2)  #回帖
    except:
        pass

def bbs_fatie(url):  #发帖
    try:
        br.open(url)
        #for f in br.forms():##有的页面有很多表单，你可以通过来查看
        #    print f
        br.select_form(nr=1)##选择表单1，
        s1='Anonymous------你好中国'
        s2='DFFDFDFDFDFDFDFDFDF我非常好'
        br.form['subject'] = s1.decode('utf8').encode('gbk')
        br.form['message'] = s2.decode('utf8').encode('gbk')
        response = br.submit()  #提交表单
        data=response.read().decode('gbk')
        #print data
        #thread_url: 'http://bbs.sandaha.com/thread-291356-1-1.html',    新帖子的位置
        p = re.compile( r'thread_url: \'(.*?)\',' )
        sarr = p.findall(data)
        if str(sarr[0]).find('http')>-1:
            print '发帖成功',str(sarr[0])
        else:
            print '发帖失败'
    except BaseException, e:
        print(str(e))
        pass

#def bbs_ini():
#    try:
#
#    except:
#        pass
if __name__=='__main__':
    bbs_long(URL,'2602159946','2602159946')   #登陆
    #bbs_list('http://bbs.sandaha.com/forum-36-1.html')   #查询帖子列表    回帖
    bbs_fatie('http://bbs.sandaha.com/forum.php?mod=post&action=newthread&fid=36')  #发帖






