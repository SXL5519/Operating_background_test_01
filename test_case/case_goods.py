from test_case.mytest import MyTest
from positions.login import login_operate
from positions.home_page import Home_page
from positions.commodity_management import Commodity_Management
from positions.shops_manage import Shops_Manage
from time import sleep

class My_home_case(MyTest):

    def test_login_case(self):
        '''验证登录'''
        ha=login_operate(self.driver)
        hb=Home_page(self.driver)
        ha.open()###打开浏览器
        ha.log_in()
        obj=hb.text_home_page()
        self.assertEqual(obj,"首页")###断言
    #
    # def test_add_commodity(self):
    #     """验证添加商品页面跳转"""
    #     ha = login_operate(self.driver)
    #     ha.open()  ###打开浏览器
    #     ha.log_in()
    #     hb=Commodity_Management(self.driver)
    #     hb.click_commodity_management()
    #     hb.click_add_commodity()
    #     obj=hb.text_select_sort()
    #     self.assertEqual(obj,"选择分类")

    def test_click_class(self):
        """验证添加商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("AddGoods")
        hb = Commodity_Management(self.driver)
        hb.click_one_class()
        hb.click_too_class()
        hb.click_three_class()
        hb.click_next_1()
        obj=hb.Information()
        self.assertEqual(obj,'基本信息')
        obj=hb.Commdity_name()
        hb.Subhead()
        hb.Shops()
        sleep(2)
        hb.Shops_Select()
        hb.Shops_presentation()
        hb.Freight()
        hb.Cost_price()
        hb.Selling_price()
        hb.Market_price()
        hb.SaleNumBase()
        hb.BaseTransWeight()
        hb.AddTransWeight()
        hb.AddTransPrice()
        hb.Next_2()
        hb.Shops_attribute()
        sleep(2)
        hb.Select_Shops_attribute()
        sleep(2)
        hb.Specification_Goods()
        hb.KG_input()
        hb.Early_warn()
        sleep(1)
        hb.Upload_pictures()
        hb.Select_pictures()
        sleep(1)
        hb.Default()
        hb.Commdity_album()
        sleep(1)
        hb.Next_3()
        sleep(1)
        hb.Relevance_Commdity()
        sleep(1)
        hb.Anticon_right()
        hb.Submit()
        hb.assert_addcommdity()
        sleep(3)
        num=hb.Commdity_name_list()
        self.assertEqual(obj,num)

    def test_shops_list_allshops(self):
        """验证商品列表，全部商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(1)
        mur=hb.text_all_shops(1)
        if int(mur) > 0:
            obj=hb.text_shops_num()
            self.assertEqual(mur,obj)
        else:
            print('无数据')


    def test_shops_list_In_the_shelf(self):
        """验证商品列表，上架中商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(2)
        mur=hb.text_all_shops(2)
        if int(mur) > 0:
            sleep(1.5)
            obj=hb.text_shops_num()
            self.assertEqual(mur,obj)
        else:
            print('无数据')


    def test_shops_list_The_shelves(self):
        """验证商品列表，下架中商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(3)
        mur=hb.text_all_shops(3)
        if int(mur) > 0:
            sleep(1.5)
            obj=hb.text_shops_num()
            self.assertEqual(mur,obj)
        else:
            print('无数据')

    def test_shops_list_To_audit(self):
        """验证商品列表，待审核商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(4)
        mur=hb.text_all_shops(4)
        if int(mur) > 0:
            sleep(1.5)
            obj=hb.text_shops_num()
            self.assertEqual(mur,obj)
        else:
            print('无数据')

    def test_shops_list_approve(self):
        """验证商品列表，审核通过"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(5)
        sleep(1)
        mur=hb.text_all_shops(5)
        if int(mur)>0:
            sleep(1.5)
            obj=hb.text_shops_num()
            self.assertEqual(mur,obj)
        else:
            print('无数据')

    def test_shops_list_disapprove(self):
        """验证商品列表，审核不通过"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(6)
        mur=hb.text_all_shops(6)
        if int(mur)>0:
            sleep(1.5)
            obj=hb.text_shops_num()
            self.assertEqual(mur,obj)
        else:
            print('无数据')

    def test_shops_list_sell_out(self):
        """验证商品列表，售罄"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(7)
        mur=hb.text_all_shops(7)
        if int(mur)>0:
            sleep(1.5)
            obj=hb.text_shops_num()
            self.assertEqual(mur,obj)
        else:
            print('无数据')

    def test_shops_list_search(self):
        """以商品编号查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        mur=hb.shops_list_search(3)
        hb.assert_addcommdity1()
        sleep(1)
        obj=hb.SHop_num1(3)
        self.assertEqual(mur,obj)

    def test_shops_list_Shop_class(self):
        """以商品分类查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.Shop_class_input()
        mur=hb.SHOP_Classs()
        hb.assert_addcommdity1()
        sleep(1)
        obj=hb.Shop_Type(7)
        if obj!=0:
            self.assertIn(mur,obj)
        else:
            print('该分类无商品')

    def test_shops_list_Shop_name(self):
        """以商家名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.Shop_name_input()
        mur=hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1.5)
        obj = hb.Shop_Type(3)
        if obj!=0:
            self.assertIn(mur[:2],obj)
        else:
            print('该商家无商品')

    def test_shops_list_group_query1(self):
        """上架中，以编号，分类，名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(2)
        hb.Shop_class_input()
        sleep(1)
        mur1 = hb.SHOP_Classs()
        hb.Shop_name_input()
        mur2 = hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1)
        obj1 = hb.Shop_Type(3)
        obj2 = hb.Shop_Type(7)
        if obj1 != 0:
            self.assertIn(mur1, obj2)
            self.assertIn(mur2[:2], obj1)
        else:
            print('无商品')

    def test_shops_list_group_query2(self):
        """下架中，以编号，分类，名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(3)
        hb.Shop_class_input()
        sleep(1)
        mur1 = hb.SHOP_Classs()
        hb.Shop_name_input()
        mur2 = hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1)
        obj1 = hb.Shop_Type(3)
        obj2 = hb.Shop_Type(7)
        if obj1 != 0:
            self.assertIn(mur1, obj2)
            self.assertIn(mur2[:2], obj1)
        else:
            print('无商品')

    def test_shops_list_group_query3(self):
        """待审核，以编号，分类，名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(4)
        hb.Shop_class_input()
        sleep(1.5)
        mur1 = hb.SHOP_Classs()
        hb.Shop_name_input()
        mur2 = hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1)
        obj1 = hb.Shop_Type(3)
        obj2 = hb.Shop_Type(7)
        if obj1 != 0:
            self.assertIn(mur1, obj2)
            self.assertIn(mur2[:2], obj1)
        else:
            print('无商品')

    def test_shops_list_group_query4(self):
        """审核通过，以编号，分类，名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(5)
        hb.Shop_class_input()
        sleep(1.5)
        mur1 = hb.SHOP_Classs()
        hb.Shop_name_input()
        mur2 = hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1.5)
        obj1 = hb.Shop_Type(3)
        obj2 = hb.Shop_Type(7)
        if obj1 != 0:
            self.assertIn(mur1, obj2)
            self.assertIn(mur2[:2], obj1)
        else:
            print('无商品')

    def test_shops_list_group_query5(self):
        """审核不通过，以编号，分类，名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(6)
        hb.Shop_class_input()
        sleep(1.5)
        mur1 = hb.SHOP_Classs()
        hb.Shop_name_input()
        sleep(0.5)
        mur2 = hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1.5)
        obj1 = hb.Shop_Type(3)
        obj2 = hb.Shop_Type(7)
        if obj1 != 0:
            self.assertIn(mur1, obj2)
            self.assertIn(mur2[:2], obj1)
        else:
            print('无商品')

    def test_shops_list_group_query6(self):
        """售罄，以编号，分类，名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(7)
        hb.Shop_class_input()
        sleep(1.5)
        mur1 = hb.SHOP_Classs()
        hb.Shop_name_input()
        sleep(0.5)
        mur2 = hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1.5)
        obj1 = hb.Shop_Type(3)
        obj2 = hb.Shop_Type(7)
        if obj1 != 0:
            self.assertIn(mur1, obj2)
            self.assertIn(mur2[:2], obj1)
        else:
            print('无商品')

    def test_revise_food_stamps(self):
        """修改粮票规则"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.click_all_shops(3)
        sleep(1)
        hb.Shop_list_checkbox()
        hb.Revise_food_stamps()
        hb.Food_stamps()
        mur=hb.Foog_Stamps()
        hb.Revise_Food_stamps_confirm()
        sleep(1.5)
        obj=hb.Shop_Type(5)
        if obj != 0:
            self.assertIn(obj[5:],mur)
        else:
            print('无商品')

    def test_putaway_shop(self):
        """点击上架按钮"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        hb.click_all_shops(3)
        sleep(1)
        A=hb.PUtaway()
        hb.click_all_shops(2)
        hb.Search(A)
        hb.assert_addcommdity1()
        sleep(3)
        if hb.Shop_amount()>0:
            B=hb.SHop_num1(3)
            self.assertEqual(A,B)
            value=hb.text_class_value()
            self.assertEqual(value,'ant-switch ant-switch-checked')
            obj=hb.Audition_text()
            self.assertIn(obj,'待审核,审核不通过,审核通过')
        else:
            raise Exception('查询商品编号为空')

    def test_autid_button(self):
        """验证审核按钮"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.click_all_shops(4)
        sleep(3)
        mur=hb.Audit_button()
        sleep(1)
        hb.Audit_pass()
        hb.Audit_ion(2)
        sleep(1)
        hb.click_all_shops(1)
        sleep(3)
        hb.Search(mur)
        sleep(0.5)
        hb.assert_addcommdity1()
        # sleep(10)
        if hb.Shop_amount() > 0:
            obj = hb.Audition_text()
            self.assertEqual(obj, '审核通过')
            print('审核通过')
        else:
            raise Exception('查询商品编号为空')

    def test_delete_shop(self):
        """验证删除上架商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.click_all_shops(2)
        hb.Delete_shop()
        sleep(1)
        hb.Delete_affirm(2)
        mur=hb.text_error_massage()
        self.assertEqual(mur,'请先下架该商品')

    def test_delete_shop01(self):
        """验证删除下架商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.click_all_shops(3)
        sleep(2)
        obj=hb.Delete_shop()
        sleep(1)
        hb.Delete_affirm(2)
        hb.Search(obj)
        hb.assert_addcommdity1()
        sleep(3)
        if hb.Shop_amount() == 0:
            # hb.Get(self.url + "GoodsStation")
            print('删除成功')
        else:
            raise Exception('删除失败')



    def test_page_break(self):
        """验证切换分页下拉框"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsList")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.Slide_mouse03()
        hb.Page_nu()
        obj=hb.Page()
        sleep(3)
        mur=hb.Shop_amount()
        print(mur)
        self.assertEqual(obj,mur)


    def test_delete_shop_search(self):
        """商品回收站页面，验证搜索商品编码"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsStation")
        hb = Commodity_Management(self.driver)
        sleep(1)
        obj=hb.shops_list_search(2)
        hb.assert_addcommdity1()
        mur=hb.SHop_num1(2)
        self.assertEqual(obj,mur)

    def test_delete_shops_list_Shop_class(self):
        """商品回收站页面，验证以商品分类查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsStation")
        hb = Commodity_Management(self.driver)
        hb.Shop_class_input()
        mur=hb.delete_shop_Classs()
        hb.assert_addcommdity1()
        sleep(2)
        obj=hb.Shop_amount()
        if obj!=0:
            ob = hb.SHop_num1(5)
            self.assertIn(ob,mur)
        else:
            print('该分类无商品')

    def test_delete_shops_list_Shop_name(self):
        """商品回收站页面，以商家名称查询商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsStation")
        hb = Commodity_Management(self.driver)
        hb.Shop_name_input()
        hb.Shop_Name()
        hb.assert_addcommdity1()
        sleep(1.5)
        obj = hb.Shop_amount()
        if obj!=0:
            print('查询成功')
        else:
            print('该商家无商品')

    def test_delete_shops_restore(self):
        """商品回收站页面，还原商品"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsStation")
        hb = Commodity_Management(self.driver)
        obj=hb.click_restore()
        hb.Delete_affirm(2)
        hb.Search(obj)
        hb.assert_addcommdity1()
        sleep(1)
        mur = hb.Shop_amount()
        if mur!= 0:
            raise Exception('商品还原失败')
        else:
            print('商品还原成功')

    def test_delete_page_break(self):
        """商品回收站页面，验证切换分页下拉框"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsStation")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.Slide_mouse03()
        hb.Page_nu()
        obj=hb.Page()
        sleep(3)
        mur=hb.Shop_amount()
        print(mur)
        self.assertEqual(obj,mur)


    def test_delete_shop_class_and_name(self):
        """商品回收站，以商品分类和商家名称查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsStation")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.Shop_class_input()
        mur = hb.delete_shop_Classs()
        hb.Shop_name_input()
        mur1=hb.Shop_Name()
        hb.assert_addcommdity1()
        if hb.Shop_amount()>0:
            obj1=hb.text_value(1,4)
            obj=hb.text_value(1, 5)
            self.assertEqual(mur,obj)
            self.assertEqual(mur1,obj1)
        else:
            print('查询无数据')

    def test_goods_evaluate(self):
        """商品评价,按商品名称查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Evaluate")
        hb = Commodity_Management(self.driver)
        sleep(1)
        mur=hb.text_good_evaluate_name(4)[0]
        print('商品名称：'+mur)
        hb.Search_input(mur)
        hb.Search_click()
        obj=hb.text_good_evaluate_name(4)[0]
        print('搜索结果的商品名称：'+obj)
        self.assertEqual(mur,obj)

    def test_goods_evaluate_username(self):
        """商品评价，按用户昵称查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Evaluate")
        hb = Commodity_Management(self.driver)
        sleep(1)
        mur=hb.text_good_evaluate_name(3)[0]
        print('用户昵称：'+mur)
        hb.Search_input(mur)
        hb.Search_click()
        obj=hb.text_good_evaluate_name(3)[0]
        print('搜索后的用户昵称：'+obj)
        self.assertEqual(mur,obj)

    def test_goods_evaluate_view(self):
        """商品评价，查看"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Evaluate")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.Operation_search(1)
        mur=hb.Search_assert()
        self.assertEqual(mur,'回复评价')

    def test_goods_evaluate_delete(self):
        """商品评价，删除"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Evaluate")
        hb = Commodity_Management(self.driver)
        sleep(1)
        hb.Operation_search(2)
        hb.Search_delete_primary()
        mur=hb.Delete_succeed()
        self.assertEqual(mur,'操作成功')

    def test_goods_rows(self):
        """商品评价，页面显示条数"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("Evaluate")
        hb = Commodity_Management(self.driver)
        hb.Slide_mouse03()
        mur=hb.Rows_n()
        sleep(3)
        obj=hb.text_good_evaluate_name(3)[1]
        self.assertEqual(mur[:2],str(obj))

    def test_goods_class(self):
        """商品分类，查询"""
        ha = login_operate(self.driver)
        ha.open()  ###打开浏览器
        ha.log_in()
        sleep(1.5)
        ha.Get("GoodsClass/0")
        hb = Commodity_Management(self.driver)
        obj=hb.class_name_text(2)
        hb.Class_name_input(obj)
        hb.Goodclass_search()
        sleep(1)
        mur=hb.class_name_text(2)
        self.assertEqual(obj,mur)


