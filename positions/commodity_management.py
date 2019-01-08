import random
import re
import string
from time import sleep

from Elements.element import Commodity_management
from positions.base import Page

class Commodity_Management(Commodity_management,Page):
    """
    商品管理元素操作
    """
    Commdityna=''
    def click_commodity_management(self):
        self.wait_element_located(self.driver, self.commodity_management)
        self.find_element(*self.commodity_management).click()###点击商品管理
        print('点击商品管理')

    def click_add_commodity(self):
        self.wait_element_located(self.driver, self.add_commodity)
        self.find_element(*self.add_commodity).click()###点击添加商品
        print('点击添加商品')

    def text_next_1(self):
        self.wait_element_located(self.driver, self.next_1)
        obj=self.find_element(*self.next_1).text###读取商品分类下一步文案
        return obj

    def click_next_1(self):
        self.find_element(*self.next_1).click()

    def text_select_sort(self):
        """
        读取选择分类
        :return: 选择分类
        """
        # self.wait_element_located(self.driver, self.select_sort)
        obj = self.find_element(*self.select_sort).text
        print(obj)
        return obj

    def click_one_class(self):
        """
        选择一级分类
        a:一级分类个数
        aa:选择的一级分类文案
        :return: 选择的一级分类文案
        """
        try:
            a=self.find_elements(*self.len_commodity_oneclass)##读取一级分类个数
            if len(a)>1:
                n=random.randint(1,len(a))
                obj = self.find_element(*self.select_oneclass(n))
                aa = obj.get_attribute("title")
                print('一级分类为：'+aa)
                self.find_element(*self.select_oneclass(n)).click()
                return str(aa)
            elif len(a)==1:
                obj = self.find_element(*self.select_oneclass(1))
                aa = obj.get_attribute("title")
                print('一级分类为：' + aa)
                self.find_element(*self.select_oneclass(1)).click()
                return str(aa)
            elif len(a)==0:
                print("无一级分类")
        except :
            print("无一级分类")

    def click_too_class(self):
        """
        选择二级分类
        a:二级分类个数
        aa:选择的二级分类文案
        :return: 选择的二级分类文案
        """
        try:
            a=self.find_elements(*self.len_commodity_tooclass)##读取二级分类个数
            if len(a) > 1:
                n=random.randint(1,len(a))
                obj = self.find_element(*self.select_tooclass(n))
                aa = obj.get_attribute("title")
                print('二级分类为：' + aa)
                self.find_element(*self.select_tooclass(n)).click()##点击二级分类
                return str(aa)
            elif len(a)==0:
                print("无二级分类")
            else:
                obj = self.find_element(*self.select_tooclass(1))
                aa = obj.get_attribute("title")
                print('二级分类为：' + aa)
                self.find_element(*self.select_tooclass(1)).click()
                return str(aa)
        except:
            print("无二级分类")

    def click_three_class(self):
        '''
        选择三级分类
        a:三级分类个数
        aa:选择的三级分类文案
        :return: 选择的三级分类文案
        '''
        try:
            a=self.find_elements(*self.len_commodity_threeclass)##读取三级分类个数
            if len(a) > 1:
                n=random.randint(1,len(a))
                obj=self.find_element(*self.select_threeclass(n))
                aa=obj.get_attribute("title")
                print('三级分类为：' + aa)
                self.find_element(*self.select_threeclass(n)).click()##点击三级分类
                return str(aa)
            elif len(a)==0:
                print("无三级分类")
            else:
                obj = self.find_element(*self.select_threeclass(1))
                aa = obj.get_attribute("title")###读取title属性的值
                print('三级分类为：' + aa)
                self.find_element(*self.select_threeclass(1)).click()
                return str(aa)
        except:
            print("无三级分类")

    def Input_Class(self):
        obj = self.find_element(*self.input_class).text
        return obj

    def Information(self):
        obj=self.find_element(*self.information).text
        return obj

    def Commdity_name(self):
        """
        输入商品名称
        :return:
        """
        Commdityname='test_'+str(random.randint(1000,2000))
        self.Commdityna=Commdityname
        self.find_element(*self.commdity_name).send_keys(Commdityname)
        print('商品名称：'+Commdityname)
        return Commdityname

    def Subhead(self):
        """
        输入商品副标题
        :return:
        """
        n='test_'+str(random.randint(2000,3000))
        self.find_element(*self.subhead).send_keys(n)
        print('副标题：'+n)

    def Shops(self):
        self.find_element(*self.shops).click()
    def Shops_title(self):
        """
        读取商家文案
        :return:
        """
        n=self.find_element(*self.shops_title).text
        return n

    def Shops_Select(self):
        """
        选择商家名称
        :return:
        """
        # a = self.find_elements(*self.shops_selects)
        # if len(a) > 1:
        #     n = random.randint(1, len(a))
        #     self.find_element(*self.Shops_select(n)).click()  ##点击商品名称
        #     print('第%d个商家名称'%(n+1)+':'+self.Shops_title())
        # else:
        #     self.find_element(*self.shops_selects).click()
        #     print('选择第一个商家名称')

        self.find_element(*self.shops_title).send_keys("sxl")

    def Shops_presentation(self):
        """
        输入商品介绍
        :return:
        """
        self.find_element(*self.shops_presentation).send_keys('testetsetetsetstt')
        print("商品介绍为:testetsetetsetstt")

    def Freight(self):
        """
        输入运费
        :return:
        """
        n=str(random.randint(10,50))
        self.find_element(*self.freight).send_keys(n)
        print("运费为："+n)

    def Cost_price(self):
        """
        输入商品成本价
        :return:
        """
        n=str(random.randint(50, 100))
        self.find_element(*self.cost_price).send_keys(n)
        print('商品成本价为：'+n)

    def Selling_price(self):
        """
        输入商品售价
        :return:
        """
        n=str(random.randint(100, 1000))
        self.find_element(*self.selling_price).send_keys(n)
        print('商品售价为：'+n)

    def Market_price(self):
        """
        输入市场价
        :return:
        """
        n=str(random.randint(100, 1000))
        self.find_element(*self.market_price).send_keys(n)
        print('市场价为：'+n)

    def SaleNumBase(self):
        '''
        输入初始销量
        :return:
        '''
        n=str(random.randint(10, 100))
        self.find_element(*self.saleNumBase).send_keys(n)
        print('初始销量为：'+n)

    def BaseTransWeight(self):
        """
        输入首重
        :return:
        """
        n=str(random.randint(100, 1000))
        self.find_element(*self.baseTransWeight).send_keys(n)
        print('首重为：'+n)

    def AddTransWeight(self):
        """
        输入续重重量
        :return:
        """
        n=str(random.randint(100, 300))
        self.find_element(*self.addTransWeight).send_keys(n)
        print('续重重量'+n)

    def AddTransPrice(self):
        """
        输入续重重量单价
        :return:
        """
        n=str(random.randint(1,10))
        self.find_element(*self.addTransPrice).send_keys(n)
        print('续重重量单价：'+n)

    def Next_2(self):
        self.find_element(*self.next_2).click()

    def Shops_attribute(self):
        self.find_element(*self.shops_attribute).click()

    def Shops_attribute_title(self):
        n=self.find_element(*self.shops_attribute_title)
        obj=n.get_attribute('title')
        print(obj)
        return obj

    def Select_Shops_attribute(self):
        """
        选择商品属性类型
        :return:
        """
        a = self.find_elements(*self.select_shops_attributes)
        if len(a) > 1:
            n = random.randint(1, len(a))
            self.find_element(*self.Select_shops_attribute(n)).click()  ##点击商品名称
            sleep(2)
            print('选择商品属性%d个'%(n+1)+':'+self.Shops_attribute_title())
        else:
            self.find_element(*self.select_shops_attributes).click()
            print('选择第一个商品属性')

    def Specification_Goods(self):
        """
        选择商品属性规格
        :return:
        """
        # a = self.find_elements(*self.specification)
        # if len(a)>1:
        #     n=random.randint(1,len(a))
        #     b= self.find_elements(*self.Specification_random(n))
        #     m=random.randint(1,len(b))
        #     self.find_element(*self.Specification_goods(n,m)).click()
        #     print('选择属性规格第%d排，第%d个'%(n,m))
        # elif len(a)==1:
        #     b = self.find_elements(*self.Specification_random(1))
        #     m = random.randint(1, len(b))
        #     self.find_element(*self.Specification_goods(1, m)).click()
        #     print('选择属性规格第1排，第%d个' % (m))
        # else:
        #     print('无商品分类')

        a = self.find_elements(*self.specification)
        if len(a) > 1:
            n = random.randint(1, len(a))
            for i in random.sample(range(1,len(a)+1),n):
                b = self.find_elements(*self.Specification_random(i))
                m = random.randint(1, len(b))
                if m>2:
                    m=2
                    for j in random.sample(range(1, len(b)+1),m):
                        self.find_element(*self.Specification_goods(i, j)).click()
                        print('选择属性规格第%d排，第%d个' % (i, j))
                else:
                    for j in random.sample(range(1, len(b)+1),m):
                        self.find_element(*self.Specification_goods(i, j)).click()
                        print('选择属性规格第%d排，第%d个' % (i, j))
        elif len(a) == 1:
            b = self.find_elements(*self.Specification_random(1))
            m = random.randint(1, len(b))
            self.find_element(*self.Specification_goods(1, m)).click()
            print('选择属性规格第1排，第%d个' % (m))
        else:
            print('无商品分类')

    def KG_input(self):
        '''
        输入商品重量
        :return:
        '''
        a = self.find_elements(*self.KGS)
        if len(a)>1:
            for i in range(1,len(a)+1):
                n=str(random.randint(1,10))
                self.find_element(*self.KGs(i)).send_keys(n)
                print('商品sku_%d重量为%s：'%(i,n))
        else:
            n = str(random.randint(1, 10))
            self.find_element(*self.KG).send_keys(n)
            print('商品sku_1重量为%s：' % (n))

    def Early_warn(self):
        """
        输入商品预警值
        :return:
        """
        a = self.find_elements(*self.KGS)
        if len(a) > 1:
            for i in range(1, len(a)+1):
                n=str(random.randint(1,10))
                self.find_element(*self.Early_Warn(i)).send_keys(n)
                print('SKU_%d库存预警值：%s'%(i,n))
        else:
            n = str(random.randint(1, 10))
            self.find_element(*self.early_warns).send_keys(n)
            print('库存预警值：' + n)

    def Upload_pictures(self):
        """
        点击上传图片
        :return:
        """
        a=self.find_elements(*self.upload_picture)
        if len(a)>1:
            for i in range(1,len(a)+1):
                sleep(1)
                self.find_element(*self.Upload_Pictures(i)).click()
                sleep(1)
                self.Select_pictures()
        else:
            self.find_element(*self.upload_picturess).click()

    def Select_pictures(self):
        """
        上传图片
        :return:
        """
        # self.wait_element_located(self.driver,self.select_pictures)
        self.find_element(*self.select_pictures).send_keys('D:\\11.png')
        print('上传成功')

    def Default(self):
        '''
        勾选默认
        :return:
        '''
        self.find_element(*self.default).click()
        print('勾选成功')

    def Commdity_album(self):
        '''
        上传商品相册
        :return:
        '''
        self.find_element(*self.commdity_album).send_keys('D:\\11.png')
        print('上传成功')

    def Next_3(self):
        self.find_element(*self.next_3).click()

    def Relevance_Commdity(self):
        '''
        选择关联商品
        :return:
        '''
        a=self.find_elements(*self.relevance_commditys)
        n = random.randint(1, len(a))
        self.find_element(*self.Relevance_commdity(n)).click()
        print('选择关联商品第%d个'%(n+1))

    def Anticon_right(self):
        '''
        点击关联
        :return:
        '''
        self.find_element(*self.anticon_right).click()
        print('关联成功')

    def Submit(self):
        '''
        点击提交按钮
        :return:
        '''
        self.find_element(*self.submit).click()
        print('提交成功')

    def assert_addcommdity(self):
        '''
        商品列表页，点击查询
        :return:
        '''
        self.Get('https://mantest.godteam.net/#/IndexPage/GoodsList')
        self.find_element(*self.search).send_keys(self.Commdityna)
        self.find_element(*self.look_up).click()
        print('查询成功')


    def assert_addcommdity1(self):
        '''
        商品列表页，点击查询
        :return:
        '''
        self.find_element(*self.look_up).click()
        print('点击查询')


    def Commdity_name_list(self):
        '''
        读取商品列表页的商品名称
        :return:
        '''
        obj=self.find_element(*self.commdity_name_list).text
        print('商品名称为：'+obj)
        return obj

    def click_all_shops(self,n):
        """
        点击商品列表页的导航栏
        :return:
        """
        self.Slide_mouse02()
        self.wait_element_located(self.driver,self.Navigation_bar(n))
        sleep(3)
        self.find_element(*self.Navigation_bar(n)).click()

    def text_all_shops(self,a):
        """
        读取商品列表页导航栏按钮显示的数量
        :return:
        """
        n=self.find_element(*self.Navigation_bar(a)).text
        nn=(re.findall(r"(\d+\.?\d*)",n))
        # nn=n[-5:-1]
        print('按钮数量为'+nn[0])
        return nn[0]

    def text_shops_num(self):
        """
        读取商品列表页分页处显示的商品数量
        :return:
        """
        n=self.find_element(*self.all_shops_num).text.split(" ")
        nn = (re.findall(r"(\d+\.?\d*)", n[1]))
        print("分页处显示的数量为"+nn[0])
        return nn[0]

    def shops_list_search(self,a):
        """
        以商品编号查询商品
        :return:
        """
        n = random.randint(1, 10)
        m=self.find_element(*self.Shop_num(n,a)).text
        sleep(1)
        self.find_element(*self.search).send_keys(m)
        return m

    def Search(self,m):
        """
        输入查询数据  m
        :param m:
        :return:
        """
        sleep(1)
        self.find_element(*self.search).clear()
        self.find_element(*self.search).send_keys(m)
        print('查询数据：'+m)


    # def Search01(self):
    #     self.find_element(*self.search).send_keys('50001172294131')

    def SHop_num1(self,n):
        """读取查询的商品编号"""
        n=self.find_element(*self.Shop_num1(1,n)).text
        return n


    def Shop_class_input(self):
        """
        点击商品分类
        :return:
        """
        self.find_element(*self.shop_class_input).click()

    def Shop_classs(self):
        """
        计算有多少个商品分类数量
        :return: 返回商品分类总数
        """
        n=self.find_elements(*self.shop_classs)
        return len(n)

    def SHOP_Classs(self):
        """
        点击商品分类
        :return:
        """
        n=random.randint(1,self.Shop_classs())
        a=self.find_element(*self.SHOP_class(n)).text
        self.find_element(*self.SHOP_class(n)).click()
        print('选择的商品分类为：'+a)
        return a

    def Shop_Type(self,m):
        """
        读取商品类型
        m=5:读取粮票规则
        :return:
        """
        if self.Shop_amount()>0:
            if m!=5:
                a=random.randint(1,self.Shop_amount())
                n=self.find_element(*self.Shop_type(a,m)).text
            else:
                n=self.find_element(*self.Shop_type(1,m)).text
        else:
            n=0
        return n

    def Shop_amount(self):
        """
        统计当前页商品数量
        :return:
        """
        n=self.find_elements(*self.shop_amount)
        return len(n)

    def Shop_name_input(self):
        """
        点击商品名称
        :return:
        """
        self.find_element(*self.shop_name_input).click()

    def Shop_names(self):
        """
        读取商家数量
        :return: 返回商家数量
        """
        n=self.find_elements(*self.shop_names)
        return len(n)

    def Shop_Name(self):
        """
        点击商家名称
        :return:
        """
        n=random.randint(1,self.Shop_names())
        self.wait_element_located(self.driver,self.Shop_name(n))
        a=self.find_element(*self.Shop_name(n)).text
        self.find_element(*self.Shop_name(n)).click()
        print('选择的商家名称为:'+a)
        return a

    def Revise_food_stamps(self):
        """
        点击修改粮票规则
        :return:
        """
        self.find_element(*self.revise_food_stamps).click()

    def Food_stamps(self):
        """
        点击粮票规则下拉框
        :return:
        """
        self.find_element(*self.food_stamps_select).click()

    def Foog_stampss(self):
        """
        读取粮票规则总数
        :return: 返回粮票规则总数量
        """
        n=self.find_elements(*self.foog_stampss)
        return len(n)

    def Foog_Stamps(self):
        """
        选择粮票规则
        :return:
        """
        n=random.randint(1,self.Foog_stampss())
        a=self.find_element(*self.Foog_stamps(n)).text
        self.find_element(*self.Foog_stamps(n)).click()
        print('选择的修改粮票规则为：'+a)
        return a

    def Revise_Food_stamps_confirm(self):
        """
        点击修改粮票确定按钮
        :return:
        """
        self.find_element(*self.Revise_food_stamps_confirm(2)).click()

    def Shop_list_checkbox(self):
        """
        选择修改粮票规则的商品
        :return:
        """
        self.find_element(*self.shop_list_checkbox).click()

    def PUtaway(self,):
        """
        点击上架按钮
        :return:
        """
        n=random.randint(1,self.Shop_amount())
        m = self.find_element(*self.Shop_num(n,3)).text
        print('上架的商品编码：'+m)
        self.Slide_mouse01(self.Shop_num(n,3))
        sleep(1)
        self.find_element(*self.Putaway(n)).click()
        return m

    def text_class_value(self):
        """
        读取上架按钮的class值
        :return:
        """
        class_value=self.find_element(*self.Putaway(1)).get_attribute('class')
        print('class:'+class_value)
        return class_value



    def Audition_text(self):
        """
        读取审核状态
        :return:
        """
        a=self.find_element(*self.Audition(1)).text
        return a

    def Audit_button(self):
        """
        点击待审核按钮
        :return:
        """
        n = random.randint(1, self.Shop_amount())
        m = self.find_element(*self.Shop_num(n,3)).text
        self.find_element(*self.Audition(n)).click()
        print(m)
        return m

    def Audit_pass(self):
        """点击审核通过按钮"""
        self.wait_element_located(self.driver,self.audit_pass)
        self.find_element(*self.audit_pass).click()
        sleep(1)

    def Audit_ion(self,n):
        """点击审核结果按钮"""
        self.find_element(*self.audit_ion(n)).click()

    def Delete_shop(self):
        """
        点击删除按钮
        :return:
        """
        n = random.randint(1, self.Shop_amount())
        m = self.find_element(*self.Shop_num(n,3)).text
        print('删除的商品编码：' + m)
        self.Slide_mouse01(self.Shop_num(n,3))
        sleep(1)
        self.find_element(*self.delete_shop(n)).click()
        return m

    def text_error_massage(self):
        """
        读取页面提示的消息
        :return:
        """
        self.wait_element_located(self.driver, self.error_massage)
        sleep(1)
        n=self.find_element(*self.error_massage).text
        return n

    def Delete_affirm(self,n):
        """
        点击删除操作，确认或取消
        :return:
        """
        self.wait_element_located(self.driver, self.delete_affirm(n))
        self.find_element(*self.delete_affirm(n)).click()

    def Page_nu(self):
        """
        点击分页下拉表
        :return:
        """
        self.find_element(*self.page_nu).click()

    def Page(self):
        """
        选择下拉框数据
        :return:
        """
        ns=self.find_elements(*self.page_nus)
        n=random.randint(1,len(ns))
        nn=self.find_element(*self.page_n(n)).text
        self.find_element(*self.page_n(n)).click()
        print(nn)
        return int(nn[:2])


    def delete_shop_Classs(self):
        """
        点击商品分类
        :return:
        """
        b=''
        n=random.randint(1,self.Shop_classs())
        a=self.find_element(*self.SHOP_class(n)).text
        self.find_element(*self.SHOP_class(n)).click()
        ns=self.find_elements(*self.too_class)
        if len(ns)>0:
            if len(ns)==1:
                b=self.find_element(*self.Too_class_n(1)).text
                self.find_element(*self.Too_class_n(1)).click()
            else:
                q=random.randint(1,len(ns))
                b = self.find_element(*self.Too_class_n(q)).text
                self.find_element(*self.Too_class_n(q)).click()
        else:
            print('无二级分类')
        print('选择的商品分类为：'+a+'/'+b)
        return a+b

    def click_restore(self):
        """
        点击还原按钮
        :return:
        """
        ns=self.Shop_amount()
        n=random.randint(1,ns)
        m=self.find_element(*self.Shop_num1(n,2)).text
        self.find_element(*self.Shop_num1(n,8)).click()
        print('还原商品编码：'+m)
        return m

    def text_value(self,n,m):
        """
        商品列表页，读取页面数据

        :return: 返回读取的数据
        """
        m = self.find_element(*self.Shop_num1(n, m)).text
        # self.find_element(*self.Shop_num1(n, m)).click()
        return m

    def text_good_evaluate_name(self,m):
        """
        读取页面展示的商品名称
        m:1-9
        :return:
        """
        a=self.find_elements(*self.evaluates)
        n=random.randint(1,len(a))
        mur=self.find_element(*self.evaluate_n(n,m)).text
        return mur,len(a)

    def Search_input(self,m):
        """
        输入搜索数据
        :return:
        """
        self.find_element(*self.search_input).send_keys(m)

    def Search_click(self):
        """
        点击查询按钮
        :return:
        """
        self.find_element(*self.search_click).click()

    def Operation_search(self,i):
        """
        点击操作
        i: 1 查看
           2 删除
        :return:
        """
        a = self.find_elements(*self.evaluates)
        n = random.randint(1, len(a))
        mur = self.find_element(*self.evaluate_n(n, 4)).text
        print('商品名称：'+mur)
        self.find_element(*self.Operation(n,i)).click()
        return mur

    def Search_assert(self):
        """
        读取文案
        :return:
        """
        mur=self.find_element(*self.search_assert).text
        return mur

    def Search_delete_primary(self):
        """
        点击确认
        :return:
        """
        self.find_element(*self.search_delete_primary).click()

    def Search_delete_cancel(self):
        """
        点击取消
        :return:
        """
        self.find_element(*self.search_delete_cancel).click()

    def Delete_succeed(self):
        """
        读取操作成功文案
        :return:
        """
        obj=self.find_element(*self.delete_succeed).text
        return obj

    def Rows_n(self):
        """
        点击显示条数
        :return:
        """
        self.wait_element_located(self.driver, self.rows_button)
        self.find_element(*self.rows_button).click()
        a=self.find_elements(*self.row)
        n=random.randint(1,len(a))
        obj=self.find_element(*self.Rows(n)).text
        self.find_element(*self.Rows(n)).click()
        return obj

    def Rows_button(self):
        """
        点击显示条数按钮
        :return:
        """
        self.wait_element_located(self.driver,self.rows_button)
        self.find_element(*self.rows_button).click()

    def class_name_text(self,m):
        """
        读取页面第 n 条数据的m个数据
        :return:
        """
        # n=''.join(random.choice(string.digits + string.ascii_letters) for i in range(6))
        nn=self.find_elements(*self.all_goodclass)
        n=random.randint(1,len(nn))
        obj=self.find_element(*self.Goodclass_n(n,m)).text
        return obj

    def Class_name_input(self,m):
        """
        商品分类，搜索框
        :return:
        """
        self.find_element(*self.class_name_input).send_keys(m)

    def Goodclass_search(self):
        """
        点击查询
        :return:
        """
        self.find_element(*self.goodclass_search).click()