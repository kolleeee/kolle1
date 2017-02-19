# -*- coding: cp936 -*-  
import WebCrawler
#http://blog.csdn.net/fbd2011/article/details/7208194
url ='http://www.bbs020.net'  #设置入口url(例-->http://www.baidu.com): \n
thNumber = int(5)    #之前类型未转换出bug  设置线程数:
Maxdepth = int(5)  #最大搜索深度：
  
wc = WebCrawler.WebCrawler(thNumber, Maxdepth)  
wc.Craw(url) 