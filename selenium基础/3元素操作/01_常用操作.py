# 1、导包
import time
from selenium import webdriver
# 2、打开浏览器（火狐）
driver = webdriver.Firefox()
# 3、打开测试网站(百度）
driver.get(url='https://www.baidu.com')
time.sleep(1)
# 4、对测试网站进行操作
# 分步写法：先定位元素，用返回的元素对象调用输入方法
ele = driver.find_element_by_id('kw')
ele.send_keys('比特币') # 输入方法
time.sleep(1)
ele.clear()
time.sleep(1)
ele.send_keys('婚恋')
time.sleep(1)
# 链式写法
driver.find_element_by_id('su').click() # 点击
time.sleep(3)
# 5、关闭浏览器
driver.close()