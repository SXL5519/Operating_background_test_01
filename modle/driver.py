from selenium import webdriver
import os
"""
class Browser:
    def __init__(self):
       self.driver = webdriver.PhantomJS()

    def get_driver(self):
        return self.driver
"""



class Chrome():
    # 配置谷歌浏览器模拟'Galaxy S5'手机打开浏览器
    # mobileEmulation = {'deviceName': 'Galaxy S5'}
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('mobileEmulation', mobileEmulation)
    # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    #驱动最大化打开谷歌浏览器
    def browser_chrome(self):
        # print(os.path.abspath('./')+'\\Application60\\chromedriver.exe')
        self.driver=webdriver.Chrome(executable_path=os.path.abspath('..')+'\\Application60\\chromedriver.exe')

        self.driver.maximize_window()

        return self.driver