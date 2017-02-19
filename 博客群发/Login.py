#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
from selenium import webdriver
#from PIL import Image
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time


class   Login(object):
    def __init__(self,ui):
        self.ui=ui
        path = 'phantomjs-2.0.0-windows/bin/phantomjs.exe'
        self.driver = webdriver.PhantomJS(executable_path=path)
        from sc_data import sc_data   #文章生成
        self.sc_data=sc_data(self.ui)
        #newFirefox = webdriver.FirefoxProfile(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\06asfeco.default-1402969528759")
        #driver=webdriver.Firefox(newFirefox)

    def open_dl(self,url,username=None,password=None):  #登陆
        try:
            self.driver.get(url)
            time.sleep(2)
            self.driver.find_element_by_id("username").clear()#这个是以id选择元素
            self.driver.find_element_by_id("username").send_keys(str(username))
            self.driver.find_element_by_id("username").send_keys(Keys.TAB)
            #tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
            time.sleep(2)
            self.driver.find_element_by_id("password").send_keys(str(password))
            #通过定位密码框，enter（回车）来代替登陆按钮
            time.sleep(2)
            self.driver.find_element_by_id("password").send_keys(Keys.ENTER)
        except Exception, e:
            self.ui.messagebox.append(u"登陆 %s 异常"%(e))
            pass

    def fabu_blog(self,url,Title=None,Content=None): #发布博客
        try:
            self.driver.get(url)
            time.sleep(5)
            #driver.find_element_by_xpath("//div[@class='ml_r']/span/span/img")
            #driver.find_element_by_xpath("//*[@id='editorForm']/div[@class='BNE_content BNE_editor']/div[@class='editor_tit']/span/textarea").find_element_by_id("article_title").send_keys("11111111111")
            self.driver.find_element_by_id("article_title").send_keys(Title)
            self.driver.find_element_by_id("editor").send_keys(Content)
            time.sleep(3)
            facg=self.driver.find_element_by_id("articlePostBtn")
            if facg:
                facg.click()
                time.sleep(5)
                ok = self.driver.find_element_by_class_name('e_prompt_btn')
                if ok:
                    ok.click()
                    #print u"发布成功"
                    self.ui.messagebox.append(u"发布成功")
                    time.sleep(8)
                    #print self.driver.current_url
                    self.ui.messagebox.append(u"%s"%(self.driver.current_url))
        except Exception, e:
            self.ui.messagebox.append(u"发布 %s 异常"%(e))
            pass
    def long(self):
        self.driver=webdriver.Firefox()
        #self.driver.maximize_window()
        self.open_dl("http://login.sina.com.cn/signup/signin.php",self.ui.username_textEdit.toPlainText(),self.ui.password_textEdit.toPlainText())
        #self.driver.get("http://i.blog.sina.com.cn/blogprofile/index.php?com=1")

    def fb_wz(self):

        Title_data=self.ui.Title_textEdit.toPlainText()  #读取内容
        Title_data=u"%s"%(self.sc_data.sc_data(u"%s"%(Title_data)))  #写入内容

        Content_data=self.ui.Content_textEdit.toPlainText()  #读取内容
        Content_data=u"%s"%(self.sc_data.sc_data(u"%s"%(Content_data)))  #写入内容
        #print Title_data
        #print Content_data
        self.fabu_blog("http://control.blog.sina.com.cn/admin/article/article_add.php?is_new_editor=1",Title_data,Content_data) #发布博客