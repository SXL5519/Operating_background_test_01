import random

from selenium.webdriver.common.by import By
####  我的页面元素定位
class Log_in():
    """
    登录页
    """
    neme=(By.ID,'username')###定位用户名
    passWord=(By.ID,'passWord')###定位密码
    login_submit=(By.CLASS_NAME,'loginFormButton___2SPvP')###定位登录按钮


class home_Page():
    """
    首页
    """
    home_page=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[1]/div/span[1]/span[1]')###定位首页“首页”文案


class Commodity_management():
    """
    商品管理页
    """
    commodity_management=(By.CLASS_NAME,"anticon-tags")###定位商品管理
    # add_commodity=(By.CLASS_NAME,"ant-menu-item-selected")##定位添加商品
    add_commodity=(By.XPATH,'//*[@id="2$Menu"]/li[2]/a')
    next_1=(By.CLASS_NAME,'ant-btn-primary')##商品分类页，下一步
    # select_sort=(By.CLASS_NAME,'anticon-tagt')##选择分类文案定位
    select_sort=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section/div[1]/div/span')###选择商品分类页“选择分类”文案定位
    def select_oneclass(self,n):
        if n>1:
            commodity_class=(By.XPATH,'/html/body/div[3]/div/div/div/ul/li[%d]'%n)##一级分类定位
        else:
            commodity_class = (By.XPATH, '/html/body/div[3]/div/div/div/ul/li')  ##一级分类定位
        return commodity_class

    len_commodity_oneclass=(By.XPATH,'/html/body/div[3]/div/div/div/ul/li')##一级分类集数量

    def select_tooclass(self,n):
        if n>1:
            commodity_class=(By.XPATH,'/html/body/div[3]/div/div/div/ul[2]/li[%d]'%n)##二级分类定位
        else:
            commodity_class = (By.XPATH, '/html/body/div[3]/div/div/div/ul[2]/li')
        return commodity_class

    len_commodity_tooclass=(By.XPATH,'/html/body/div[3]/div/div/div/ul[2]/li')##二级分类集数量

    def select_threeclass(self,n):
        if n>1:
            commodity_class=(By.XPATH,'/html/body/div[3]/div/div/div/ul[3]/li[%d]'%n)##三级分类定位
        else:
            commodity_class = (By.XPATH, '/html/body/div[3]/div/div/div/ul[3]/li')
        return commodity_class

    len_commodity_threeclass=(By.XPATH,'/html/body/div[3]/div/div/div/ul[3]/li')##三级分类集数量

    input_class=(By.CLASS_NAME,'ant-cascader-picker-label')###选择的分类定位

    information=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/form/section[1]/div[1]/div/span')###定位基本信息
    commdity_name=(By.ID,'goodsName')###商品名称
    subhead=(By.ID,'subtitle')###副标题
    shops=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/form/section[1]/div[2]/div[4]/div[2]/div/span/div/div/div')###商家名称输入框

    shops_title = (By.ID,"merchant")##商家名称输入框，title文案定位
    # shops_title=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/form/section[1]/div[2]/div[4]/div[2]/div/span/div/div/div/div[2]')##商家名称输入框，title文案定位
    def Shops_select(self,n):
        shops_select=(By.XPATH,'/html/body/div[3]/div/div/div/ul/li[%d]'%n)###定位下拉商家
        return shops_select

    shops_selects=(By.XPATH,'/html/body/div[3]/div/div/div/ul/li')
    shops_presentation=(By.ID,'goodsDesc')##商品介绍

    freight =(By.ID,'transPrice')###运费

    cost_price=(By.ID,'costPrice')###成本价
    selling_price=(By.ID,'salePrice')###售价
    market_price=(By.ID,'markPrice')##市场价
    saleNumBase=(By.ID,'saleNumBase')###初始销量
    baseTransWeight=(By.ID,'baseTransWeight')##首重
    addTransWeight=(By.ID,'addTransWeight')###续重
    addTransPrice=(By.ID,'addTransPrice')###续重重量单价
    next_2=(By.CLASS_NAME,'ant-btn-primary')###填写订单页，下一步
    shops_attribute=(By.CLASS_NAME,'ant-select-selection__rendered')###商品属性输入框
    def Select_shops_attribute(self,n):
        select_shops_attribute=(By.XPATH,'/html/body/div[3]/div/div/div/ul/li[%d]'%n)###商品属性
        return select_shops_attribute

    shops_attribute_title=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[1]/div/div/div/div/div[2]')##商品属性输入框,，title

    select_shops_attributes=(By.XPATH,'/html/body/div[3]/div/div/div/ul/li')###商品属性总数
    def Specification_goods(self,n,m):
        specification_goods=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/section/div[%d]/div[2]/div/label[%d]/span[1]'%(n,m))
        return specification_goods  ###定位商品规格的多选框

    specification=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/section/div')###定位商品规格分类数量
    def Specification_random(self,n):
        specification_random=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/section/div[%d]/div[2]/div/label'%n)###定位某一个分类下的规格数量
        return specification_random
    KGS=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr')###SKU数量
    def KGs(self,n):
        kg=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[%d]/td[5]/div/div[2]/input'%n)###商品重量
        return kg
    KG = (By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[5]/div/div[2]/input')  ###商品重量
    def Early_Warn(self,n):
        early_warn=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[%d]/td[6]/div/div[2]/input'%n)###库存预警
        return early_warn

    early_warns = (By.XPATH,
                  '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div[2]/input')
    def Upload_Pictures(self,n):
        upload_pictures=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[%d]/td[10]/a[1]'%n)##上传图片
        return upload_pictures

    upload_picturess = (By.XPATH,
                       '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[10]/a[1]')  ##上传图片

    upload_picture = (By.XPATH,
                       '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr')  ##上传图片集
    select_pictures=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/span/div[2]/span/input')##选择图片
    default=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[1]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[10]/label/span[1]/input')###默认
    commdity_album=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section[3]/div[2]/div/div/div/div/span/div[2]/span/input')###商品相册
    next_3=(By.CLASS_NAME,'ant-btn-primary')##商品属性页，下一步
    relevance_commditys=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section/div[2]/div[2]/div/div[1]/div[2]/ul/div')###关联商品集
    def Relevance_commdity(self,n):
        relevance_commdity=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section/div[2]/div[2]/div/div[1]/div[2]/ul/div[%d]'%n)##关联商品
        return relevance_commdity

    anticon_right=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/section/div[2]/div[2]/div/div[2]/button[2]')###右关联
    submit=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/button[2]')###提交按钮

    search=(By.ID,'queryWord')###商品列表页，搜索框定位
    look_up=(By.CSS_SELECTOR,'.ant-btn.ant-btn-primary')##查询，商品列表页
    commdity_name_list=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[5]/div/div[1]')###商品名称，商品列表页

    def Navigation_bar(self,n):
        """
        :param n:参数为1—7
        :return: 返回为对应的导航栏对应的按钮定位
        """
        navigation_bar =(By.CSS_SELECTOR,'div.ant-btn-group>button:nth-child(%d)'%n)###商品列表页导航栏
        return navigation_bar

    all_shops_num=(By.CSS_SELECTOR,'ul[unselectable="unselectable"]>li')##全部商品数量显示
    def Shop_num(self,n,m):
        shop_num=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(%d)'%(n,m))###商品列表页，商品编码定位
        return shop_num
    def Shop_num1(self,n,m):
        shop_num1 = (By.CSS_SELECTOR, '.ant-table-tbody>tr:nth-child(%d)>td:nth-child(%d)'%(n,m))###商品列表页，定位搜索出来的商品编码
        return shop_num1

    shop_class_input=(By.ID,'menus')###商品列表页的商品分类下拉框
    shop_classs=(By.CSS_SELECTOR,'.ant-cascader-menu>li')###商品分类集，商品列表页
    def SHOP_class(self,n):
        shop_class=(By.CSS_SELECTOR,'.ant-cascader-menu>li:nth-child(%d)'%n)
        return shop_class   ##商品分类定位
    def Shop_type(self,n,m):
        shop_type=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(5)>div>div:nth-child(%d)'%(n,m))
        return shop_type##商品类型定位

    shop_amount=(By.CSS_SELECTOR,'.ant-table-tbody>tr')###当前页商品数量显示
    shop_name_input=(By.CSS_SELECTOR,'.ant-select-selection__placeholder')###商品名称输入框
    shop_names=(By.CSS_SELECTOR,'.ant-select-dropdown-menu>li')###商家名称集
    def Shop_name(self,n):
        shop_name=(By.CSS_SELECTOR,'.ant-select-dropdown-menu>li:nth-child(%d)'%n)###商家名称
        return shop_name

    revise_food_stamps=(By.CSS_SELECTOR,'.actionBar___335p7>div:nth-child(3)>div>span>span>button')###修改粮票规则按钮
    food_stamps_select=(By.CSS_SELECTOR,'.ant-col-14.ant-form-item-control-wrapper')##粮票规则下拉框
    def Foog_stamps(self,n):
        foog_stamps=(By.CSS_SELECTOR,'.ant-select-dropdown-menu-vertical>li:nth-child(%d)'%n)###粮票规则
        return foog_stamps

    foog_stampss=(By.CSS_SELECTOR,'.ant-select-dropdown-menu-vertical>li')##粮票规则总数定位
    def Revise_food_stamps_confirm(self,n):
        revise_food_stamps_confirm=(By.CSS_SELECTOR,'.ant-modal-footer>div>button:nth-child(%d)'%n)###修改粮票确定按钮
        return revise_food_stamps_confirm

    shop_list_checkbox=(By.CSS_SELECTOR,'.ant-table-tbody>tr>td>span')##商品列表页，第一个复选框
    def Putaway(self,n):
        putaway=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(7)>div>div>span'%n)##上架按钮
        return putaway
    def Audition(self,n):
        audition=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(11)>div>span>span>div'%n)###审核状态
        return audition
    audit_pass=(By.CSS_SELECTOR,'.ant-radio-input')###审核通过
    def audit_ion(self,n):
        """
        参数1-2
        :param n: 1：取消；2：确定
        :return:
        """
        audit_ion=(By.CSS_SELECTOR,'.ant-modal-footer>div>button:nth-child(%d)'%n)
        return audit_ion


    def delete_shop(self,n):
        """
        商品列表删除按钮定位
        :param n:当前页面第n个商品数据
        :return:
        """
        delete_n = (By.CSS_SELECTOR, '.ant-table-tbody>tr:nth-child(%d)>td:nth-child(12)>p>a:nth-child(7)' % n)
        return delete_n

    error_massage=(By.CSS_SELECTOR,'.ant-message-error>span')##页面错误消息提示定位
    def delete_affirm(self,n):
        """
        删除确认按钮定位
        :param n: 1:取消；2：确认
        :return:
        """
        delete=(By.CSS_SELECTOR,'.ant-popover-inner-content>div:nth-child(2)>button:nth-child(%d)'%n)
        return delete

    page_nu=(By.CSS_SELECTOR,'.ant-pagination-options-size-changer')###分页下拉框
    page_nus=(By.CSS_SELECTOR,'.ant-select-dropdown-menu-vertical>li')###分页下拉框数据
    def page_n(self,n):
        nn= (By.CSS_SELECTOR, '.ant-select-dropdown-menu-vertical>li:nth-child(%d)'%n)  ###分页下拉框数据
        return nn

    too_class=(By.CSS_SELECTOR,'.ant-cascader-menus-placement-bottomLeft>div>ul:nth-child(2)>li')###二级分类集
    def Too_class_n(self,n):###第N个二级分类
        too_class_n=(By.CSS_SELECTOR,'.ant-cascader-menus-placement-bottomLeft>div>ul:nth-child(2)>li:nth-child(%d)'%n)
        return too_class_n

    evaluates=(By.CSS_SELECTOR,'.ant-table-tbody>tr')###当前页所有的商品评价数据

    def evaluate_n(self,n,m):
        evaluate=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(%d)'%(n,m))###当前页面第 n 条数据的第 m 个展示的数据
        return evaluate

    search_input=(By.ID,'goodsName')##商品评价搜索框定位
    search_click=(By.CSS_SELECTOR,'button[type = "submit"]')###商品评价页面查询按钮

    def Operation(self,n,i):
        operation=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(9)>p>a:nth-child(%d)'%(n,i))
        return operation
    search_assert=(By.CSS_SELECTOR,'.ant-col-24.RightReply___3s8qX>p')###评价详情页面，回复评价文案

    search_delete_primary=(By.CSS_SELECTOR,'.ant-btn.ant-btn-primary.ant-btn-sm')###商品评价，删除确认按钮
    search_delete_cancel=(By.CSS_SELECTOR,'.ant-btn.ant-btn-sm')###商品评价，删除取消按钮
    delete_succeed=(By.CSS_SELECTOR,'.ant-message>span>div>div>div>span')###删除，操作成功

    def Rows(self,n):
        rows=(By.CSS_SELECTOR,'.ant-select-dropdown-menu>li:nth-child(%d)'%n)
        return rows###某一个显示条数
    row=(By.CSS_SELECTOR,'.ant-select-dropdown-menu>li')###所有的条数
    rows_button=(By.CSS_SELECTOR,'.ant-select-selection-selected-value')##条数按钮

    class_name_input=(By.ID,'menuName')###分类名称输入框

    all_goodclass=(By.CSS_SELECTOR,'.ant-table-tbody>tr')###商品分类页所有数据
    def Goodclass_n(self,n,m):
        goodclass_n=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(%d)'%(n,m))###商品分类页的某一条数据
        return goodclass_n

    goodclass_search=(By.CSS_SELECTOR,'.ant-btn-primary')###商品分类，查询按钮
class shops_manage():
    """
    商家管理
    """
    Shops_manage=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div/div/ul/li[4]/div')##商家管理

    shops_check_in=(By.CSS_SELECTOR,'a[href*="#/IndexPage/ShopDetail/0/edit"]')##商家列表

    create_account=(By.ID,'merchant.accounts')##开通商家账号

    shops_id=(By.ID,'merchant.userName')##商家账号
    shops_password=(By.ID,'merchant.passWord')##商家密码
    shops_num=(By.ID,'merchant.merchantId')#艾家编号
    shops_name=(By.ID,'merchant.merchantName')##商家名称
    shop_name=(By.ID,'merchant.storeName')##店铺名称
    key_word=(By.ID,'merchant.keyWord')##搜索关键字
    shops_logo=(By.CSS_SELECTOR,'input[accept*="image/*"]')##店铺LOGO
    shops_photo = (By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div[1]/div[2]/div/div[16]/div[2]/div/span/div/div/span/div[2]/span/input')
    company_name=(By.ID,'company.companyName')##公司名称
    company_certifyNO=(By.ID,'company.certifyNO')#营业执照注册号
    company_certifyName=(By.ID,'company.certifyName')###法定代表人姓名
    company_identityNo=(By.ID,'company.identityNo')##身份证号
    business_license=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div[3]')##营业执照
    bank=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div[4]')##银行许可证
    bank_companyName=(By.ID,'bank.companyName')##银行公司名称
    bank_blankNo=(By.ID,'bank.blankNo')###公司银行账号
    bank_blankName=(By.ID,'bank.blankName')###开户银行名称
    other=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div[5]/div[1]')##其他设置
    shop_grade=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div[5]/div[2]/div/div[2]/div[2]/div/span/div/div/div')##商家等级
    merchant_companyGrade=(By.ID,'merchant.companyGrade')##商家等级输入框
    shop_class=(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[1]/div[5]/div[2]/div/div[3]/div[2]/div/span/div/div/div')##商家类别
    merchant_companyType=(By.ID,'merchant.companyType')##商家类别输入框
    submit=(By.CSS_SELECTOR,'button[type*="submit"]')##提交

    placeholder = (By.ID, 'merchantId')  ##商家列表页，商家账号输入框
    def Text_value(self,n,m):
        text_value=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(%d)'%(n,m))
        return text_value###商家列表页，数据读取

    shop_nu=(By.CSS_SELECTOR,'.ant-table-tbody>tr')##页面展示的商家数量
    query =(By.CSS_SELECTOR,'.ant-btn-primary')##查询按钮定位
    store_name=(By.ID,'storeName')###店铺名称输入框
    store_grade=(By.CSS_SELECTOR,'.ant-select-selection__rendered')##店铺等级
    grade=(By.CSS_SELECTOR,'.ant-select-dropdown-menu-root>li')##所有等级
    def grade_N(self,n):
        grade_n=(By.CSS_SELECTOR,'.ant-select-dropdown-menu-root>li:nth-child(%d)'%n)
        return grade_n####第 n 个等级

    def remain_sum_and_recharge(self,n,m):
        recharge=(By.CSS_SELECTOR,'.ant-table-tbody>tr:nth-child(%d)>td:nth-child(9)>span>span:nth-child(%d)'%(n,m))
        return recharge###可用余额和充值按钮

    recharge_money=(By.ID,'money')###充值金额输入框
    def Recharge_Confirm_or_cancel(self,n):
        recharge_Confirm_or_cancel=(By.CSS_SELECTOR,'.ant-modal-footer>div>button:nth-child(%d)'%n)
        return recharge_Confirm_or_cancel  ###充值 确认或者取消