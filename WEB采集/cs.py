# -*- coding: utf-8 -*-
import top.api

url="http://gw.api.tbsandbox.com/router/rest?sign=3EF0F6A67258EDA0B763CCFAA369496B&timestamp=2013-09-11+00%3A01%3A26&v=2.0&app_key=1012129701&method=taobao.taobaoke.caturl.get&partner_id=top-apitools&format=xml&cid=55656"
port=80

secret="D53AF741A19BF1F973C7B5550E4C64E6"
appkey="1012129701"
req=top.api.TaobaokeCaturlGetRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.cid=0
try:
    resp= req.getResponse()
    print(resp)
except Exception,e:
    print(e)