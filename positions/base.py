import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

class Page():

    # base_url="https://mantest.godteam.net/#/"
    base_url = "https://mantest.godteam.net/#/"
    #初始化方法
    def __init__(self,driver,url=base_url):
        # self.requests = None
        self.driver = driver
        self.url = url
        self.time=8

    #打开相应网址
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.time)

    #二次封装元素定位的方法
    def find_element(self,*loc):

        return self.driver.find_element(*loc)

    def find_elements(self, *loc):

        return self.driver.find_elements(*loc)

#二次封装显示等待的方法
    def wait_element_located(self,driver,locator):
        wait = WebDriverWait(driver,20)
        wait.until(EC.presence_of_element_located(locator))

    def Get(self,url):
        self.driver.get(self.base_url+'IndexPage/'+url)
        self.driver.implicitly_wait(self.time)



    def Slide_mouse01(self,n):
        """
        鼠标滑动到目标元素target
        :return:
        """
        target = self.find_element(*n)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def Slide_mouse02(self):
        """
        鼠标滑动到顶部
        :return:
        """
        js = "window.scroll(0,0)"
        self.driver.execute_script(js)

    def Slide_mouse03(self):
        """
        鼠标下拉到底部
        :return:
        """
        js = "window.scroll(0,10000000)"
        self.driver.execute_script(js)

    def screen_shot(self):
        """用于测试用例执行过程中的截图
        :param
        第一个当然是driver对象，
        第二个是保存的图片文件名，不用输.png"""
        a=time.strftime("%Y%m%d")
        path=os.path.exists('../image/'+a)
        if not path:
            os.mkdir('../image/'+a)
        top_dir = "../image/"+a+'/'
        times = time.strftime("%Y%m%d%H%M%S")
        image_file = top_dir + times + ".png"
        print(top_dir)
        print(image_file)
        self.driver.get_screenshot_as_file(image_file)


    def open_window_handle(self,i):
        """
        浏览器打开多个窗口时，切换到对应的浏览器窗口
        :return:
        """
        handles = self.driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        self.driver.switch_to_window(handles[i]) ##切换到对应的浏览器窗口

    def close_window_handle(self):
        """
        关闭当前浏览器窗口
        :return:
        """
        self.driver.close()


    def Get(self,url):
        """
        跳转到指定URL页面
        :param url:
        :return:
        """
        self.driver.get(url)
