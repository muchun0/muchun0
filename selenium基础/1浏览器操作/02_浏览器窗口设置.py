from selenium import webdriver
import time
driver = webdriver.Firefox()
time.sleep(2)
# driver.set_window_size(800,1000) # 自定义窗口大小，单位是像素
driver.maximize_window() # 窗口最大化
driver.get('https://www.baidu.com')
time.sleep(2)
driver.close()