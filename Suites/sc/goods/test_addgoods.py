import os.path
import time

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from txhoutai.selecet import select1

@allure.epic('后台商城系统')
@allure.feature('商品模块')
@allure.story("新增商品功能")
class Test_addgoods(select1):

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
    @allure.story("新增商品功能")
    @allure.title('新增商品流程')
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addgood1(self):
        '''
        检验添加商品的流程测试
        :return:
        '''
        with allure.step('点击新增商品按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[1]/button[1]')

        with allure.step('填入基本信息'):
            # 填写商品名称
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input', '商品价格输入')
            # 上传商品图片
            path = self.getlocation()
            path1 = os.path.join(path, 'ocr.png')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input', path1)
            # 选择分类
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[3]/div/div/div/input')
            self.click('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
        with allure.step('填写销售信息'):
            # 选择性别
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[1]/div/div/label[1]/span[1]/span')
            # 填写商品价格
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input')
            self.input(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input',
                12)
            # 点击数量自动补足按钮
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input')
            self.input(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input',
                11)
            # 选择上架时间
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
        with allure.step('填写商品详情'):
            # 填写购买须知
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[2]')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[1]/span')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div/div/label[1]/span[1]/span')
            # 填写商品详情
            self.click('//*[@id="wangeditor"]/div[2]/div[1]')
            self.input('//*[@id="wangeditor"]/div[2]/div[1]', '自动化测试')
        with allure.step('点击提交按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span')



    # @allure.epic('后台商城系统')
    # @allure.feature('商品模块')
    # @allure.story("新增商品功能")
    # @allure.title('新增商品流程')
    # # @pytest.mark.flaky(reruns=1, reruns_delay=1)
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_addgood2(self):
    #     '''
    #     检验商品不同分类的测试
    #     :return:
    #     '''
    #     with allure.step('点击新增商品按钮'):
    #         time.sleep(1)
    #         self.click('//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[1]/button[1]')
    #     with allure.step('填入基本信息'):
    #         # 填写商品名称
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input')
    #         time.sleep(1)
    #         self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input','自动化商品')
    #         # 上传商品图片
    #         time.sleep(1)
    #         path =self.getlocation()
    #         path1 = os.path.join(path,'ocr.png')
    #         self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input',path1)
    #         # 选择分类
    #         time.sleep(1)
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[3]/div/div/div/input')
    #         self.click('/html/body/div[2]/div[1]/div[1]/ul/li[3]/span')
    #         time.sleep(1)
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[4]/div/div/div/input')
    #         self.click('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
    #         # 服务类型
    #         element1 = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[5]/div/div/div')
    #         ActionChains(self.driver).move_to_element(element1).click().perform()
    #         time.sleep(1)
    #
    #
    #         # 医生职称
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[6]/div/div[1]/div/input')
    #         self.click('/html/body/div[7]/div[1]/div[1]/ul/li[1]/span')
    #     with allure.step('填写销售信息'):
    #         # 选择性别
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[1]/div/div/label[1]/span[1]/span')
    #         # 填写商品价格
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input')
    #         self.input('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input','55')
    #         # 点击数量自动补足按钮
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/label/span[1]')
    #         # 选择上架时间
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[4]/div/div/div/input')
    #         self.input('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[4]/div/div/div/input','立即上架')
    #     with allure.step('填写商品详情'):
    #         # 填写购买须知
    #         time.sleep(2)
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[1]/span')
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div/div/label[1]/span[1]/span')
    #         # 填写商品详情
    #         self.click('//*[@id="wangeditor"]/div[2]/div[1]')
    #         self.input('//*[@id="wangeditor"]/div[2]/div[1]','自动化测试')
    #     with allure.step('点击提交按钮'):
    #         self.click('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span')

    @allure.epic('后台商城系统')
    @allure.feature('商品模块')
    @allure.story("新增商品功能")
    @allure.title('针对商品标题的测试')
    @pytest.mark.parametrize('name',['自动化商品',''])
    @allure.severity(allure.severity_level.NORMAL)
    def test_goodstitle(self,name):
        '''
        针对商品标题的测试(前端未设定商品不可重复)
        :param name: 商品标题的不同输入
        :return:
        '''
        with allure.step('点击新增商品按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[1]/button[1]')

        with allure.step('填入基本信息'):
            # 填写商品名称
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input', name)
            # 上传商品图片
            path = self.getlocation()
            path1 = os.path.join(path, 'ocr.png')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input', path1)
            # 选择分类
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[3]/div/div/div/input')
            self.click('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
        with allure.step('填写销售信息'):
            # 选择性别
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[1]/div/div/label[1]/span[1]/span')
            # 填写商品价格
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input')
            self.input(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input',
                '11')
            # 点击数量自动补足按钮
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input')
            self.input(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input',
                '11')
            # 选择上架时间
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
        with allure.step('填写商品详情'):
            # 填写购买须知
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[2]')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[1]/span')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div/div/label[1]/span[1]/span')
            # 填写商品详情
            self.click('//*[@id="wangeditor"]/div[2]/div[1]')
            self.input('//*[@id="wangeditor"]/div[2]/div[1]', '自动化测试')
        with allure.step('点击提交按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span')
            time.sleep(1)
        with allure.step('审查是否提交失败'):
            assert self.getText('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span') == '提交商品'

    @allure.epic('后台商城系统')
    @allure.feature('商品模块')
    @allure.story("新增商品功能")
    @allure.title('针对商品价格的测试')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('num',['asd','_+/*','','-1','0'])
    def test_goodprice(self,num):
        '''
        针对价格输入进行测试
        :return:
        '''
        with allure.step('点击新增商品按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[1]/button[1]')

        with allure.step('填入基本信息'):
            # 填写商品名称
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input', '商品价格输入')
            # 上传商品图片
            path = self.getlocation()
            path1 = os.path.join(path, 'ocr.png')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input', path1)
            # 选择分类
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[3]/div/div/div/input')
            self.click('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
        with allure.step('填写销售信息'):
            # 选择性别
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[1]/div/div/label[1]/span[1]/span')
            # 填写商品价格
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input')
            self.input(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input',
                num)
            # 点击数量自动补足按钮
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input')
            self.input(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input',
                111)
            # 选择上架时间
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
        with allure.step('填写商品详情'):
            # 填写购买须知
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[2]')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[1]/span')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div/div/label[1]/span[1]/span')
            # 填写商品详情
            self.click('//*[@id="wangeditor"]/div[2]/div[1]')
            self.input('//*[@id="wangeditor"]/div[2]/div[1]', '自动化测试')
        with allure.step('点击提交按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span')
            time.sleep(1)
        with allure.step('审查是否提交失败'):
            assert self.getText('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span') == '提交商品'

    @allure.epic('后台商城系统')
    @allure.feature('商品模块')
    @allure.story("新增商品功能")
    @allure.title('针对商品数量的测试')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('num', ['asd', '_+/*', '', '-1', '0'])
    def test_goodprice(self, num):
        '''
        针对价格输入进行测试
        :return:
        '''
        with allure.step('点击新增商品按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[1]/button[1]')
        with allure.step('填入基本信息'):
            # 填写商品名称
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[1]/div/div[1]/div[1]/input', '商品价格输入')
            # 上传商品图片
            path = self.getlocation()
            path1 = os.path.join(path, 'ocr.png')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input', path1)
            # 选择分类
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[3]/div/div/div/input')
            self.click('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')
            time.sleep(1)
            self.click('//*[@id="app"]/div/div[2]/section/form/div[1]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')
        with allure.step('填写销售信息'):
            # 选择性别
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[1]/div/div/label[1]/span[1]/span')
            # 填写商品价格
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input')
            self.input(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div/div/div/div[1]/input',
                num)
            # 点击数量自动补足按钮
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input')
            self.input('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[2]/div[3]/table/tbody/tr/td[3]/div/div/div/div[1]/input',num)
            # 选择上架时间
            self.click('//*[@id="app"]/div/div[2]/section/form/div[2]/div[2]/div[4]/div/div/div/input')
            self.click('/html/body/div[5]/div[1]/div[1]/ul/li[1]/span')
        with allure.step('填写商品详情'):
            # 填写购买须知
            self.click('//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[2]')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/div/div/div/label/span[1]/span')
            self.click(
                '//*[@id="app"]/div/div[2]/section/form/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/div/div/label[1]/span[1]/span')
            # 填写商品详情
            self.click('//*[@id="wangeditor"]/div[2]/div[1]')
            self.input('//*[@id="wangeditor"]/div[2]/div[1]', '自动化测试')
        with allure.step('点击提交按钮'):
            self.click('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span')
            time.sleep(1)
        with allure.step('审查是否提交失败'):
            assert self.getText('//*[@id="app"]/div/div[2]/section/form/div[4]/button/span') == '提交商品'
