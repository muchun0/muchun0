from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/12_文件上传.html')
sleep(3)
driver.find_element_by_tag_name('input').send_keys(r'C:\Users\Administrator\Desktop\test.txt')
sleep(3)
driver.quit()