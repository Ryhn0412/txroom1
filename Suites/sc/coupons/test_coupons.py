# -*- coding:utf-8 -*-
# @author Ryhn
# @date 2022-02-21
import datetime
import time
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from txhoutai.selecet import select1

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
    @pytest.mark.flaky(reruns=1,reruns_dalay=2)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_selectcoupon(self):
        '''
        查询发放规则的测试
        查询条件：测试（名称）糖心关爱（店铺）进行中（状态）当前时间-两百年后（发放时间）
        :return:
        '''

        with allure.step("输入查询的规则名称"):
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[1]/div/div/div/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/form/div/div[1]/div/div/div/input','测试')
        with allure.step("输入查询的店铺名称"):
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/div/div/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/div/div/input','糖心关爱')
        with allure.step("选择状态"):
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[3]/div/div/div/div[1]')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')
        with allure.step("选择发放时间"):
            ry1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 自动定位当前时间为开始时间
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[4]/div/div/div/input[1]')
            self.input('//*[@id="app"]/div/div[2]/section/div/form/div/div[4]/div/div/div/input[1]',ry1)
            # 手动输入结束时间
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[4]/div/div/div/input[2]')
            self.input('//*[@id="app"]/div/div[2]/section/div/form/div/div[4]/div/div/div/input[2]','2200-12-25 00:00:00')
        with allure.step("点击查询按钮"):
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[5]/button[1]/span')
        with allure.step("断言查询结果,并截图"):
            allure.attach(self.driver.get_screenshot_as_png(), '查询结果', attachment_type=allure.attachment_type.PNG)
            assert self.getText\
                        ('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div')== '自动化测试'
        with allure.step("恢复列表"):
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[5]/button[2]/span')
            self.click('//*[@id="app"]/div/div[2]/section/div/form/div/div[5]/button[1]/span')

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
            with allure.step("点击新增规则按钮"):
                self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/button/span')

                # 规则名称输入
                self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input')
                self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/form/div[1]/div/div[1]/input', '自动化测试3232')
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
                time.sleep(3)
                self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
                self.click('/html/body/div[2]/div/div[3]/button[2]/span')
            with allure.step('点击编辑按钮'):
                self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]/span')
                time.sleep(1)
            with allure.step('审查是否进入编辑界面'):
                time.sleep(1)
                assert self.getText('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/label') =='店铺名称'
            with allure.step('点击删除按钮'):
                time.sleep(2)
                self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            with allure.step('审查是否删除'):
                time.sleep(1)
                assert self.getText('//*[@id="app"]/div/div[2]/section/div/form/div/div[2]/div/label') == '店铺名称'
                # 测试结束，删除该条规则
                time.sleep(1)
                self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
                self.click('/html/body/div[2]/div/div[3]/button[2]/span')
                self.click(
                    '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
                self.click('/html/body/div[2]/div/div[3]/button[2]/span')



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
        with allure.step('点击编辑按钮'):
              self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]/span')
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
        with allure.step('点击提交按钮'):
              self.click('//*[@id="app"]/div/div[2]/section/div/div[4]/button[2]/span')
        with allure.step('审查是否编辑成功'):
              assert \
                  self.getText\
                      ('//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div') =='修改自动化'

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
        with allure.step('点击删除按钮'):
            self.click(
                    '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[4]/span')
            self.click('/html/body/div[2]/div/div[3]/button[2]/span')
        with allure.step('审查删除的结果并截图'):
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), '删除结果', attachment_type=allure.attachment_type.PNG)
            assert self.getText(
                    '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div') != '自动化编辑测试'