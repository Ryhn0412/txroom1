import time

import allure
from selenium.webdriver import ActionChains, Keys

from base.selecet import select1


class buys_action(select1):
    '''
    # 关于查看订单详情的页面动作元素类
    '''
    # 商品搜索文本框
    text_select = '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div/div/input'
    # 搜索条件选择框
    select_idea = '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[2]/div/div/div/div/div/input'
    # 查询按钮
    button_select = '//div[@class="search-item search-item-btn"]/button[1]/span[1]'
    # 重置按钮
    button_restart = '//div[@class="search-item search-item-btn"]/button[2]/span[1]'
    # 切换店铺的按钮
    button_shangpuname = '//div[@class="search-item el-input el-input--small"]/input'
    # 查看详情的按钮
    button_look = '//div[@class="card-style"]/div[3]/div[3]/table[1]/tbody[1]/tr[1]/td[10]/div/div'
    # 糖心关爱的店铺id
    button_dianpuid = '//div[@class="el-dialog__wrapper"]/div[1]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/label[1]/span[1]'
    # 提交店铺切换确定的按钮
    button_yep = '//div[@class="el-dialog__wrapper"]/div[1]/div[3]/div[1]/div[1]/div[1]/button[2]'
    # 开始时间输入框
    start_text = '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/div/div/input[1]'
    # 结束时间输入框
    end_text = '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/div/div/input[2]'
    # 订单数量显示框
    buys_text = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/span[1]'

    def setup(self):
        # 初始化页面设置，跳转至糖心关爱的店铺的订单页面
        self.shangcheng()
        self.url('https://pre-release.jyhk.com/txga/mall/#/ordermall/orderList')
        self.driver.implicitly_wait(5)
        time.sleep(2)
        # 切换店铺
        self.click(self.button_shangpuname)
        time.sleep(1)
        element1 = self.find(self.button_dianpuid)
        ActionChains(self.driver).move_to_element(element1).click(element1).perform()
        self.click(self.button_yep)

    def quit1(self):
        # 关闭浏览器
        self.quit()
        time.sleep(2)
        print('_______________________该条用例测试结束_______________________')

    def lookbuys(self):
        '''
        查看订单详情的页面动作
        :return:
        '''
        with allure.step('初始化浏览器'):
            self.setup()
        with allure.step('点击查看详情按钮'):
            self.click(self.button_look)
        with allure.step('审查实际情况'):
            time.sleep(3)
            self.catch_png()
        with allure.step('退出浏览器'):
            self.quit1()

    def select(self, idea_select, select_text):
        '''
        搜索订单的页面动作(包含搜索方式的搜索）
        :return:
        '''
        with allure.step('初始化页面'):
            self.setup()
        with allure.step('选择搜索条件为商品名称'):
            a = self.getText(self.buys_text)
            self.click(self.select_idea)
            self.tagclick('span', idea_select)
        with allure.step('输入搜索内容'):
            self.click(self.text_select)
            self.input(self.text_select, select_text)
        with allure.step('点击查询按钮'):
            self.click(self.button_select)
            time.sleep(2)
            b = self.getText(self.buys_text)
        with allure.step('审查查询结果'):
            self.catch_png()
            assert a != b
            time.sleep(2)
        with allure.step('点击重置按钮并查询'):
            self.click(self.button_restart)
            self.click(self.button_select)
        with allure.step('退出浏览器'):
            time.sleep(2)
            self.quit1()

    def time_select(self, start_time, end_time):
        '''
        通过时间进行查找订单的页面动作
        :return:
        '''
        with allure.step('初始化页面'):
            self.setup()
            time.sleep(2)
        with allure.step('输入查找的订单的开始时间'):
            a = self.getText(self.buys_text)
            self.click(self.start_text)
            self.input(self.start_text, start_time)
            self.input(self.start_text, Keys.ENTER)
        with allure.step('输入查找的订单的结束时间'):
            self.click(self.end_text)
            self.input(self.end_text, end_time)
            self.input(self.end_text, Keys.ENTER)
        with allure.step('进行查找'):
            time.sleep(1)
            self.click(self.button_select)
        with allure.step('审查查找结果'):
            time.sleep(1)
            b = self.getText(self.buys_text)
            assert a != b
            self.catch_png()
        with allure.step('退出浏览器'):
            time.sleep(2)
            self.quit1()

    def buys_buff(self, buff_name):
        '''
        点击订单管理界面的各状态切换卡
        :return: 
        '''
        with allure.step('初始化页面'):
            self.setup()
        with allure.step('点击订单状态切换卡'):
            time.sleep(2)
            a = self.getText(self.buys_text)
            self.tagclick('div', buff_name)
        with allure.step('审查实际情况'):
            time.sleep(1)
            b = self.getText(self.buys_text)
            assert a != b
            self.catch_png()
        with allure.step('退出浏览器'):
            time.sleep(1)
            self.quit1()
