from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/11_单选框和复选框.html')
driver.find_element_by_id('boy').click() # 单选框，先定位元素，直接点击即可
sleep(3)
driver.quit()