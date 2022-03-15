import allure
import pytest

from base.selecet import select1
from page_actions.sc_action.buys_action.look_action import look_action
from utils.yaml_decode import get_yaml, yaml_locator


@allure.epic("后台商城系统")
@allure.feature("商品订单模块")
@allure.story("订单管理功能")
@allure.severity(allure.severity_level.CRITICAL)
class Test_buys(select1):
    '''
    有关于订单模块的测试用例
    '''

    file1 = get_yaml(yaml_locator(r'\sc_texts\buys_texts\lookbuys.ymal'))

    @allure.epic("后台商城系统")
    @allure.feature("商品订单模块")
    @allure.story("订单管理功能")
    @allure.title("查看订单功能")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("text1", file1)
    def test_lookbuys(self, text1):
        look_action().lookbuys(text1)
