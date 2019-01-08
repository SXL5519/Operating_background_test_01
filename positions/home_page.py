from Elements.element import home_Page
from positions.base import Page

class Home_page(Page,home_Page):
    """
    首页元素操作
    """
    def text_home_page(self):
        self.wait_element_located(self.driver,self.home_page)
        obj=self.find_element(*self.home_page).text###读取首页“首页”文案
        print(obj)
        return obj