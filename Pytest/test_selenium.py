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
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def teardown_class(self):
        self.driver.quit()

    def test_cookie(self):
        # print()
        time.sleep(15)
        pprint.pprint(self.driver.get_cookies())
        print("访问成功")

    def test_myweb(self):
        print("开始访问别的网页")
        pprint.pprint(self.driver.get("https://work.weixin.qq.com/wework_admin/frame#profile"))