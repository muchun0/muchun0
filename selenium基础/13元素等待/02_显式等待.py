from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.maximize_window()
# 显示等待，每1秒检查百度输入框是否出现，如果出现则进行下一步操作，否则继续等待，直到超过20秒就抛出超时异常
# WebDriverWait(driver,20,1).until(EC.presence_of_element_located((By.ID,'kw'))).send_keys('hello world!')
WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_id('kw')).send_keys('hello world!')
sleep(3)
driver.close()