# -*- coding:utf8 -*-

import time

from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
#
# browser = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()

address = "www.baidu.com"

driver.get(url=address)

# driver.find_element_by_id("kw").send_keys(u"龙市唐川")
#
# driver.find_element_by_id("su").click()
#
# time.sleep(5)
#
# driver.find_element_by_id("1").find_element_by_tag_name("a").click()
