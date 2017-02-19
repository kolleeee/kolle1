#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#requests 模拟提交表单登陆DZ BBS  为啥登陆不成功呢  请指教  QQ29295842
################################################
'''
import re
import requests as rq
#全局变量
s = rq.session()
if __name__=='__main__':
    lgurl='http://bbs.sandaha.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LvEpL&inajax=1'
    get_formhash_url='http://bbs.sandaha.com/forum.php?action=login'
    login_page = s.get(get_formhash_url).content
    #<input type="hidden" name="formhash" value="e936919d" />
    p = re.compile( r'<input type="hidden" name="formhash" value="(.*?)" />')
    sarr = p.findall(login_page)
    print sarr[0]  #获取当前formhash

    #表单数据
    postData = {
        'formhash':sarr[0],
        'referer':'http://bbs.sandaha.com/forum.php?action=login',
        'loginfield':'username',
        'username':'2602159946',
        'password':'2602159946',
        'questionid':0,
        'answer':None    }
    #Content-Length: 81
    #fastloginfield=username&username=123&password=12312&quickforward=yes&handlekey=ls
    hds = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
    r = s.post(url =lgurl,data =postData, headers = hds)
    r2 = s.get(url =get_formhash_url)
    fp=open('dz.html','a+')
    fp.write(r2.text.encode('utf8').decode('ascii','ignore'))
    fp.close()
#    html = r.text.encode(r.encoding).decode('gbk')
#    #print html
'''

def file_data(data):
    data2=""
    try:
        n=5
        intn=len(data)/n
        for i in range(n):
         #if len(data)>=intn:
            data2+=data[0:intn]  #复制指定长度的字符
            data2+="1122233344\n"
            data=data[intn:] #字符串删除
        return data2
    except BaseException, e:
        print(str(e))
        return data2

data=u"昨天(12月25日)緋闻小三温心的经理人公司先发表声明，否认温心跟黄晓明拍拖，两人是“认识超过两年的好友”，还“谢谢黄晓明邀请的晚餐，额外赠送了一次头条”。黄晓明下午发表严正声明，强调报道严重失实，将会采取法律行动。声明强调黄晓明跟温心不熟，指“温小姐是朋友带来的”，并非黄晓明邀请，反驳温心自称跟黄晓明是好朋友。黄晓明还讽刺温心炒作宣传：“遗憾新人为求知名度所采取的手段。娱乐圈的路还很长，祝福新人温小姐近期上映的电影大卖。”"
print file_data(data)
#print len(data)
#




