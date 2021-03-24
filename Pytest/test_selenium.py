#!/usr/bin/env python
# encoding: utf-8
'''
@author: luwenbo
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 272077966@qq.com
@software: garner
@file: test_selenium.py
@time: 2021/3/23 0:01
@desc:
'''
import logging
import pprint
import time

import yaml
from selenium import webdriver


class Testselenium():
    def setup_class(self):
        logging.basicConfig(level=logging.DEBUG)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        # chrome_options.debugger_address = "localhost:9222"  #开启调试地址，默认本地即可  （chrome --remote-debugging-port=9222）设置好环境变量,如果要先登录那么这个就无效
        # 使用headless无界面浏览器模式
        # chrome_options.add_argument('--headless') # 增加无界面选项
        chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)  #只有导入了webdriver才可以出来(放入python的俺安装目录即可)
        # self.driver.get(r"https://work.weixin.qq.com/wework_admin/frame#customer/analysis")  #只需要调用一次

    def teardown_class(self):
        self.driver.quit()

    # def test_cookie(self):
    #     # print()
    #     time.sleep(10)
    #     cookies = self.driver.get_cookies()
    #     with open('data.yaml',"w",encoding="utf-8") as f:
    #         yaml.dump(cookies,f) #有中文encoding='utf-8',allow_unicode=True
    #     pprint.pprint(self.driver.get_cookies())  #通过yaml保存cookie到本地
    #     print("访问成功")

    def test_myweb(self):
        print("开始访问别的网页")
        #第一个是登录页面，第二个是地址页面获取cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#customer/analysis")
        with open(r"data.yaml",encoding="utf-8") as f:
            cookies = yaml.safe_load(f)  #load有Loader=yaml.FullLoader方法
        print(cookies)  #获取到cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(5)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#customer/analysis")
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_id("menu_profile").click()
        time.sleep(5)
        # pprint.pprint(self.driver.get("https://work.weixin.qq.com/wework_admin/frame#profile"))