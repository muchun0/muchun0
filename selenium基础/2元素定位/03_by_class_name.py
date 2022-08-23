from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html')
time.sleep(2)
# 通过元素的class属性定位元素,class允许有多个属性值，定位时选择任意值即可
class_name = driver.find_element_by_class_name('telA')
# 获取元素的HTML代码
print(class_name.get_attribute('outerHTML'))
time.sleep(2)
driver.close()