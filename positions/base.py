import os
import random
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

class Page():

    # base_url="https://mantest.godteam.net/#/"
    # base_url = "https://mantest.godteam.net/#/"##外网
    base_url = "http://192.168.1.72:82/#/"  ##内网
    #初始化方法
    def __init__(self,driver,url=base_url):
        # self.requests = None
        self.driver = driver
        self.url = url
        self.time=3

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
        print(self.base_url+'IndexPage/'+url)
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

    def file_path(self):
        """
        os.walk，生成生成器
        :param file_dir: 文件绝对路径
        :return: 当前目录路径 ， 当前路径下的所有子目录 ，当前目录下的所有非目录子文件
        """
        file=''
        # files=os.walk(file_dir)####创建生成器
        # for i in files:
        #     file=i[2]
        #     print(file)

        files = os.walk(os.path.dirname(os.path.dirname(__file__)) + '/upload_img')
        for i in files:
            file=i[2]
        i = random.randint(0, len(file) - 1)
        # self.find_element(n).send_keys(
        #     os.path.dirname(os.path.dirname(__file__)) + '/upload_img/' + file[i])
        print('上传' + file[i])

        return os.path.dirname(os.path.dirname(__file__)) + '/upload_img/' + file[i]


