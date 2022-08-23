from selenium.webdriver.common.by import By
from common.BasePage import BasePage
from time import sleep

class Page():
    def __init__(self,driver):
        self.driver = driver
    send = (By.ID, 'kw')
    baiduyixia = (By.ID,"su")
    # 输入内容
    def test_send(self,text):
        BasePage(self.driver).my_send_keys(self.send,text)
    # 点击百度一下
    def test_click(self):
        BasePage(self.driver).my_click(self.baiduyixia)
    # 3、功能层
    def test_operation(self,text):
        self.test_send(text)
        sleep(2)
        self.test_click()
        sleep(2)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    Page(driver).test_operation('hello')
    sleep(3)
    driver.quit()