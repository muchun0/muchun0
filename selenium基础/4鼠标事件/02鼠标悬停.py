from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/4_鼠标事件.html')
time.sleep(1)
submitA = driver.find_element_by_id('submitA')
ActionChains(driver).move_to_element(submitA).perform()
time.sleep(3)
driver.quit()