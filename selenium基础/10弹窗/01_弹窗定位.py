from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/10_弹窗.html')
sleep(2)
# driver.find_element_by_id('buttonA').click()
# driver.find_element_by_id('buttonB').click()
driver.find_element_by_id('buttonC').click()
# sleep(1)
# print(driver.switch_to.alert.text) # 获取弹窗的文本
# driver.switch_to.alert.accept() # 点击弹窗确定按钮
# sleep(2)
# driver.switch_to.alert.dismiss() # 点击弹窗取消按钮
driver.switch_to.alert.send_keys('123456') # 弹窗输入
driver.switch_to.alert.accept()
sleep(2)
driver.quit()