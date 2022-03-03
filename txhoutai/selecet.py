import time

# from wuqiku.login import Login
from txhoutai.login import Login


class select1(Login):


    def pingta(self):
        """
        选择进入平台管理系统
        :return:
        """
        self.longin1()
        self.click('//*[@id="app"]/div/div[3]/div/div/ul/li/div[1]/p')
        time.sleep(1)
    def jigou(self):
        """
        选择进入机构管理系统
        :return:
        """
        self.longin1()
        self.click('//*[@id="app"]/div/div[3]/div/div/ul/li/div[2]/p')
        time.sleep(1)
    def yaoshi(self):
        """
        选择进入药事管理系统
        :return:
        """
        self.longin1()
        self.click('//*[@id="app"]/div/div[3]/div/div/ul/li/div[3]/p')
        time.sleep(1)
    def fuzheng(self):
        """
        选择进入复诊管理系统
        :return:
        """
        self.longin1()
        self.click('//*[@id="app"]/div/div[3]/div/div/ul/li/div[4]/p')
        time.sleep(1)
    def shangcheng(self):
        """
        选择进入商城管理系统
        :return:
        """
        self.longin1()
        self.click('//*[@id="app"]/div/div[3]/div/div/ul/li/div[5]/p')
        time.sleep(1)