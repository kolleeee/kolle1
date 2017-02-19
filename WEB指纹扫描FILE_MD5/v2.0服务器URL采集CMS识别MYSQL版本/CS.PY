#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
###################################################
import xx_com_cn_xx #对域名拆分

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
################################################
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

if __name__=='__main__':
    data="baidu.com.cn"  #判断域名是否是二级域名 1是0否
    print xxx_www(data)
