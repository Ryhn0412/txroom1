import os
import time
import ddddocr
from selenium.webdriver.common.by import By
# from tx.webkeys1 import ryhn
from txhoutai.webkeys1 import ryhn

"""
主要用于登录后台系统首页
"""
class Login(ryhn):
    def longin1(self):
        """
        进行登录，难点在于验证码识别(主要用ddddocr这个库进行识别)
        :return:
        """
        self.openweb('ed')
        self.driver.maximize_window()
        self.url('https://pre-release.jyhk.com/txga/admin/#/login')
        # time.sleep(1)
        self.input('//*[@class="el-input"]/input','jyhk')
        self.input('//*[@type="password"]','kingtang=2020')
        """
        进行首次验证码识别
        """
        png = self.driver.find_element(By.XPATH,'//*[@id="s-canvas"]')
        png.screenshot('ocr.png')
        ocr = ddddocr.DdddOcr()
        with open("ocr.png", 'rb') as f:
            image = f.read()
        res = ocr.classification(image)

        self.input('//*[@class="el-form-item__content"]/div/input',res)
        self.click('//*[@type="button"]')
        time.sleep(3)
        """
        进行网页判断查看是否验证码通过
        未通过则继续识别
        """
        page = self.driver.current_url
        url2 = 'https://pre-release.jyhk.com/txga/admin/#/systemList'


        while(page != url2):
            # self.driver.refresh()
            page1 =self.driver.current_url
            if(page1 == url2):
                break
            time.sleep(3)

            image1 = self.getlocation()
            image_url = os.path.join(image1,'ocr.png')

            try:
                os.remove(image_url)
            except Exception as error:
                # 强制删除截屏获得的验证码图片
                os.system("del /f /q %s" % image_url)
            # 验证码再次识别
            png = self.driver.find_element(By.XPATH, '//*[@id="s-canvas"]')
            png.screenshot('ocr.png')
            ocr = ddddocr.DdddOcr()
            with open("ocr.png", 'rb') as f:
                image = f.read()
            res = ocr.classification(image)
            time.sleep(2)
            self.input('//*[@class="el-form-item__content"]/div/input', res)
            time.sleep(2)
            self.click('//*[@type="button"]')
            # 刷新page所得到的网址进行判断
            page = self.driver.current_url
            time.sleep(3)

        print('_______________________该条用例开始测试_______________________')








