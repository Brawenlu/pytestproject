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
import allure

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

import pytest,requests,json

@allure.feature("计算机的功能")

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
        # self.i=1
        print("开始计算")
        self.calc=Calc()
        # 实例化测试函数
        # 实例化对象使用self使得其作用域更大，实例变量

    def teardown_class(self):
        print("结束计算")

    @allure.story("测试加法")
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



    def test_loginsuccess(self):
        username ="Luwenbo"
        pwd="sangfor123"

    def setup_method(self):
        self.i = 1
        print(self.i)
    def teardown_method(self):
        print(self.i)
        self.i = self.i + 1

    @pytest.mark.parametrize('username,pwd',[
        ['abcdefg','12345'],
        ['dasdsad11','11111'],
        ['sd','dsadasdasda']
    ])
     # 参数化需要用到的需要定义，以列表形式,就在上方就行,必须在上方
    # 参数化传输
    # def setup_class(self):

    @allure.story("测试举例")
    def test_loginfailed(self,username,pwd):
        # print(self.i)
        # print(type(self.i))
        print("第"+str(self.i)+"条测试用例参数："+username)
        print("第"+str(self.i)+"条测试用例的密码:"+pwd)
        self.i = self.i + 1
        # print(self.i)
        # 同时运行的不能相加
        # username="luwenbo1"
        # pwd="sangfor@123"

    # def test_loginfiled2(self):
    #     username = "Luwenbo1"
    #     pwd = "sangfor1234"
    #
    # def test_loginfiled3(self):
    #     username = "Luwenbo11"
    #     pwd = "sangfor123454"

    @allure.title("验证测试人帖子topid是否满足")  #只可以在方法上面，@allure.step（‘’）只能放在类或者方法上面，with allure.step（’’）: 可以放在函数里面

    @pytest.mark.parametrize('topic_id',[
        "10704","10705","10706","10707"
    ])
    # @allure.link("https://ceshiren.com/t/topic/10704",name="allure报告")
    # @allure.testcase(TESTCASELINK, name='测试用例管理平台')
    @allure.issue("https://ceshiren.com/t/topic/10704",name="bug链接")
    @allure.story("测试人帖子测试功能")
    # 多个参数需要列表，单个只需要""
    def test_ceshiren(self,topic_id):
        # topic_id="10704"
        print(type(topic_id))
        # 使用f可以识别常量里面的变量
        with allure.step("访问【测试人】社区"):
            result=requests.get("https://ceshiren.com/t/topic/{}.json".format(topic_id))
            # {}format()和f{}都可以用格式化
            print(json.dumps(result.json(),sort_keys=True,indent=4))
        with allure.step("验证结果"):
            if "errors" in result.json():
                # 判断是否存在某个字段
                print(result.json()["errors"])
                # print("是")
            else:pass
        # if result.json()["errors"] !="":
        #     print(result.json()["errors"])
        # else:pass
            respnse_id=result.json()["id"]
            print(type(respnse_id))
            assert topic_id==str(respnse_id)
        allure.attach.file("C:\\Users\\Administrator\\Desktop\\psb.jpg", name="胖嘟",
                            attachment_type=allure.attachment_type.JPG)




class Testdemo():

    def test_print(self):
        print("这是另一个测试类的方法")

    def test_print2(self):
        print("这是另一个测试类的方法二")