# -*- coding:utf-8 -*-
# @author Ryhn
# @date 2022-02-25
import os
import time

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

from txhoutai.selecet import select1

@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('后台商城系统')
@allure.feature('图片库模块')
class Test_picture(select1):

    def setup_method(self):
        '''
        测试用例的初始化
        :return:
        '''
        self.shangcheng()
        self.url('https://pre-release.jyhk.com/txga/mall/#/setupmall/pics')
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
    @allure.feature('图片库模块')
    @allure.story("新增图片功能")
    @allure.title('新增图片流程')
    @pytest.mark.flaky(reruns=5,reruns_delay=2)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addpicture(self):
        '''
        添加图片的测试用例
        :return:
        '''
        with allure.step('点击新增图片按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[2]/div/button[1]/span/i')
        with allure.step('点击图片分类选项'):
            self.click('/html/body/div[2]/div/div[2]/form/div[1]/div/div/div/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
        with allure.step('上传图片'):
            pic = os.path.join(self.getlocation(), './ocr.png')
            time.sleep(1)
            self.input('/html/body/div[2]/div/div[2]/form/div[2]/div/div/div[1]/div/input',pic)
        with allure.step('点击提交按钮'):
            element1 = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div/button[2]/span')
            ActionChains(self.driver).move_to_element(element1).perform()
            ActionChains(self.driver).click(element1).perform()
        with allure.step('审查是否出现新增图片'):
            allure.attach(self.driver.get_screenshot_as_png(),'新增图片',attachment_type=allure.attachment_type.PNG)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[3]/div') =='ocr'



    @allure.epic('后台商城系统')
    @allure.feature('图片库模块')
    @allure.story("查询图片功能")
    @allure.title('全条件搜索查询图片')
    @pytest.mark.flaky(reruns=1,reruns_delay=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_searchpicture1(self):
        '''
        全条件输入，进行查询图片的测试用例
        :return:
        '''
        with allure.step('点击搜索图片名称框'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/div/div/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/div/div/input','ocr')
        with allure.step('点击图片分类'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[2]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
        with allure.step('点击查询按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[3]/div/button[1]/span/i')
        with allure.step('审查查找结果'):
            allure.attach(self.driver.get_screenshot_as_png(),'查找图片结果',allure.attachment_type.PNG)
        with allure.step('点击重置按钮并查找'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[3]/div/button[2]/span/i')
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[3]/div/button[1]/span/i')

    @allure.epic('后台商城系统')
    @allure.feature('图片库模块')
    @allure.story("查询图片功能")
    @allure.title('通过图片名称查询图片')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_searchpicture2(self):
        '''
        通过搜索图片名称，进行查询图片的测试用例
        :return:
        '''
        with allure.step('点击搜索图片名称框'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/div/div/input')
            self.input('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/div/div/input', '自动化图片')
        with allure.step('点击查询按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[3]/div/button[1]/span/i')
        with allure.step('审查查找结果'):
            allure.attach(self.driver.get_screenshot_as_png(),'查找图片结果',allure.attachment_type.PNG)

    @allure.epic('后台商城系统')
    @allure.feature('图片库模块')
    @allure.story("查询图片功能")
    @allure.title('通过图片分类查找图片')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_searchpicture3(self):
        '''
        通过图片分类，进行查询图片的测试用例
        :return:
        '''
        with allure.step('点击图片分类'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[2]/div/div/div/input')
            self.click('/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
        with allure.step('点击查询按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[3]/div/button[1]/span/i')
        with allure.step('审查查找结果'):
            allure.attach(self.driver.get_screenshot_as_png(), '查找图片结果', allure.attachment_type.PNG)

    @allure.epic('后台商城系统')
    @allure.feature('图片库模块')
    @allure.story("编辑图片功能")
    @allure.title('编辑图片流程')
    # @pytest.mark.flaky(reruns=3, reruns_delay=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_changepicture(self):
        '''
        编辑图片的测试用例
        :return:
        '''
        with allure.step('点击图片编辑按钮'):
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/button[1]')
        with allure.step('修改图片名称'):
            time.sleep(1)
            self.click('/html/body/div[2]/div/div[2]/form/div[2]/div/div[1]/div[1]/div/div[2]')
            element3 = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/form/div[2]/div/div[1]/div[1]/div/div[2]')
            ActionChains(self.driver).move_to_element(element3).send_keys('自动化测试').perform()
            # self.input('/html/body/div[2]/div/div[2]/form/div[2]/div/div[1]/div[1]/div/div[2]/input','自动化测试')
        with allure.step('点击提交按钮'):
            self.click('/html/body/div[2]/div/div[3]/div/div/div/button[2]/span/i')
        with allure.step('审查修改结果'):
            time.sleep(1)
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[3]/div') =='ocr自动化测试'




    @pytest.mark.flaky(reruns=1,reruns_delay=1)
    @allure.epic('后台商城系统')
    @allure.feature('图片库模块')
    @allure.story("删除图片功能")
    @allure.title('删除图片流程')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_deletepicture(self):
        '''
        删除图片的测试用例
        :return:
        '''
        self.driver.refresh()
        with allure.step('点击删除按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/button[2]/span')
        with allure.step('确认删除'):
            self.click('/html/body/div[2]/div/div[3]/button[2]')
        with allure.step('审查是否删除'):
            assert self.getText('//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr[1]/td[3]/div') !='自动化测试'

