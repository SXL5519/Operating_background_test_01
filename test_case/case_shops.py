from positions.shops_manage import Shops_Manage
from time import sleep
from test_case.mytest import MyTest
from positions.login import login_operate
from positions.home_page import Home_page

class shops_manage(MyTest):
    def test_shops_check_in(self):
        """验证商家入驻"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        # ha.screen_shot()
        ha.Get("ShopDetail/0/edit")
        hb = Shops_Manage(self.driver)
        hb.Create_account()
        hb.Shops_id()
        hb.Shops_password()
        hb.Shops_num()
        hb.Shops_name()
        hb.Shop_name()
        hb.Shops_logo()
        hb.Key_word()
        hb.Shops_photo()
        hb.Business_license()
        hb.Company_name()
        hb.Company_certifyNO()
        hb.Company_certifyName()
        hb.Company_identityNo()
        hb.Bank()
        hb.Bank_companyName()
        hb.Bank_blankNo()
        hb.Bank_blankName()
        hb.Other()
        sleep(1.5)
        hb.Shop_grade()
        hb.Merchant_companyGrade()
        sleep(1.5)
        hb.Shop_class()
        hb.Merchant_companyType()
        sleep(1.5)
        hb.Submit()

    def test_placeholder_query(self):
        """验证商家ID查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Shop")
        hb = Shops_Manage(self.driver)
        obj=hb.Text_Value(2)
        hb.Placeholder(obj)
        hb.Query()
        sleep(1)
        if hb.Shop_nu()[0]>0:
            mur=hb.Text_Value(2)
            self.assertEqual(obj,mur)
        else:
            raise Exception('查询无数据')

    def test_shop_ID_query(self):
        """验证商家ID查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Shop")
        hb = Shops_Manage(self.driver)
        obj=hb.Text_Value(3)
        hb.Placeholder(obj)
        hb.Query()
        sleep(1)
        if hb.Shop_nu()[0]>0:
            mur=hb.Text_Value(3)
            self.assertEqual(obj,mur)
        else:
            raise Exception('查询无数据')

    def test_store_name(self):
        """验证商家名称查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Shop")
        hb = Shops_Manage(self.driver)
        obj = hb.Text_Value(4)
        hb.Store_name(obj)
        hb.Query()
        sleep(1)
        if hb.Shop_nu()[0] > 0:
            mur = hb.Text_Value(4)
            self.assertEqual(obj, mur)
        else:
            raise Exception('查询无数据')

    def test_store_grade(self):
        """验证商家等级查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Shop")
        hb = Shops_Manage(self.driver)
        sleep(1)
        obj = hb.Store_grade()
        hb.Query()
        sleep(1)
        if hb.Shop_nu()[0] > 0:
            mur = hb.Text_Value(5)
            self.assertEqual(obj, mur)
        else:
            raise Exception('查询无数据')


    def test_store_Recharge(self):
        """验证商家充值"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Shop")
        hb = Shops_Manage(self.driver)
        mur=hb.Remain_sum_and_recharge()
        n=hb.Recharge_money()
        hb.Recharge_Confirm_or_Cancel()
        sleep(1.5)
        obj=hb.text_Remain(mur[0])
        self.assertEqual(str(int(mur[1])+n),str(obj))
        sleep(10)

