# -*- coding:utf-8 -*-
# @author Ryhn
# @date 2022-02-25
import datetime
import time

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from txhoutai.selecet import select1

@allure.epic('后台商城系统')
@allure.feature('发放规则模块')
@allure.story("新增发放规则")
class Test_addcoupons(select1):
    def setup_method(self):
        '''
        测试用例的初始化
        :return:
        '''
        self.shangcheng()
        self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
        self.driver.implicitly_wait(10)
        self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/button/span')

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
    @allure.story("新增发放规则")
    @allure.title('新增规则的流程测试')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addcoupon(self):
        """
        新增发放规则的流程测试
        :return:
        """
        with allure.step("点击新增规则按钮"):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/button/span')
        with allure.step("填入基本信息"):
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择关联店铺
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
            # 手动输入开始时间
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
        with allure.step('填写规则组信息'):
            # 选择规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div[1]/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
            # 选择商品
            self.click('//*[@id="pane-0"]/form/div[2]/div/button/span')
            element2 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element2).perform()
            ActionChains(self.driver).click(element2).perform()
            self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
        with allure.step('填写优惠券信息'):
            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            element1 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[6]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element1).perform()
            ActionChains(self.driver).click(element1).perform()
            self.click('/html/body/div[6]/div/div[3]/div/div/div/button[2]/span')
        with allure.step('提交'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')

    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title("针对发放规则名称的测试1")
    @allure.severity(allure.severity_level.NORMAL)
    def test_couposname(self):
        '''
        针对规则名称的测试
        检验是否会重复
        :return:
        '''
        # 第一次新增（直接忽略，重点看第二次新增后的断言）
        with allure.step("第一次新增规则"):

            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择关联店铺
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
            # 手动输入开始时间
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            # 选择规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div[1]/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
            # 选择商品
            self.click('//*[@id="pane-0"]/form/div[2]/div/button/span')
            element2 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element2).perform()
            ActionChains(self.driver).click(element2).perform()
            self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            element1 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[6]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element1).perform()
            ActionChains(self.driver).click(element1).perform()
            self.click('/html/body/div[6]/div/div[3]/div/div/div/button[2]/span')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        # 第二次新增，主要看是否会出现提交失败，规则名称重复
        with allure.step("第二次新增规则"):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            # 点击复制按钮
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
        with allure.step('提交'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交失败'):
            allure.attach(self.driver.get_screenshot_as_png(), '审查结果', allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'
        with allure.step('删除本次测试所新建的发放规则'):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.click('/html/body/div[2]/div/div[3]/button[2]/span')


    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('针对发放规则名称的测试2')
    def test_couponname2(self):
        '''
        针对不填写发放规则的测试
        检验能否提交成功
        :return:
        '''
        with allure.step("填写规则内容"):
            # 规则名称不输入

            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择关联店铺
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
            # 手动输入开始时间
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            # 选择规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div[1]/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
            # 选择商品
            self.click('//*[@id="pane-0"]/form/div[2]/div/button/span')
            element2 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element2).perform()
            ActionChains(self.driver).click(element2).perform()
            self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            element1 = self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element1).perform()
            ActionChains(self.driver).click(element1).perform()
            self.click('/html/body/div[6]/div/div[3]/div/div/div/button[2]/span')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交失败'):
            allure.attach(self.driver.get_screenshot_as_png(), '审查结果', allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'



    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('针对发放规则内容的测试')
    def test_coupontext(self):
        '''
        针对规则内容的测试
        检验能否提交成功
        :return:
        '''
        with allure.step('填写必要内容'):
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试')
            # 不输入规则描述

            # 选择关联店铺
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
            # 手动输入开始时间
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
        with allure.step('填写规则组信息'):
            # 选择规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div[1]/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
            # 选择商品
            self.click('//*[@id="pane-0"]/form/div[2]/div/button/span')
            element2 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element2).perform()
            ActionChains(self.driver).click(element2).perform()
            self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
        with allure.step('填写优惠券信息'):
            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            element1 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[6]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element1).perform()
            ActionChains(self.driver).click(element1).perform()
            self.click('/html/body/div[6]/div/div[3]/div/div/div/button[2]/span')
        with allure.step('提交'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交失败'):
            allure.attach(self.driver.get_screenshot_as_png(), '审查结果', allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'



    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('针对发放规则店铺的测试')
    def test_couponroom(self):
        '''
        针对不选择发放规则店铺的测试
        检验能否提交成功
        :return:
        '''
        with allure.step('填写必要内容'):
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 不选择关联店铺

            # 手动输入开始时间
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
            ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
            # 输入结束时间为2200-12-12 00:00:00
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                       , '2200-12-12 00:00:00')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
        try:
          with allure.step('填写规则组信息'):
            # 选择规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div[1]/input')
            self.click('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
            # 选择商品
            self.click('//*[@id="pane-0"]/form/div[2]/div/button/span')
            element2 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element2).perform()
            ActionChains(self.driver).click(element2).perform()
            self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
          with allure.step('填写优惠券信息'):
            # 选择优惠券
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
            element1 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[6]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element1).perform()
            ActionChains(self.driver).click(element1).perform()
            self.click('/html/body/div[6]/div/div[3]/div/div/div/button[2]/span')
        except Exception as e:
          with allure.step('提交'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交失败'):
            allure.attach(self.driver.get_screenshot_as_png(), '审查结果', allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'

    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('针对发放规则时间的测试')
    def test_coupontime(self):
        # 规则名称输入
        self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
        self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试')
        # 输入规则描述
        self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
        self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
        # 选择关联店铺
        self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
        self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
        # 手动输入开始时间
        self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]')
        ry2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[1]', ry2)
        # 输入结束时间为2200-12-12 00:00:00
        self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]')
        self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/input[2]'
                   , '2200-12-12 00:00:00')
        time.sleep(1)
        self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
        # 选择规则类型
        self.click('//*[@id="pane-0"]/form/div[1]/div/div/div[1]/input')
        self.click('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
        # 选择商品
        self.click('//*[@id="pane-0"]/form/div[2]/div/button/span')
        element2 = self.driver.find_element(By.XPATH,
                                            '/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
        ActionChains(self.driver).move_to_element(element2).perform()
        ActionChains(self.driver).click(element2).perform()
        self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
        # 选择优惠券
        self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[2]/form/div/div/button/span')
        element1 = self.driver.find_element(By.XPATH,
                                            '/html/body/div[6]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')
        ActionChains(self.driver).move_to_element(element1).perform()
        ActionChains(self.driver).click(element1).perform()
        self.click('/html/body/div[6]/div/div[3]/div/div/div/button[2]/span')
        time.sleep(1)
        self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        # 第二次新增，主要看是否会出现提交失败，规则名称重复
        with allure.step("填写必要内容"):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            # 点击复制按钮
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择关联店铺
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
            # 不填写时间
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[4]/div/div/i[2]')
            time.sleep(3)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交失败'):
            allure.attach(self.driver.get_screenshot_as_png(), '审查结果', allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'
            # self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            # self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            # self.click('/html/body/div[2]/div/div[3]/button[2]/span')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('不同规则类型的流程1')
    def test_guize1(self):
        with allure.step('输入必填内容'):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试规则类型')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择计数达标规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            # 填写达标次数
            self.click('//*[@id="pane-0"]/form/div[5]/div/div/input')
            self.clear('//*[@id="pane-0"]/form/div[5]/div/div/input')
            self.input('//*[@id="pane-0"]/form/div[5]/div/div/input',2)
            time.sleep(1)
            # 点击提交按钮
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交成功'):
            allure.attach(self.driver.get_screenshot_as_png(), '审查结果', allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div') =='自动化测试规则类型'
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.click('/html/body/div[2]/div/div[3]/button[2]/span')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('不同规则类型的流程2')
    def test_guize2(self):
        with allure.step('输入必填内容'):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试规则类型2')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            # 选择消费金额达标规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div/input')
            self.driver.find_element\
                (By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(3) > span').click()
            # 填写达标次数
            self.click('//*[@id="pane-0"]/form/div[4]/div/div/input')
            self.clear('//*[@id="pane-0"]/form/div[4]/div/div/input')
            self.input('//*[@id="pane-0"]/form/div[4]/div/div/input',2)
            time.sleep(1)
            # 点击提交按钮
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交成功'):
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), '审查结果', allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div') == '自动化测试规则类型2'
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.click('/html/body/div[2]/div/div[3]/button[2]/span')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('针对任务型计数类型的测试')
    @pytest.mark.parametrize('name,num',[('自动化测试类型3','asd'),('自动化测试类型4','--'),('自动化测试类型5','++'),('自动化测试类型6','5555555555555555')])
    def test_guize3(self,name,num):
        '''
        对于达标次数输入框的检查
        :param name: 规则名称
        :param num: 达标次数
        :return:
        '''
        with allure.step('填写必要内容'):
           self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
           time.sleep(1)
           self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
           # 规则名称输入
           self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
           self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', name)
           # 输入规则描述
           self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
           self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
           # 选择任务型计数规则类型
           self.click('//*[@id="pane-0"]/form/div[1]/div/div/div/input')
           self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
        with allure.step('对于达标测试进行测试'):
           # 填写达标次数
           self.driver.find_element(By.CSS_SELECTOR,'#pane-0 > form > div:nth-child(5) > div > div > input').click()
           self.driver.find_element(By.CSS_SELECTOR,'#pane-0 > form > div:nth-child(5) > div > div > input').clear()
           time.sleep(2)
           self.input('//*[@id="pane-0"]/form/div[5]/div/div/input', num)
           time.sleep(2)
           # 点击提交按钮
           self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
           time.sleep(2)
        with allure.step('审查是否提交成功'):
            allure.attach(self.driver.get_screenshot_as_png(),'审查结果',allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('针对达标期限输入框的测试')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('timedemo',[0,9999999,'asd','()_)'])
    def test_guize3(self,timedemo):
        '''
        针对达标期限输入框的测试
        :return:
        '''
        with allure.step("填入基本信息"):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', timedemo)
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')

        with allure.step('填写规则组信息'):
            # 选择任务型计数规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]/span')
            # 选择达标期限选项
            self.click('//*[@id="pane-0"]/form/div[4]/div/div/label[2]/span[2]')
            # 输入达标期限时间
            self.click('//*[@id="pane-0"]/form/div[5]/div/div/input')
            self.clear('//*[@id="pane-0"]/form/div[5]/div/div/input')
            self.input('//*[@id="pane-0"]/form/div[5]/div/div/input',timedemo)
        with allure.step('提交'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交成功'):
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('针对消费金额输入框的测试')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('timedemo', ['asd', '()_)','_+_+_/*'])
    def test_guize3(self, timedemo):
        '''
        针对达标期限输入框的测试
        :return:
        '''
        with allure.step("填入基本信息"):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', timedemo)
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
        with allure.step('填写规则组信息'):
            # 选择消费金额规则类型
            self.click('//*[@id="pane-0"]/form/div[1]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[3]/span')
            # 针对消费金额输入框
            self.click('//*[@id="pane-0"]/form/div[4]/div/div/input')
            self.clear('//*[@id="pane-0"]/form/div[4]/div/div/input')
            self.input('//*[@id="pane-0"]/form/div[4]/div/div/input',timedemo)
        with allure.step('提交'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交成功'):
            time.sleep(2)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span') == '保存'

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('多条子规则的流程测试')
    @allure.severity(allure.severity_level.NORMAL)
    def test_guize4(self):
        '''
        检测包含多条子规则的流程测试(前端bug尚未改正)
        :return:
        '''
        with allure.step("填入基本信息"):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', 'timedemo')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            time.sleep(2)
        with allure.step('点击增加子规则按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/div[1]/button')
        with allure.step('切换至子规则2'):
            element7 = self.driver.find_element(By.XPATH,'//*[@id="tab-1"]')
            ActionChains(self.driver).move_to_element(element7).perform()
            ActionChains(self.driver).click().perform()
        with allure.step('填写新建子规则的内容'):
            self.click('//*[@id="pane-1"]/form/div[2]/div/button/span')
            element5 = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element5).perform()
            ActionChains(self.driver).click().perform()
            self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
        with allure.step('点击提交按钮'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交成功'):
            time.sleep(2)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input') == 'timedemo'
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.click('/html/body/div[2]/div/div[3]/button[2]/span')

    @allure.epic('后台商城系统')
    @allure.feature('发放规则模块')
    @allure.story("新增发放规则")
    @allure.title('多条规则组的流程测试')
    @allure.severity(allure.severity_level.NORMAL)
    def test_guize4(self):
        '''
        检测多条规组的流程测试(前端bug尚未改正)
        :return:
        '''
        with allure.step("填入基本信息"):
            self.url('https://pre-release.jyhk.com/txga/mall/#/marketing/marketing')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[9]/div/button[3]/span')
            # 规则名称输入
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', 'timedemo')
            # 输入规则描述
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[2]/div/div[1]/input', '自动化测试')
            time.sleep(3)
        with allure.step('点击新增规则组按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/button')
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[1]/div/div[2]/label/span[1]')
        with allure.step('填写新增规则组内容'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            time.sleep(1)
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[1]')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[3]/div/div/div/input')
            time.sleep(2)
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')

            time.sleep(2)
            self.click('//*[@id="pane-1"]/form/div[2]/div/button/span')
            element5 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[5]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div')
            ActionChains(self.driver).move_to_element(element5).perform()
            ActionChains(self.driver).click().perform()
            self.click('/html/body/div[5]/div/div[3]/div/div/div/button[2]')
        with allure.step('点击提交按钮'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否提交成功'):
            time.sleep(2)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input') == 'timedemo'
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.click('/html/body/div[2]/div/div[3]/button[2]/span')
