#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
###################################################
#对域名的处理
suffixes = 'ac','ad','ae','aero','af','ag','ai','al','am','an','ao','aq','ar','arpa','as',\
           'asia','at','au','aw','ax','az','ba', 'bb','bd','be','bf','bg','bh','bi','biz',\
           'bj','bm','bn','bo','br','bs','bt','bv','bw','by','bz','ca','cat','cc','cd','cf',\
           'cg','ch','ci','ck','cl','cm','cn','co','com','coop','cr','cu','cv','cx','cy',\
           'cz','de','dj','dk','dm','do','dz','ec','edu','ee','eg','er','es','et','eu','fi',\
           'fj','fk','fm','fo','fr','ga','gb','gd','ge','gf','gg','gh','gi','gl','gm','gn',\
           'gov','gp','gq','gr','gs','gt','gu','gw','gy','hk','hm','hn','hr','ht','hu','id',\
           'ie','il','im','in','info','int','io','iq','ir','is','it','je','jm','jo','jobs',\
           'jp','ke','kg','kh','ki','km','kn','kp','kr','kw','ky','kz','la','lb','lc','li',\
           'lk','lr','ls','lt','lu','lv','ly','ma','mc','md','me','mg','mh','mil','mk','ml',\
           'mm','mn','mo','mobi','mp','mq','mr','ms','mt','mu','mv','mw','mx','my','mz','na',\
           'name','nc','ne','net','nf','ng','ni','nl','no','np','nr','nu','nz','om','org','pa',\
           'pe','pf','pg','ph','pk','pl','pm','pn','pr','pro','ps','pt','pw','py','qa','re','ro',\
           'rs','ru','rw','sa','sb','sc','sd','se','sg','sh','si','sj','sk','sl','sm','sn','so',\
           'sr','st','su','sv','sy','sz','tc','td','tel','tf','tg','th','tj','tk','tl','tm','tn',\
           'to','tp','tr','tt','tv','tw','tz','ua','ug','uk','us','uy','uz','va','vc','ve','vg',\
           'vi','vn','vu','wf','ws','xn','ye','yt','za','zm','zw'

def xxx_www(domain):  #判断域名是否是二级域名 1是0否
    try:
        sdomain = []
        bdomain = False
        for section in domain.split('.'):
            if section in suffixes:
                sdomain.append(section)
                bdomain = True
            else:
                sdomain = [section]
            #return '.'.join(sdomain) if bdomain  else ''
        if bdomain:
            if (len(domain)-len('.'.join(sdomain)))>=2:
                return 1
            else:
                return 0
        else:
            return 0
    except:
        return 0

def get_sdomain(domain):  #域名拆解www.baidu.com->baidu.com
    try:
        sdomain = []
        bdomain = False
        for section in domain.split('.'):
            if section in suffixes:
                sdomain.append(section)
                bdomain = True
            else:
                sdomain = [section]
        return '.'.join(sdomain) if bdomain  else ''
    except:
        return 0

def www_com(domain):  #获取域名  后辍名
    sdomain = []
    bdomain = False
    for section in domain.split('.'):
        if section in suffixes:
            sdomain.append(section)
            bdomain = True
    return '.'.join(sdomain) if bdomain  else ''

def www_www(url): #排除一些违规域名
    try:
        for L in [":","?","=","%","&",";","|",","]:
            if url.__contains__(L):
                return 0
        if len(url)>=4: #判断 域名长度应该大于>=4字节为真域名
            return 1
        return 0
    except:
        return 0

