#!/usr/bin/env python
# -*- coding: utf_8 -*-
import unittest
import time

from lib.HTMLTestRunner import HTMLTestRunner
from testCase import post_request

'''集体运行选中的测试用例'''
suite = unittest.TestSuite()  # 实例化测试集

suite.addTest(post_request.TestUserAPI('test_userAPI'))  # 增加测试用例

if __name__ == '__main__':
    test_unit = unittest.TestSuite()
    test_unit.addTest(suite)
    now = time.strftime('%Y-%m-%d %H-%M-%S')    # 获取当前的时间，并固定其格式
    filename = './report/' + now + 'test_result.html'    # 定义报告的存放位置
    fp = open(filename, 'wb')   # wb表示有读写权限
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title="api测试", description='新核云接口测试报告：')
    # 运行测试
    runner.run(suite)
    fp.close()      # 关闭文件对象，才能保存数据，生成文档
