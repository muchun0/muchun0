import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://wwww.baidu.com')
time.sleep(2)
driver.get('https://www.jd.com')
time.sleep(2)
driver.back() # 后退到百度
time.sleep(2)
driver.forward() # 前进到京东
time.sleep(2)
driver.refresh() # 刷新
time.sleep(2)
driver.close()