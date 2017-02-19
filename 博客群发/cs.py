#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#QQ29295842
##################################################

from selenium import webdriver
#from PIL import Image
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time
path = 'phantomjs-2.0.0-windows/bin/phantomjs.exe'
#driver = webdriver.PhantomJS(executable_path=path)
newFirefox = webdriver.FirefoxProfile(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\06asfeco.default-1402969528759")
driver=webdriver.Firefox(newFirefox)
#driver.maximize_window()
#firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
#os.environ["webdriver.firefox.bin"] = firefoxBin
#newFirefox = webdriver.FirefoxProfile()
#driver = webdriver.Firefox(newFirefox)

def open_dl(url,username=None,password=None):  #登陆
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_id("username").clear()#这个是以id选择元素
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("username").send_keys(Keys.TAB)
    #tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
    time.sleep(2)
    driver.find_element_by_id("password").send_keys(password)
    #通过定位密码框，enter（回车）来代替登陆按钮

def fabu_blog(url): #发布博客
    driver.get(url)
    time.sleep(5)
    #driver.find_element_by_xpath("//div[@class='ml_r']/span/span/img")
    #driver.find_element_by_xpath("//*[@id='editorForm']/div[@class='BNE_content BNE_editor']/div[@class='editor_tit']/span/textarea").find_element_by_id("article_title").send_keys("11111111111")
    driver.find_element_by_id("article_title").send_keys("22AAAAAAAAAAAA222222222222222222")
    driver.find_element_by_id("editor").send_keys("333333333")
    time.sleep(3)
    facg=driver.find_element_by_id("articlePostBtn")
    if facg:
        facg.click()
        time.sleep(5)
        ok = driver.find_element_by_class_name('e_prompt_btn')
        if ok:
            ok.click()
            print "发布成功"
            time.sleep(5)
            print driver.current_url
        #    driver.find_element_by_id("_9471432989564046_btn_close").send_keys(Keys.CLEAR)
#    time.sleep(2)
#    driver.find_element_by_id("article_title").clear()#这个是以id选择元素
#    driver.find_element_by_id("article_title").send_keys("11111111111")
#    time.sleep(2)
#    driver.find_element_by_id("editor").clear()#这个是以id选择元素
#    driver.find_element_by_id("editor").send_keys("222222222222222")
#    time.sleep(2)
#    driver.find_element_by_id("articlePostBtn").send_keys(Keys.ENTER)

if __name__=='__main__':
#    open_dl("http://login.sina.com.cn/signup/signin.php","17071827114","120275151")
#    time.sleep(20)
#    #遍历cookies中的name 和value信息打印，当然还有上面添加的信息
#    # 获得cookie信息
#    cookie= driver.get_cookies()
#    #将获得cookie的信息打印
#    print cookie
#
#    for cookie in driver.get_cookies():
#        print "%s -> %s" % (cookie['name'], cookie['value'])
    #driver.add_cookie({'name':'cREMloginname', 'value':'17071827114'})

    driver.get("http://i.blog.sina.com.cn/blogprofile/index.php?com=1")
    time.sleep(10)
    fabu_blog("http://control.blog.sina.com.cn/admin/article/article_add.php?is_new_editor=1")


