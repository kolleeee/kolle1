# -*- coding: utf-8 -*-
#windows  #无控制台 
#console   #有控制台

from distutils.core import setup  

import py2exe
#如果你要创建一个图形用户界的程序，那么你只需要将mysetup.py中的console=["helloworld.py"]替换为windows=["myscript.py"]既可。
#windows  不会显示控制台窗口
#setup(version = "1.0",description = "QQ:2602159946",
#      name = "opurl",zipfile=None,
#    console=[{"script": "opurl.py", "icon_resources": [(1, "App.ico")]}],
#      options={"py2exe":{"includes":["sip"]}},
#    includes = ["list.py"],includes1 = ["mysql.py"])

setup(version = "baidu-google-bing_URL",description = "QQ:29295842",
    name = "postadmin",zipfile=None,
    console=[{"script": "baidu-google-bing_URLTQ.py", "icon_resources": [(1,"App.ico")]}],
    options={"py2exe":{"includes":["baidu-google-bing_URLTQ"]}},
    includes1 = ["list.py"])

#includes1 = ["Cthread.py","Cclose_open.py","internet_close.dll","Ctitle.py","ClinkFTP.py","Cmysql.py","Cmysql_delete.py","Copenftp.py","Copenurl.py","CpasswordFTP.py","list.py"])
