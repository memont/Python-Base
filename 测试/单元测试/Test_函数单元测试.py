#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'memont'
# Email   :
# File    :Test_函数单元测试.py
# Datetime:2018/8/21 18:43
# Project :Python-Base

from funTest import fsum
from funTest import fsub

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print("每个测试开始自动调用!")

    def tearDown(self):
        print("每个测试结束自动调用!")

    # 为了测试fsum
    def test_fsum(self):
        self.assertEqual(fsum(1, 2), 3, 'fsum error!')

    def test_fsub(self):
        self.assertEqual(fsub(3, 2), 1, 'fsub error!')


# python -m unittest Test_函数单元测试.py

if __name__ == '__main__':
    unittest.main()
