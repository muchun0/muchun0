from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html')
time.sleep(1)
userA_label = driver.find_element_by_css_selector('#p1 > label:nth-child(1)')
print(userA_label.text)  # 获取元素文本【掌握】
passwdA = driver.find_element_by_id('passwordA')
print(passwdA.get_attribute('placeholder')) # 获取元素的属性值,传入的实参为属性名
lia = driver.find_element_by_id('lia')
print(lia.is_selected()) # 判断元素是否被选择
time.sleep(1)
cancelA = driver.find_element_by_id('cancelA') # 定位隐藏元素
print(cancelA.is_displayed()) # 判断元素是否可见
print(cancelA.is_enabled()) # 判断元素是否可用
# cancelA.click() # 隐藏元素不可交互
print(driver.find_element_by_id('yyA').is_enabled())
driver.quit()