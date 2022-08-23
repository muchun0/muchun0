from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/11_单选框和复选框.html')
# driver.find_element_by_id('c2').click() # 复选框的单选与单选框一样，先定位元素，然后直接点击即可
# 复选框的全选
alist = driver.find_elements_by_xpath('//input[@type="checkbox"]')
for i in alist:
    if not i.is_selected():
        i.click()
sleep(3)
driver.quit()
