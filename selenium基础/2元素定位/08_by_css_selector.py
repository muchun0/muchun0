from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window() # 窗口最大化
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/css元素定位.html')
time.sleep(1)
# css元素定位，使用id属性定位
# element = driver.find_element_by_css_selector('#u1')
# css元素定位，使用class属性定位
# element = driver.find_element_by_css_selector('.u2')
# element = driver.find_element_by_css_selector('li[type="text"]') # css表达式：标签+属性
# element = driver.find_element_by_css_selector\
#     ('ul[class="u2"]>li[name="i2"]') # 层级定位：父元素标签[父元素属性=”属性值“]>子元素标签
# element = driver.find_element_by_css_selector('.u2>:nth-child(2)')  # 父元素标签[父元素属性=”属性值“]>:nth-child(索引)
# element = driver.find_element_by_css_selector\
#     ('li[name="i1"][type="text"]') # 逻辑定位： 标签名[属性名1=”属性值1“][属性名2=”属性值2“]
# element = driver.find_element_by_css_selector('.u2 > li:nth-child(2)')
element = driver.find_element_by_css_selector('html body ul.u2 li')
# 获取元素的HTML代码
print(element.get_attribute('outerHTML'))
time.sleep(1)
driver.close()
