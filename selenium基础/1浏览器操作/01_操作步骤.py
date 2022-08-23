# 1、导包
import time
from selenium import webdriver
# 2、打开浏览器（火狐）
driver = webdriver.Firefox()
time.sleep(2)
# 3、打开测试网站(百度）
driver.get(url='https://www.baidu.com')
time.sleep(2)
# 4、对测试网站进行操作
# 5、关闭浏览器
driver.close()