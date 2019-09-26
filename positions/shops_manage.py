import random
from time import sleep

import os

from Elements.element import shops_manage
from positions.base import Page


class Shops_Manage(shops_manage,Page):
    """
    商家管理元素操作
    """
    def Shops_manage_click(self):
        """
        点击商家管理
        :return:
        """
        self.find_element(*self.Shops_manage).click()

    def Shops_check_in(self):
        """
        点击商家入驻
        :return:
        """
        self.find_element(*self.shops_check_in).click()

    def Create_account(self):
        """
        点击开通商家账号
        :return:
        """
        self.wait_element_located(self.driver,self.create_account)
        self.find_element(*self.create_account).click()

    def Shops_id(self):
        """
        输入商家账号
        :return:
        """
        n=str(random.randint(1,1000))
        self.find_element(*self.shops_id).send_keys('sxl123')
        print('输入的商家账号为：sxl123')

    def Shops_password(self):
        """
        输入商家密码
        :return:
        """
        self.find_element(*self.shops_password).send_keys('123456')
        print('输入密码为：123456')

    def Shops_num(self):
        """
        输入艾家编号
        :return:
        """
        n=str(random.randint(5000,100000))
        self.find_element(*self.shops_num).send_keys(n)
        print('艾家编号为：'+n)

    def Shops_name(self):
        """
        输入商家名称
        :return:
        """
        self.find_element(*self.shops_name).send_keys('sxl123')
        print('商家名称为：sxl123')

    def Shop_name(self):
        """
        输入店铺名称
        :return:
        """
        self.find_element(*self.shop_name).send_keys('sxl123')
        print('店铺名称为：sxl123')

    def Key_word(self):
        """
        输入搜索关键字
        :return:
        """
        self.find_element(*self.key_word).send_keys('sxl')
        print('输入搜索关键字为：sxl')

    def Shops_logo(self):
        """
        上传店铺LOGO
        :return:
        """
        # file=self.file_path(os.path.dirname(os.path.dirname(__file__))+'/upload_img')
        # i=random.randint(0,len(file)-1)
        self.find_elements(*self.shops_logo)[0].send_keys(self.file_path())
        print('上传成功')

    def Shops_photo(self):
        """
        上传店铺展示图
        :return:
        """
        # file = self.file_path(os.path.dirname(os.path.dirname(__file__)) + '/upload_img')
        # i = random.randint(0, len(file) - 1)
        self.find_elements(*self.shops_logo)[1].send_keys(self.file_path())
        print('上传成功')

    def Company_name(self):
        """
        输入公司名称
        :return:
        """
        self.find_element(*self.company_name).send_keys('sdfdsfsdf')

    def Company_certifyNO(self):
        """
        输入营业执照注册号
        :return:
        """
        self.find_element(*self.company_certifyNO).send_keys('123456789987')

    def Company_certifyName(self):
        """
        输入法定代表人姓名
        :return:
        """
        self.find_element(*self.company_certifyName).send_keys('哈哈')

    def Company_identityNo(self):
        """
        输入身份证号
        :return:
        """
        self.find_element(*self.company_identityNo).send_keys('123456987456')

    def Business_license(self):
        """
        点击营业执照
        :return:
        """
        self.find_elements(*self.business_license)[3].click()

    def Bank_companyName(self):
        """
        输入银行公司名称
        :return:
        """
        self.find_element(*self.bank_companyName).send_keys('shjfsdf')

    def Bank(self):
        self.find_element(*self.bank).click()

    def Bank_blankNo(self):
        """
        输入公司银行账号
        :return:
        """
        self.find_element(*self.bank_blankNo).send_keys('1234567899874561')

    def Bank_blankName(self):
        """
        输入开户行银行名称
        :return:
        """
        self.find_element(*self.bank_blankName).send_keys('sfsdf')

    def Other(self):
        self.find_element(*self.other).click()

    def Shop_grade(self):
        """
        点击商家等级
        :return:
        """
        self.wait_element_located(self.driver,self.shop_grade)
        self.find_element(*self.shop_grade).click()

    def Merchant_companyGrade(self):
        """
        输入商家等级
        :return:
        """
        self.find_element(*self.merchant_companyGrade).send_keys("校园配送")

    def Shop_class(self):
        """
        点击商家类别
        :return:
        """
        self.wait_element_located(self.driver, self.shop_class)
        self.find_element(*self.shop_class).click()

    def Merchant_companyType(self):
        """
        输入商家类别
        :return:
        """
        self.find_element(*self.merchant_companyType).send_keys('四川地区艾家')

    def Submit(self):
        """
        点击提交按钮
        :return:
        """
        self.find_element(*self.submit).click()
        self.find_element(*self.submit).click()
        print('商家添加成功')

    def Placeholder(self,n):
        """
        点击商家账号输入框，并输入 n
        :return:
        """
        self.wait_element_located(self.driver,self.placeholder)
        self.find_element(*self.placeholder).clear()
        self.find_element(*self.placeholder).send_keys(n)

    def Text_Value(self,m):
        """
        数据读取
        n:标签tr 行数
        m: 标签td 列数
        :return:
        """
        mur=self.find_element(*self.Text_value(self.Shop_nu()[1],m)).text
        print(mur)
        return mur

    def Shop_nu(self):
        """
        当前页面商家总数
        :return:
        """
        c=0
        a=self.find_elements(*self.shop_nu)
        if len(a)>0:
            c=random.randint(1,len(a))
        else:
            print('当前页无数据')
        return len(a),c

    def Query(self):
        """
        点击查询按钮
        :return:
        """
        self.find_element(*self.query).click()

    def Store_name(self,n):
        """
        输入店铺名称
        :return:
        """
        self.find_element(*self.store_name).send_keys(n)

    def Store_grade(self):
        """
        选择店铺等级
        :return:
        """
        self.find_element(*self.store_grade).click()
        self.wait_element_located(self.driver,self.grade)
        a=self.find_elements(*self.grade)
        n=random.randint(2,len(a))
        b=self.find_element(*self.grade_N(n)).text
        print(b)
        self.find_element(*self.grade_N(n)).click()
        return b

    def Remain_sum_and_recharge(self):
        """
        点击充值按钮
        :return: n-产生的随机数；a-显示的可用余额
        """
        b=self.find_elements(*self.shop_nu)
        n=random.randint(1,len(b))
        print(n)
        a=self.text_Remain(n)
        self.find_element(*self.remain_sum_and_recharge(n,2)).click()
        return n,a

    def text_Remain(self,n):
        """
        读取可用余额
        :return:
        """
        a = self.find_element(*self.remain_sum_and_recharge(n, 1)).text
        print('剩余的可用余额为：'+a)
        return a


    def Recharge_money(self):
        """
        输入充值金额
        :return:
        """
        n=random.randint(100,1000)
        self.find_element(*self.recharge_money).clear()
        print('输入充值金额为：'+str(n))
        self.find_element(*self.recharge_money).send_keys(n)
        return n

    def Recharge_Confirm_or_Cancel(self):
        """
        点击充值确认或者取消按钮
        :return:
        """
        self.find_element(*self.Recharge_Confirm_or_cancel(2)).click()