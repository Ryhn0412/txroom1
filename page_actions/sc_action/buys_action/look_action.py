import time

import allure
from selenium.webdriver import ActionChains

from base.selecet import select1


class look_action(select1):
    # 切换店铺的按钮
    button_shangpuname = '//div[@class="search-item el-input el-input--small"]/input'
    # 查看详情的按钮
    button_look = '//div[@class="card-style"]/div[3]/div[3]/table[1]/tbody[1]/tr[1]/td[10]/div/div'
    # 糖心关爱的店铺id
    button_dianpuid = '//div[@class="el-dialog__wrapper"]/div[1]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/label[1]/span[1]'
    # 提交店铺切换确定的按钮
    button_yep = '//div[@class="el-dialog__wrapper"]/div[1]/div[3]/div[1]/div[1]/div[1]/button[2]'
    # 商家备注文本框
    buys_text = '//*[@id="app"]/div/div[2]/section/div/div[4]/div[2]/div[1]/div[3]/div[4]/div[1]/textarea'

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

    def lookbuys(self, text1):
        '''
        查看订单详情的页面动作
        :return:
        '''
        with allure.step('初始化浏览器'):
            self.setup()
        with allure.step('点击查看详情按钮'):
            self.click(self.button_look)
        with allure.step('点击备注框'):
            self.click(self.buys_text)
            self.input(self.buys_text, text1)
        with allure.step('审查实际情况'):
            time.sleep(3)
            self.catch_png()
        with allure.step('退出浏览器'):
            self.quit1()
