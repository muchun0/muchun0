from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/8_退出表单.html')
driver.switch_to.frame('f1')
driver.switch_to.frame('f2')
driver.find_element_by_id('kw').send_keys('比特币')
driver.find_element_by_id('su').click()
sleep(2)
# driver.switch_to.parent_frame()
# driver.switch_to.parent_frame()
driver.switch_to.default_content() # 返回最外层
# driver.refresh()
sleep(2)
print(driver.find_element_by_id('f_h').text)
driver.switch_to.frame('f1')
print(driver.find_element_by_id('inn').text)
driver.quit()