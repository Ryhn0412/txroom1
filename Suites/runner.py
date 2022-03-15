import os

import pytest

from utils.emailzip import make_zip

# 启动测试
pytest.main(['-s', '-v', '--alluredir', './report/result/'])
# 生成报告文件
os.system('allure generate ./report/result/ -o ./report/allure1 --clean')
# 获取报告路径
report_dir = os.getcwd() + "./report"
# 调用打包方法，对报告进行ZIP压缩
make_zip(report_dir, "test_report" + ".zip")
