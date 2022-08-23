'''对selenium进行二次封装'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def my_find_element(self,locator,timeout=20,poll_frequency=0.5):
        '''
        元素定位
        :param locator:元素定位器，元组形式
        :param timeout: 超时时间，单位秒
        :param poll_frequency: 轮询时间，单位秒
        :return: 元素对象
        '''
        try:
            element = WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(locator))
        except:
            print(f'{locator}元素未找到')
            element = None
        finally:
            return element
    def my_send_keys(self,locator,text,timeout=20,poll_frequency=0.5):
        '''
        输入
        :param locator: 元素定位器，元组形式
        :param text: 输入文本
        :param timeout: 超时时间，单位秒
        :param poll_frequency: 轮询时间，单位秒
        :return: None
        '''
        self.my_find_element(locator,timeout,poll_frequency).send_keys(text)

    def my_click(self,locator,timeout=20,poll_frequency=0.5):
        '''
        点击
        :param locator: 元素定位器，元组形式
        :param timeout: 超时时间，单位秒
        :param poll_frequency: 轮询时间，单位秒
        :return: None
        '''
        self.my_find_element(locator, timeout, poll_frequency).click()
    def get_text(self,locator,timeout=20,poll_frequency=0.5):
        '''
        获取元素文本
        :param locator: 元素定位器，元组形式
        :param timeout: 超时时间，单位秒
        :param poll_frequency: 轮询时间，单位秒
        :return: 文本内容
        '''
        return self.my_find_element(locator, timeout, poll_frequency).text
if __name__ == '__main__':
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://localhost:8080/ecshop/eashop/upload/user.php')
    sleep(2)
    BasePage(driver).my_send_keys((By.NAME,"username"),"muchun")
    sleep(2)
    BasePage(driver).my_send_keys((By.NAME,"password"),"yue_426983")
    sleep(2)
    BasePage(driver).my_click((By.CLASS_NAME,"us_Submit"))
    sleep(3)
    driver.quit()



