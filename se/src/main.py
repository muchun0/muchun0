import os
import datetime
import time
import re

import requests
from selenium import webdriver
import unittest
import ddt
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basepage.tool import writeData

if not os.path.exists(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today())):
    os.mkdir(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()))

xpath = []
for i in range(1, 101):
    xpath.append('/html/body/div[6]/div/div/div/div[2]/div[2]/div/ul/li[' + str(i) + ']/a/span')

@ddt.ddt()
class TestGetMovie(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('https://warwetretyry.com/portal.php')
        self.driver.minimize_window()
        self.movie_name=None
    def tearDown(self) -> None:
        writeData(self.movie_name,self.url,self.movie_data)
        self.driver.quit()
    @ddt.data(*xpath)
    def testCase(self,data):
        WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(('xpath', data))).click()
        self.movie_name = WebDriverWait(self.driver,timeout=20).until(EC.presence_of_element_located(('xpath', data))).text
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(3)
        res = requests.get(self.driver.current_url).text
        self.url = re.findall(r'https://www\..*\.jpg', res) #可能会超时
        self.movie_data = WebDriverWait(self.driver,timeout=20).until(EC.presence_of_element_located(('class name', 't_f'))).text

if __name__ == '__main__':
    unittest.main()