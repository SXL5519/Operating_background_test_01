from Elements.element import Log_in
from positions.base import Page



class login_operate(Page,Log_in):
    """
    登录页元素操作
    """
    def input_name(self):
        self.find_element(*self.neme).clear() ###清空内容
        self.find_element(*self.neme).send_keys('xingling')

    def ipput_passWord(self):
        self.find_element(*self.passWord).clear()  ###清空内容
        self.find_element(*self.passWord).send_keys('000000')

    def click_lofin_button(self):
        self.find_element(*self.login_submit).click()###点击登录按钮

    def log_in(self):
        self.input_name()
        self.ipput_passWord()
        self.click_lofin_button()
        print('登录成功')

