#!/usr/bin/env python
# encoding: utf-8
'''
@author: luwenbo
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 272077966@qq.com
@software: garner
@file: test_setup.py
@time: 2021/3/21 22:05
@desc:
'''


# def setup_class(self):
#     print("这是类级别的setup")
#
#
# def teardown_class(self):
#     print("这是类级别的teardown")
#

# 模块级别在整个文件运行前后调用

def setup_module():
    print("模块级别的setup")

def teardown_module():
    print("模块级别的Teardown")

# 只会对类外面的函数生效

def setup_function():
    print("函数级别的setup")

def teardown_function():
    print("函数级别的teardown")

def test_fun1():
    print("测试函数")



class Testdemo():

    # 类级别的setup只会在每一个类中调用一次
    def setup_class(self):
        print("这是类级别的setup")
    def teardown_class(self):
        print("这是类级别的teardown")


    # 默认的setup每一条测试用例都会调用
    def setup(self):
        print("默认方法级别的setup")
    def teardown(self):
        print("默认方法级别的teardown")

    def test_demo1(self):
        print("这是一个测试demo")

    def test_demo2(self):
        print("这是另一个测试demo")

class Testdemo2():
    def test_demo1(self):
        print("这是一个测试demo")

    def test_demo2(self):
        print("这是另一个测试demo")
