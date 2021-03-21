#!/usr/bin/env python
# encoding: utf-8
'''
@author: luwenbo
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 272077966@qq.com
@software: garner
@file: test_calc.py
@time: 2021/3/21 16:53
@desc:
'''
from Pytest.Caculartor import Calc

# 导入另一个测试方法的函数

# def setup_module(self):
#     calc = Calc()

# def setup_module():
#     # calc=Calc()
#     print("这是一个模块级别的初始化")
#
# def teardown_module():
#     print("这是一个模块级别的结束")




class Testcalc():

    # def setup_function(self):
    #     print("这是一个函数级别的初始化")
    #
    # def teardown_function(self):
    #     print("这是一个函数级别的结束")
    # def setup_class(self):
    #     print("这是一个类级别的初始化")
    # def teardown_class(self):
    #     print("这是一个类级别的结束")
    #
    # def setup_method(self):
    #     print("这是一个方法接别的初始化")
    #
    # def teardown_method(self):
    #     print("这是一个方法接别的结束")

    def setup_class(self):
        print("开始计算")
        self.calc=Calc()
        # 实例化测试函数
        # 实例化对象使用self使得其作用域更大，实例变量

    def teardown_class(self):
        print("结束计算")

    def test_add(self):
        # calc = Calc()
        result = self.calc.add(1,1)
        assert result==2

    def test_add1(self):
        # calc = Calc()
        result = self.calc.add(1.1,1.1)
        assert result==2.2

    def test_add2(self):
        # calc = Calc()
        result = self.calc.add(-1,-1)
        assert result==-2

class Testdemo():

    def test_print(self):
        print("这是另一个测试类的方法")

    def test_print2(self):
        print("这是另一个测试类的方法二")