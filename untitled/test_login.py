import pytest

from selenium import webdriver
class Test_login():
    #用例执行前置条件，每个用例执行前都会执行一次
    def setup(self):
        #打开浏览器并跳转到登录页面
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(20)
    #每个用例执行完毕之后都会执行
    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element('link text',"登录").click()
        self.driver.switch_to_alert()
        self.driver.find_element('name',"username").send_keys(13466484787)
        self.driver.find_element('name',"password").send_keys('yue_426983')
        self.driver.find_element('id',"TANGRAM__PSP_11__submit").click()
if __name__ == '__main__':
    pytest.main(['-sv','test_login.py'])

