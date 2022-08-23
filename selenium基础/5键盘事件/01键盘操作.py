from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html')
time.sleep(1)
userA = driver.find_element_by_id('userA')
userA.send_keys('13568880888')
time.sleep(0.5)
userA.send_keys(Keys.TAB + '123456')
time.sleep(2)
userA.send_keys(Keys.CONTROL,'a') # 全选
userA.send_keys(Keys.CONTROL,'c') # 复制
userA.send_keys(Keys.TAB + Keys.TAB +Keys.CONTROL,'v')
time.sleep(3)
driver.quit()