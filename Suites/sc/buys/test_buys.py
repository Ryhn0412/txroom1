import allure
import pytest

from base.selecet import select1
from page_actions.sc_action.buys_action import buys_action
from utils.yaml_decode import get_yaml, yaml_locator


@allure.epic("后台商城系统")
@allure.feature("商品订单模块")
@allure.story("订单管理功能")
@allure.severity(allure.severity_level.BLOCKER)
class Test_buys(select1):
    '''
    有关于订单模块的测试用例
    '''
    # file1适用于查找订单的所用的选择条件和输入内容
    file1 = get_yaml(yaml_locator(r'\sc_texts\buys_texts\selectbuys.ymal'))
    # file2适用于查找订单的所用的开始时间和结束时间
    file2 = get_yaml(yaml_locator(r'\sc_texts\buys_texts\timeselect.ymal'))
    # file3适用于切换订单状态界面的状态
    file3 = get_yaml(yaml_locator(r'\sc_texts\buys_texts\buffbuys.ymal'))

    @allure.epic("后台商城系统")
    @allure.feature("商品订单模块")
    @allure.story("订单管理功能")
    @allure.title("查看订单功能")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_lookbuys(self):
        '''
        主要测试查看订单功能的具体实现
        '''
        buys_action().lookbuys()

    @allure.epic("后台商城系统")
    @allure.feature("商品订单模块")
    @allure.story("订单管理功能")
    @allure.title("查找订单功能1")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('caseinfo', file1)
    def test_selectbuys(self, caseinfo):
        '''
        主要测试订单管理模块的查找功能实现
        '''
        buys_action().select(caseinfo['idea_select'], caseinfo['select_text'])

    @allure.epic("后台商城系统")
    @allure.feature("商品订单模块")
    @allure.story("订单管理功能")
    @allure.title("查找订单功能2")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('caseinfo', file2)
    def test_timeselect(self, caseinfo):
        '''
        主要测试订单管理模块的通过时间查找功能实现
        '''
        buys_action().time_select(caseinfo['start_time'], caseinfo['end_time'])

    @allure.epic("后台商城系统")
    @allure.feature("商品订单模块")
    @allure.story("订单管理功能")
    @allure.title("切换订单状态的界面展示")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('caseinfo', file3)
    def test_buff(self, caseinfo):
        '''
        主要测试订单状态的界面展示
        '''
        buys_action().buys_buff(caseinfo['buff_name'])
