#!/usr/bin/env python
#-*- coding: UTF-8 -*-
__author__ = 'Jekkay Hu'

#import os
#import sys
#print sys.path
#skyeyepath = os.path.realpath((os.path.dirname(__file__)) + "/../")
#if not skyeyepath in sys.path:
#    sys.path.append(skyeyepath)

## 服务器的配置文件路径
#cfgpath = "server.ini"
##cfgpath = os.path.realpath((os.path.dirname(__file__)) + "/../server.ini")

#对域名的处理
suffixes = ['ac', 'ad', 'ae', 'aero', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'arpa', 'as',
            'asia', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'biz',
            'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cat', 'cc', 'cd', 'cf',
            'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'com', 'coop', 'cr', 'cu', 'cv', 'cx', 'cy',
            'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'edu', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'fi',
            'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn',
            'gov', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id',
            'ie', 'il', 'im', 'in', 'info', 'int', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jobs',
            'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li',
            'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mil', 'mk', 'ml',
            'mm', 'mn', 'mo', 'mobi', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na',
            'name', 'nc', 'ne', 'net', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'org', 'pa',
            'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'pro', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro',
            'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so',
            'sr', 'st', 'su', 'sv', 'sy', 'sz', 'tc', 'td', 'tel', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn',
            'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg',
            'vi', 'vn', 'vu', 'wf', 'ws', 'xn', 'ye', 'yt', 'za', 'zm', 'zw']


#def xxx_www(domain):
def is_subdomain(domain):
    #判断域名是否是二级域名 1是0否
    try:
        sdomain = []
        bdomain = False
        for section in domain.split('.'):
            if section in suffixes:
                sdomain.append(section)
                bdomain = True
            else:
                sdomain = [section]
        if bdomain:
            if (len(domain.split('.'))-len(sdomain)) >= 1:
                return 1
        return 0
    except:
        return 0


#def get_sdomain(domain):
def trim_sdomain(domain):
    #域名拆解www.baidu.com->baidu.com
    try:
        sdomain = []
        bdomain = False
        for section in domain.split('.'):
            if section in suffixes:
                sdomain.append(section)
                bdomain = True
            else:
                sdomain = [section]
        return '.'.join(sdomain) if bdomain else domain
    except:
        pass

def URL_TQURL(data): #URL提取URL
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
        print "Extract URL:%s URL error"%\
              (data)

#def www_com(domain):
def get_domain_suffix(domain):
    #获取域名的后辍名
    sdomain = []
    bdomain = False
    for section in domain.split('.'):
        if section in suffixes:
            sdomain.append(section)
            bdomain = True
        else:
            sdomain = []
    return '.'.join(sdomain) if bdomain else None


#def www_www(url):
def is_legal_domain(domain):
    #排除一些违规域名
    try:
        #判断 域名长度应该大于>=4字节为真域名
        if len(domain) < 4:
            return 0
        for i in xrange(len(domain)):
            if domain[i] == '.' or domain[i] == '-':
                continue
            if domain[i].isdigit() or domain[i].isalpha():
                continue
            return 0
        return 1
    except:
        pass

if __name__ == '__main__':
    assert is_subdomain('www.baidu.com')
    assert not is_subdomain('baidu.com')
    assert not is_subdomain('ruc.edu.cn')
    assert is_subdomain('www.ruc.edu.cn')
    assert is_subdomain('tieba.baidu.com')
    assert is_subdomain('cn.baidu.com')


    assert 1 == is_legal_domain('www.baidu.com')
    assert 1 == is_legal_domain('www.baid2-u.com')
    assert 0 == is_legal_domain('www.baid2-u.com?123')
    assert 1 == is_legal_domain('w.12.1')