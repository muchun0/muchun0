from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/8_进入表单.html')
# driver.switch_to_frame() # 进入嵌套页面的老方法，还未被移除，不推荐使用
# 进入嵌套页面，实参可以传入id属性值、name属性值、frame元素对象、索引
# driver.switch_to.frame('f2') # 传入frame标签的id属性值
# driver.switch_to.frame('if2') # 传入frame标签的name属性值
# driver.switch_to.frame(driver.find_element_by_id('f2')) # 传入frame标签元素对象
driver.switch_to.frame(0) # 传入frame元素的索引，从0开始
driver.find_element_by_id('kw').send_keys('比特币')
sleep(2)
driver.switch_to.parent_frame() # 返回上一层
print(driver.find_element_by_tag_name('h3').text)
driver.quit()