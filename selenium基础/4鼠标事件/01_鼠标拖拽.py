from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/4_鼠标事件.html')
time.sleep(1)
red = driver.find_element_by_id('div1')
green = driver.find_element_by_id('div2')
ActionChains(driver).drag_and_drop(red,green).perform()
time.sleep(3)
driver.quit()