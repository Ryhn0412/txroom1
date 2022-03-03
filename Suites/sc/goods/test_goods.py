import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from txhoutai.selecet import select1


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic('后台商城系统')
@allure.feature('商品模块')
class Test_goods(select1):
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
    @allure.story("删除商品功能")
    @allure.title('删除商品的流程')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_deletegood(self):
        '''
        删除商品的流程测试
        :return:
        '''
        element6 = self.driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[1]/div/ul/li[2]')
        ActionChains(self.driver).move_to_element(element6).click().perform()
        with allure.step('点击删除按钮'):
            self.click(
                '//*[@id="app"]/div/div[2]/section/div/div/div[4]/div[2]/div/div[3]/table/tbody/tr/td[7]/div/button[3]/span')
        with allure.step('确认删除'):
            self.click(
                '/html/body/div[3]/div/div[3]/button[2]/span')
