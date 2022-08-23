from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html')
time.sleep(2)
# 通过元素的标签名定位元素,以列表形式返回所有符合条件的元素
element = driver.find_elements_by_tag_name('input')
# print(element)
for i in element:
    print(i.get_attribute('outerHTML'))
# 通过元素的标签名定位元素,find_element_by_tag_name以对象形式返回的是第一个符合条件的元素
# element = driver.find_element_by_tag_name('input')
# # 获取元素的HTML代码
# print(element.get_attribute('outerHTML'))
time.sleep(2)
driver.close()