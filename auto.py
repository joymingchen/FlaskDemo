# -*- coding:utf8 -*-
from selenium import webdriver
import time


class common(object):
    def __init__(self):
        self.driver = webdriver.Chrome("D:\\ProgramData\\Miniconda3\\chromedriver.exe")
        self.driver.maximize_window()

    # 打开网页功能
    def open(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    # 点击
    def click(self, key):
        self.driver.find_element_by_id(key).click()
        self.driver.implicitly_wait(5)

    # 输入
    def input(self, key, word):
        self.driver.find_element_by_id(key).clear()
        self.driver.find_element_by_id(key).send_keys(word)
        self.driver.implicitly_wait(5)

    # 切换到新的页面
    def new_window(self):
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        # time.sleep(3)

    # 关闭网页功能
    def close(self):
        time.sleep(3)
        self.driver.close()


driver = common()
driver.open("https://www.baidu.com/")
driver.click("lg")
driver.new_window()
driver.input("kw", "Jesus")
driver.click("su")
