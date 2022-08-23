'''封装登录页面'''
from selenium.webdriver.common.by import By
from common.BasePage import BasePage
from time import sleep
class LoginPage(BasePage):
    # 1、表现层：页面元素定位
    username_loc = (By.NAME,"username") # 用户名输入框
    password_loc = (By.NAME,"password") # 密码输入框
    login_loc = (By.CLASS_NAME,"us_Submit") # 登录按钮
    login_result = (By.CSS_SELECTOR,"#ECS_MEMBERZONE > a:nth-child(1)") # 登录的断言元素
    # 2、操作层：页面元素操作
    def input_username(self,text):
        '''
        输入用户名
        :param text: 用户名
        :return:
        '''
        self.my_send_keys(self.username_loc,text)
    def input_password(self,text):
        '''
        输入密码
        :param text: 密码
        :return:
        '''
        self.my_send_keys(self.password_loc,text)
    def login_click(self):
        '''
        点击登录按钮
        :return:
        '''
        self.my_click(self.login_loc)
    def login_result_text(self):
        '''
        获取登录后的断言元素的文本
        :return: 元素文本内容
        '''
        return self.get_text(self.login_result)
    # 3、业务层：元素操作完成的功能
    def login(self,username,password):
        '''
        登录业务
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        sleep(2)
        self.input_username(username)
        sleep(2)
        self.input_password(password)
        sleep(2)
        self.login_click()
        sleep(5)
        return self.login_result_text()
if __name__ == '__main__':
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://localhost:8080/ecshop/eashop/upload/user.php')
    print(LoginPage(driver).login('muchun', 'yue_426983'))
    sleep(3)
    driver.quit()