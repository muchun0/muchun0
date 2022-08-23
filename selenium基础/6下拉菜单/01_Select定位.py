import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/6_select下拉菜单.html')
# 方法1：直接定位下拉菜单中的具体元素
# driver.find_element_by_css_selector('#select_demo > option:nth-child(2)').click()
# 方法2：使用Select类定位下拉菜单，然后使用该类提供的方法定位菜单中的具体元素（标签名必须是select）
select_tag = driver.find_element_by_id('select_demo')
Select(select_tag).select_by_value('strawberry') # 通过value属性值定位菜单中的元素
time.sleep(2)
Select(select_tag).select_by_visible_text('葡萄') # 通过元素的文字信息定位菜单中的元素
time.sleep(3)
Select(select_tag).select_by_index(4) # 通过元素的索引定位菜单中的元素
time.sleep(2)
driver.quit()