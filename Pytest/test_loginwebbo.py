#!/usr/bin/env python
# encoding: utf-8
'''
@author: luwenbo
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 272077966@qq.com
@software: garner
@file: test_loginwebbo.py
@time: 2021/3/24 0:27
@desc:
'''
import json
import time

from selenium import webdriver




class Test():
    def setup_class(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("https://weibo.com/login.php")
        self.driver.implicitly_wait(5)
        time.sleep(5)

    def teardown_class(self):
        print("访问结束")
        self.driver.quit()

    def test_getcookies(self):
        cookies = self.driver.get_cookies()
        jsoncookies = json.dumps(cookies,indent=True,sort_keys=4)
        print(jsoncookies)
        with open ("weibo.txt","w") as f:
            f.write(jsoncookies)

    def test_login(self):
        print("登陆成功")