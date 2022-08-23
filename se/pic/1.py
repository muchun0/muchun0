import os
import datetime
import time

from selenium import webdriver
import unittest
import ddt
# from selenium.webdriver import ActionChains
# driver = webdriver.Firefox()
# driver.get('https://warwetretyry.com/thread-865589-1-1.html')
# driver.implicitly_wait(20)
# ActionChains(driver).move_to_element(driver.find_element('xpath','/html/body/div[6]/div[6]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/span[2]/img')).perform()
# driver.find_element('link text','阅读模式').click()
# import re
# data = re.match('www.*.jpg','www.baidu.com.jpg')
# print(type(data))
import re
# print(re.findall(r'www\..*\.jpg', 'www.baidu.com/a.jpg'))
#匹配中文
# import re
# data = re.findall(r'[\u4e00-\u9fa5]+', '你好，我是中国人')
# print(data)
xpath = []
for i in range(1, 101):
    xpath.append('/html/body/div[6]/div/div/div/div[2]/div[2]/div/ul/li[' + str(i) + ']/a/span')
@ddt.ddt()
class TestCase(unittest.TestCase):

    @ddt.data(*xpath)
    def test_01(self,data):
        print(data)
if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
