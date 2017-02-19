#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#QQ29295842
##################################################
##if __name__=='__main__':
from selenium import webdriver
#from PIL import Image
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time
path = 'phantomjs-2.0.0-windows/bin/phantomjs.exe'
driver = webdriver.PhantomJS(executable_path=path)
driver=webdriver.Firefox()
#driver.set_window_size(1120,550)
driver.get("http://login.sina.com.cn/signup/signin.php")

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("17071827114")
driver.find_element_by_id("username").send_keys(Keys.TAB)
#tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
time.sleep(2)
driver.find_element_by_id("password").send_keys("120275151")
#通过定位密码框，enter（回车）来代替登陆按钮
time.sleep(2)
driver.find_element_by_id("password").send_keys(Keys.ENTER)

#print driver.find_element_by_id("check_img")
time.sleep(2)
driver.save_screenshot('screenshot.png') # 保存整个网页截图

#print driver.find_element_by_xpath("//div[@class='ml_r']/span/span/img").get_attribute('src') # find part of the page you want image of发现部分你要的页面图像



#向cookie的name 和value添加会话信息。
#cookie_str="""{u'domain': u'.sina.com.cn', u'name': u'Apache', u'value': u'125.39.131.87_1432720626.452259', u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'.sina.com.cn', u'name': u'SINAGLOBAL', u'expires': u'\u5468\u4e8c, 19 \u4e00\u6708 2038 03:00:00 GMT', u'value': u'125.39.131.87_1432720626.452257', u'expiry': 2147482800, u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'.sina.com.cn', u'name': u'ULV', u'expires': u'\u5468\u516d, 21 \u4e94\u6708 2016 09:53:39 GMT', u'value': u'1432720419705:1:1:1::', u'expiry': 1463824419, u'path': u'/', u'httponly': False, u'secure': False}, {u'domain': u'.sina.com.cn', u'name': u'UOR', u'expires': u'\u5468\u56db, 26 \u4e94\u6708 2016 09:53:39 GMT', u'value': u',login.sina.com.cn,', u'expiry': 1464256419, u'path': u'/', u'httponly': False, u'secure': False}"""
#driver.add_cookie({'name':'Apache', 'value':'125.39.131.87_1432720626.452259'})

#也可定位登陆按钮，通过enter（回车）代替click()
#driver.find_element_by_id("submit").send_keys(Keys.ENTER)
#driver.find_element_by_class_name("btn_submit").send_keys(Keys.ENTER)

#print '---', driver.page_source

# 获得cookie信息
cookie= driver.get_cookies()
#将获得cookie的信息打印
print cookie
#遍历cookies中的name 和value信息打印，当然还有上面添加的信息
#for cookie in driver.get_cookies():
#    print "%s -> %s" % (cookie['name'], cookie['value'])



#driver.find_element_by_id('kw').send_keys("realpython")
#driver.find_element_by_id("su").click()
#
#print driver.page_source
#print u'当前url:', driver.current_url
#print 'wd=realpython' in driver.current_url

#driver.quit()







