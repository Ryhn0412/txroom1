import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from txhoutai.selecet import select1


@allure.epic('后台商城系统')
@allure.feature('商品模块')
@allure.story('商品分类功能')
class Test_goodkind(select1):

    def setup_method(self):
        '''
        测试用例的初始化
        :return:
        '''
        self.shangcheng()
        self.url('https://pre-release.jyhk.com/txga/mall/#/goods/goodList')
        self.driver.implicitly_wait(10)
        element4 = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div/div[1]/div/div/input')
        ActionChains(self.driver).move_to_element(element4).click().perform()
        self.click('//*[@class="el-dialog__body"]/div[1]/div[3]/table/tbody/tr[2]/td[1]/div/label/span[1]')
        self.click('//*[@class="el-dialog__wrapper"]/div/div[3]/div/div/div/button[2]')

    def teardown_method(self):
        '''
        测试用例结束后的清理
        :return:
        '''
        time.sleep(1)
        print('_______________________该条用例测试结束_______________________')
        self.quit()

    @allure.epic('后台商城系统')
    @allure.feature('商品模块')
    @allure.story('商品分类功能')
    @allure.title('新增商品分类')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_goodkind(self):
        '''
        新增商品分类的流程测试
        :return:
        '''
        with allure.step('点击新建分类按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/div[1]/button')
        with allure.step('输入分类名称'):
            self.click('//*[@class="z-form-limit"]/div[1]/input')
            self.input('//*[@class="z-form-limit"]/div[1]/input', '自动化测试')
        with allure.step('点击确认按钮'):
            self.click('//*[@aria-label="新建分类"]/div[3]/div/div/div[2]/button[2]/span')
        with allure.step('审查是否出现新的分类'):
            time.sleep(1)
            assert self.getText(
                '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/ul/li[4]/div[1]') == '自动化测试(0)'

    @allure.epic('后台商城系统')
    @allure.feature('商品模块')
    @allure.story('商品分类功能')
    @allure.title('编辑商品分类')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_goodkinds(self):
        '''
        编辑商品分类的流程测试
        :return:
        '''
        with allure.step('点击商品分类的编辑按钮'):
            element1 = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/ul/li[4]/div[1]')
            ActionChains(self.driver).move_to_element(element1).click().perform()
            element2 = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/ul/li[4]/span[2]')
            ActionChains(self.driver).move_to_element(element2).click().perform()
        with allure.step('点击分类名称输入框'):
            self.click('//*[@class="el-popover__reference-wrapper"]/span/button/span')
            self.click('//*[@role="tooltip"]/div[2]/button[2]/span')
        with allure.step('输入此次编辑内容'):
            self.click('//*[@aria-label="编辑分类"]/div[2]/form/div/div/div/div/input')
            self.clear('//*[@aria-label="编辑分类"]/div[2]/form/div/div/div/div/input')
            self.input('//*[@aria-label="编辑分类"]/div[2]/form/div/div/div/div/input', '自动化编辑')
        with allure.step('点击提交按钮'):
            self.click('//*[@aria-label="编辑分类"]/div[3]/div/div/div[3]/button[2]/span')
        with allure.step('审查是否提交成功'):
            assert self.getText(
                '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/ul/li[4]/div[1]') == '自动化编辑(0)'

    @allure.epic('后台商城系统')
    @allure.feature('商品模块')
    @allure.story('商品分类功能')
    @allure.title('删除商品分类')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_goodkinds(self):
        '''
        删除商品分类的流程测试
        :return:
        '''
        with allure.step('点击商品分类的编辑按钮'):
            element1 = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/ul/li[4]/div[1]')
            ActionChains(self.driver).move_to_element(element1).click().perform()
            element2 = self.driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/ul/li[4]/span[2]')
            ActionChains(self.driver).move_to_element(element2).click().perform()
        with allure.step('点击删除分类按钮'):
            self.click('//*[@class="el-popover__reference-wrapper"]/span/button/span')
            self.click('//*[@role="tooltip"]/div[2]/button[2]/span')
