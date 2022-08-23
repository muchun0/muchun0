'''对selenium进行二次封装'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,driver):
        self.driver = driver
    # 定位元素
    def my_find_element(self,loctor,timeout=20,poll_frequency=0.5):
        try:
            element = WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(loctor))
        except:
            element = None
            print(f'{loctor}元素未找到')
        finally:
            return element
    # 定义输入操作
    def my_send_keys(self,loctor,text,timeout=20,poll_frequency=0.5):
        self.my_find_element(loctor,timeout,poll_frequency).send_keys(text)
    # 定义点击操作
    def my_click(self,loctor,timeout=20,poll_frequency=0.5):
        self.my_find_element(loctor,timeout,poll_frequency).click()
    # 获取元素文本
    def my_text(self,loctor,timeout=20,poll_frequency=0.5):
        return self.my_find_element(loctor,timeout,poll_frequency).text
if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    sleep(3)
    BasePage(driver).my_find_element((By.ID, 'kw'))
    BasePage(driver).my_send_keys((By.ID,'kw'),'hello')
    sleep(3)
    BasePage(driver).my_click((By.ID,"su"))
    sleep(5)
    print(BasePage(driver).my_text((By.ID, "su")))
    driver.quit()