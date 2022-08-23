from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(20) # 隐式等待,等待的是页面的所有元素，只设置一次即可
driver.find_element_by_id('kw').send_keys('hello world!')
sleep(3)
driver.close()