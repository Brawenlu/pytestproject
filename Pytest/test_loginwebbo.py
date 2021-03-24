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
import pprint
import time
import yaml

from selenium import webdriver




class Test():
    def setup_class(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver.get("https://weibo.com/brawenfire/home")
        self.driver.implicitly_wait(5)
        time.sleep(15)

    def teardown_class(self):
        print("访问结束")
        self.driver.quit()
    #
    def test_getcookies(self):
        time.sleep(3)
        cookies = self.driver.get_cookies()
        # jsoncookies = json.dumps(cookies,indent=True,sort_keys=4)  不能用这个格式再存，直接用yaml，或者json.dumps然后 f.write(jsonCookies)
        pprint.pprint(cookies)
        with open ("weibo.yaml","w") as f:
            yaml.dump(cookies,f)
        pprint.pprint(cookies)

    def test_login(self):
        self.driver.get(r"https://weibo.com/")
        time.sleep(4)
        with open(r"weibo.yaml",encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        print(cookies)
        for c in cookies:
            self.driver.add_cookie(c)
        self.driver.refresh()
        time.sleep(5)
        print("登陆成功")