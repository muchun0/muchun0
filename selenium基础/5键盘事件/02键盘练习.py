'''
需求：
1.账号A中输入12位电话，然后删掉最后一位
2.输入密码
3.复制账号A中的电话，粘贴到电话号码A输入框中
4.输入电子邮件，然后回车
注：全部使用键盘实现
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/%E6%B3%A8%E5%86%8CA.html')
userA = driver.find_element_by_id('userA')
userA.send_keys('134567856789')
time.sleep(2)
userA.send_keys(Keys.BACKSPACE)
time.sleep(1)
userA.send_keys(Keys.TAB + '123456')
userA.send_keys(Keys.CONTROL,'a')
userA.send_keys(Keys.CONTROL,'c')
userA.send_keys(Keys.TAB * 2 + Keys.CONTROL,'v')
userA.send_keys(Keys.TAB * 3,'123456@qq.com')
time.sleep(3)
userA.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()