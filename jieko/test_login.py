import requests


class Test_start:
    def test_login(self):
        url = 'https://pre-release.jyhk.com/txga/ecp-manage-sys/japi/v1/manage/admin/login'
        data = {
            "loginName": "jyhk",
            "loginPwd": "kingtang=2020",
            "manCaptcha": {
                "captchaKey": "string",
                "capthchaValue": "string"},
            "type": 0
        }
        res = requests.post(url=url, json=data, verify=False)
        print(res.json())

    # if __name__ == '__main__':
    #     pytest.main(['-vs'])
