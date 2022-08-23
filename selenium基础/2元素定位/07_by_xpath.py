from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/xpath元素定位.html')
time.sleep(1)
# 通过xpath绝对路径定位元素，以 / 开头
# element = driver.find_element_by_xpath('/html/body/p/input')
# 通过xpath相对路径定位元素，以 // 开头
# element = driver.find_element_by_xpath('//input[@class="login"]') # xpath表达式：标签+属性
# element = driver.find_element_by_xpath\
#     ('//p[@id="login_user4"]/label') # 层级定位：//父元素标签[@父元素属性=”属性值“]/子元素标签
# element = driver.find_element_by_xpath('//p[@id="login_user4"]/label[2]')
# element = driver.find_element_by_xpath('//input[@class="login-test"]')
# element = driver.find_element_by_xpath\
#     ('//input[@class="login-test" and @name="user-test"]') # 逻辑定位： //标签名[@属性名1=”属性值1“ and @属性名2=”属性值2“]
element = driver.find_element_by_xpath('/html/body/p[4]/input[2]')
# 获取元素的HTML代码
print(element.get_attribute('outerHTML'))
time.sleep(1)
driver.close()
