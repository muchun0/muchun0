"""封装注册页面"""
from selenium.webdriver.common.by import By
from time import sleep
from common.BasePage import BasePage
class RegistRage(BasePage):
    # 表现层
    username = (By.ID,'username')
    email = (By.ID,'email')
    password1 = (By.ID,'password1')
    conform_password = (By.ID,'conform_password')
    phone = (By.NAME,'extend_field5')
    regist = (By.CLASS_NAME,'us_Submit_reg')
    login_result = (By.CSS_SELECTOR, "#ECS_MEMBERZONE > a:nth-child(1)")  # 登录的断言元素
    # 操作层
    # 输入用户名
    def input_username(self,text):
        self.my_send_keys(self.username,text)
    # 输入邮箱
    def input_email(self,text):
        self.my_send_keys(self.email,text)
    # 输入密码
    def input_password(self,text):
        self.my_send_keys(self.password1,text)
    # 确认密码
    def conform_password1(self,text):
        self.my_send_keys(self.conform_password,text)
    # 输入手机号
    def input_phone(self,text):
        self.my_send_keys(self.phone,text)
    # 点击立即注册
    def click_regist(self):
        self.my_click(self.regist)
    def login_result_text(self):
        '''
        获取登录后的断言元素的文本
        :return: 元素文本内容
        '''
        return self.get_text(self.login_result)
    # 业务层
    def register(self,username,email,password,conform_password,phone):
        self.input_username(username)
        sleep(2)
        self.input_email(email)
        sleep(2)
        self.input_password(password)
        sleep(2)
        self.conform_password1(conform_password)
        sleep(2)
        self.input_phone(phone)
        sleep(3)
        self.click_regist()
        sleep(5)
        return self.login_result_text()
if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get('http://localhost:8080/ecshop/eashop/upload/user.php?act=register')
    driver.maximize_window()
    print(RegistRage(driver).register('fff', '1123174@qq.com', 123456, 123456, 13455756666))
    sleep(5)
    driver.close()