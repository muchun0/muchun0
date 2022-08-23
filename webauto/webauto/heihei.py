from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.maximize_window()
a = driver.find_element_by_id('kw')
a.send_keys('股市行情')
sleep(2)
# WebDriverWait(driver,20).until(EC.presence_of_element_located(('name','tj_login'))).click()
# 通过lambda方法，定位元素
WebDriverWait(driver,20).until(lambda x:x.find_element_by_name('tj_login')).click()
sleep(3)
driver.quit()
