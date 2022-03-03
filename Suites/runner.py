
import os
import pytest
#
pytest.main(['-s','-v','--alluredir','./result/'])
os.system('allure generate ./result/ -o ./report --clean')
