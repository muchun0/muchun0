from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html')
time.sleep(2)
# 通过超链接的全部文字定位元素
element = driver.find_element_by_link_text('访问 新浪 网站')
# 获取元素的HTML代码
print(element.get_attribute('outerHTML'))
time.sleep(2)
driver.close()