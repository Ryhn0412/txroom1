import os

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ryhn(object):
    def openweb(self, br=None):
        """
        启动浏览器
        :param br:ed即为edge浏览器，ff即为火狐浏览器，co即为chorm浏览器
        :return:
        """
        if br == 'ed':
            self.driver = webdriver.Chrome(
                r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
        elif br == 'ff':
            self.driver = webdriver.firefox()
        elif br == 'co':
            self.driver = webdriver.chrome()
        else:
            print('浏览器启动失败，切换其他浏览器尝试')
            # time.sleep(5)

    def locator(self, locator=None):
        """
        基本的元素定位
        :param locator: 
        :return: 
        """
        return self.driver.find_element(locator)

    def url(self, locator=None):
        """

        :param locator:填写相对应的网址
        :return:
        """
        self.driver.get(locator)

    def input(self, locator=None, keys=None):
        """
        对输入框填写内容
        :param locator:填写xpath地址
        :param keys: 填写输入内容
        :return:
        """
        self.driver.find_element(By.XPATH, locator).send_keys(keys)

    def click(self, locator=None):
        """
        :param locator:填写xpath地址 
        :return: 
        """
        self.driver.find_element(By.XPATH, locator).click()

    # def yeshu(self):
    #     """
    #     爬取页面数据
    #     :return:
    #     """
    #     url = 'https://www.jyhk.com/mall/#/shopmall/pics'
    #     headers = {'User-Agent':UserAgent().random}
    #     res = request.urlopen(url=url,headers=headers)
    #     html = res.read.decode("GB2312")
    #     pattern =re.compile(r'<div.*?<span class="el-pagonatopn__total">(.*?)</span.*?div>"')
    #     ye = pattern.match(html).groups(1)
    #     print(ye)
    #     # return ye
    def clear(self, locator=None):
        '''
        清除文本内容
        :return:
        '''
        self.driver.find_element(By.XPATH, locator).clear()

    def find(self, locator=None):
        '''
        定位元素
        :param locator: 输入该元素Xpath路径
        :return: 元素
        '''
        element1 = self.driver.find_element(By.XPATH, locator)
        return element1

    def getlocation(self):
        '''
        获取当前路径
        :return:
        '''
        a = os.getcwd()
        return a

    def getText(self, locator=None):
        '''
        获取当前的文本内容
        :return:
        '''
        text1 = self.driver.find_element(By.XPATH, locator).text
        return text1

    def getattributre(self, locator=None):
        '''
        获取元素内的任意属性值
        :return:
        '''
        attribute1 = self.driver.find_element(By.XPATH, locator).getAttribute()
        return attribute1

    def tagclick(self, yuansu=None, name=None):
        '''
        在class重复，没有id时候使用的点击方法（用tag_name做循环判断）
        :param name: get_text的内容
        :return: 返回一个点击效果
        '''
        list1 = self.driver.find_elements(By.TAG_NAME, yuansu)
        for element2 in list1:
            if element2.text == name:
                ActionChains(self.driver).move_to_element(element2).click().perform()
                break

    def catch_png(self):
        '''
        截图保存至allure报告的用例内
        :return:
        '''
        allure.attach(self.driver.get_screenshot_as_png(), '实际结果', attachment_type=allure.attachment_type.PNG)

    def quit(self):
        '''
        退出浏览器的操作
        :return:
        '''
        self.driver.quit()
