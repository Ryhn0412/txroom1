# -*- coding:utf-8 -*-
# @author Ryhn
# @date 2022-02-21
import datetime
import time

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.selecet import select1


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('后台商城系统')
@allure.feature("发放规则模块")
class Test_coupons(select1):

    def setup_method(self):
        '''
        测试用例的初始化
        :return:
        '''
        self.shangcheng()
        self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        '''
        测试用例的结束
        :return:
        '''
        with allure.step('测试结束，关闭浏览器'):
            time.sleep(2)
            print('_______________________该条用例测试结束_______________________')
            self.quit()

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("查询发放规则")
    @allure.title('查询规则的流程测试')
    @pytest.mark.flaky(reruns=1, reruns_dalay=2)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_selectcoupon(self):
        '''
        查询发放规则的测试
        查询条件：测试（名称）糖心关爱（店铺）进行中（状态）当前时间-两百年后（发放时间）
        :return:
        '''
        with allure.step("输入查询的规则名称"):
            list2 = self.driver.find_elements(By.TAG_NAME, 'input')
            for element8 in list2:
                if element8.get_attribute('placeholder') == '请输入规则名称':
                    element8.click()
                    element8.send_keys('这个名称根本不可能查询到')
                    break
        with allure.step("输入查询的店铺名称"):
            list3 = self.driver.find_elements(By.TAG_NAME, 'input')
            for element9 in list3:
                if element9.get_attribute('placeholder') == '请输入店铺名称':
                    element9.click()
                    element9.send_keys('糖心关爱')
                    break
        with allure.step("点击查询按钮"):
            self.tagclick('span', '查询')
        with allure.step("断言查询结果,并截图"):
            allure.attach(self.driver.get_screenshot_as_png(), '查询结果', attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[3]/div/span[1]') == '共 0 条'

        with allure.step("恢复列表"):
            self.tagclick('span', '重置')
            self.tagclick('span', '查询')

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("发放规则的状态测试")
    @allure.title('进行中的发放规则能否编辑或者删除')
    @pytest.mark.flaky(reruns=1, reruns_dalay=2)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_doubleadd(self):
        '''
        进行中的发放规则能否编辑或者删除
        :return:
        '''
        with allure.step('建立一条状态为进行中的发放规则'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/button/span')
            # 规则名称输入
            element1 = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            ActionChains(self.driver).move_to_element(element1).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试删除')
            # 输入规则描述
            element2 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            ActionChains(self.driver).move_to_element(element2).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            time.sleep(2)
            # 选择关联店铺
            element4 = self.find(
                '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            ActionChains(self.driver).move_to_element(element4).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input', '糖心')
            element3 = self.find('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            ActionChains(self.driver).move_to_element(element3).click().perform()
            # 手动输入开始时间
            element5 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ActionChains(self.driver).move_to_element(element5).click().perform()
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            element6 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            ActionChains(self.driver).move_to_element(element6).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            element7 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            ActionChains(self.driver).move_to_element(element7).click().perform()

            # 选择规则类型
            element1 = self.find(
                '//*[@class="el-tabs el-tabs--card el-tabs--top"]/div[2]/div/form/div/div/div/div/input')
            ActionChains(self.driver).move_to_element(element1).click(element1).perform()
            time.sleep(2)
            list1 = self.driver.find_elements(By.TAG_NAME, 'span')
            for element2 in list1:
                if element2.text == '购买商品':
                    ActionChains(self.driver).move_to_element(element2).click().perform()
                    break
            # 选择商品
            time.sleep(1)
            element10 = self.driver.find_element(By.XPATH, '//*[@id="pane-0"]/form/div[2]/div/button/span')
            ActionChains(self.driver).move_to_element(element10).click().perform()
            time.sleep(2)
            self.click('//div[@aria-label="选择商品"]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]')
            # 点击商品的提交按钮
            self.click('//div[@aria-label="选择商品"]/div[3]/div/div/div/button[2]')

            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            self.click('//div[@aria-label="选择优惠券"]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]')
            # 点击优惠券提交按钮
            self.click('//div[@aria-label="选择优惠券"]/div[3]/div/div/div/button[2]')
        with allure.step('提交'):
            time.sleep(1)
            self.click('//div[@class="app-wrapper openSidebar"]/div[2]/section/div[1]/div[4]/button[2]')
        with allure.step('点击编辑按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]/span')
            time.sleep(1)
        with allure.step('审查是否进入编辑界面'):
            time.sleep(1)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/label') == '店铺名称'
        with allure.step('点击删除按钮'):
            time.sleep(2)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
        with allure.step('审查是否删除'):
            time.sleep(1)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/label') == '店铺名称'
            # 测试结束，删除该条规则
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
            time.sleep(2)
            self.tagclick('span', '确定')
            time.sleep(2)
            self.click(
                '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.tagclick('span', '确定')

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("编辑发放规则")
    @allure.title('编辑规则的流程测试')
    @pytest.mark.flaky(reruns=1, reruns_dalay=2)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_changecoupons(self):
        '''
        发放规则进行修改的测试
        :return:
        '''
        with allure.step("点击新增规则按钮"):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/button/span')
        with allure.step("填入基本信息"):
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试1')
            # 输入规则描述
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择关联店铺
            time.sleep(1)
            element4 = self.find(
                '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            ActionChains(self.driver).move_to_element(element4).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input', '糖心')
            element3 = self.find('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            ActionChains(self.driver).move_to_element(element3).click().perform()
            # 手动输入开始时间
            element5 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ActionChains(self.driver).move_to_element(element5).click().perform()
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            element6 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            ActionChains(self.driver).move_to_element(element6).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            element7 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            ActionChains(self.driver).move_to_element(element7).click().perform()
        with allure.step('填写规则组信息'):
            # 选择规则类型
            element1 = self.find(
                '//*[@class="el-tabs el-tabs--card el-tabs--top"]/div[2]/div/form/div/div/div/div/input')
            ActionChains(self.driver).move_to_element(element1).click(element1).perform()
            time.sleep(2)
            list1 = self.driver.find_elements(By.TAG_NAME, 'span')
            for element2 in list1:
                if element2.text == '购买商品':
                    ActionChains(self.driver).move_to_element(element2).click().perform()
                    break
            # 选择商品
            time.sleep(3)
            element3 = self.driver.find_element(By.XPATH, '//*[@id="pane-0"]/form/div[2]/div/button/span')
            self.driver.execute_script("arguments[0].click();", element3)
            time.sleep(2)
            self.click('//div[@aria-label="选择商品"]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]')
            # 点击商品的提交按钮
            self.click('//div[@aria-label="选择商品"]/div[3]/div/div/div/button[2]')
        with allure.step('填写优惠券信息'):
            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            self.click('//div[@aria-label="选择优惠券"]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]')
            # 点击优惠券提交按钮
            self.click('//div[@aria-label="选择优惠券"]/div[3]/div/div/div/button[2]')
        with allure.step('提交'):
            self.click('//div[@class="app-wrapper openSidebar"]/div[2]/section/div[1]/div[4]/button[2]')
            time.sleep(2)
        with allure.step('点击编辑按钮'):
            self.tagclick('span', '结束')
            self.tagclick('span', '确定')
            time.sleep(1)
            self.click('//tbody/tr[1]/td[9]/div[1]/button[1]/span')
        with allure.step('编辑所要修改的内容'):
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            time.sleep(1)
            self.clear('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '修改自动化')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            time.sleep(1)
            self.clear('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '测试内容')
            # 手动输入开始时间
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]',
                       '2122-03-08 00:10:03')
            # 输入结束时间为2200-12-12 00:00:00
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
        with allure.step('点击提交按钮'):
            element110 = self.find('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]')
            ActionChains(self.driver).move_to_element(element110).click().perform()
        with allure.step('审查是否编辑成功'):
            assert \
                self.getText \
                    ('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div') == '修改自动化'
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
            time.sleep(2)
            self.tagclick('span', '确定')
            time.sleep(2)
            self.click(
                '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.tagclick('span', '确定')

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("删除发放规则")
    @allure.title('删除规则的流程测试')
    @pytest.mark.flaky(reruns=1, reruns_dalay=2)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_deletecoupons(self):
        '''
        删除发放规则的测试
        :return:
        '''
        with allure.step("点击新增规则按钮"):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/button/span')
        with allure.step("填入基本信息"):
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试122')
            # 输入规则描述
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择关联店铺
            time.sleep(1)
            element4 = self.find(
                '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            ActionChains(self.driver).move_to_element(element4).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input', '糖心')
            element3 = self.find('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            ActionChains(self.driver).move_to_element(element3).click().perform()
            # 手动输入开始时间
            element5 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ActionChains(self.driver).move_to_element(element5).click().perform()
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            element6 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            ActionChains(self.driver).move_to_element(element6).click().perform()
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            element7 = self.find('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            ActionChains(self.driver).move_to_element(element7).click().perform()
        with allure.step('填写规则组信息'):
            # 选择规则类型
            element1 = self.find(
                '//*[@class="el-tabs el-tabs--card el-tabs--top"]/div[2]/div/form/div/div/div/div/input')
            ActionChains(self.driver).move_to_element(element1).click(element1).perform()
            time.sleep(2)
            list1 = self.driver.find_elements(By.TAG_NAME, 'span')
            for element2 in list1:
                if element2.text == '购买商品':
                    ActionChains(self.driver).move_to_element(element2).click().perform()
                    break
            # 选择商品
            time.sleep(3)
            element3 = self.driver.find_element(By.XPATH, '//*[@id="pane-0"]/form/div[2]/div/button/span')
            self.driver.execute_script("arguments[0].click();", element3)
            time.sleep(2)
            self.click('//div[@aria-label="选择商品"]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]')
            # 点击商品的提交按钮
            self.click('//div[@aria-label="选择商品"]/div[3]/div/div/div/button[2]')
        with allure.step('填写优惠券信息'):
            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            self.click('//div[@aria-label="选择优惠券"]/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]')
            # 点击优惠券提交按钮
            self.click('//div[@aria-label="选择优惠券"]/div[3]/div/div/div/button[2]')
        with allure.step('提交'):
            self.click('//div[@class="app-wrapper openSidebar"]/div[2]/section/div[1]/div[4]/button[2]')
            time.sleep(2)

        with allure.step('点击删除按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
            time.sleep(2)
            self.tagclick('span', '确定')
            time.sleep(2)
            self.click(
                '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.tagclick('span', '确定')
        with allure.step('审查删除的结果并截图'):
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), '删除结果', attachment_type=allure.attachment_type.PNG)
            assert self.getText(
                '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div') != '自动化测试122'
