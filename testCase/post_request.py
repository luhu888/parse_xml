# coding=utf-8
# author:luhu
from lib import xml_to_dic
import json
import unittest
import requests


class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):
        print('start test')
        pass

    def tearDown(self):
        print('end test')
        pass


class TestUserAPI(MyTest):    # 将单个接口封装成一个类，其中的方法是具体的测试用例

    def test_userAPI(self):     # self.用在方法属性中，表示该方法的属性，不会影响其他方法的属性
        url = xml_to_dic.xml_to_url()
        data = xml_to_dic.xml_to_body()
        print(data)
        r = requests.post(url=url, data=data)
        data = json.loads(r.text)
        response = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
        print('返回数据:' + response)
        print('--------------------------------------------------------------------------------')



