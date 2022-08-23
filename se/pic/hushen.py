import os
import datetime
import time
import re
from selenium import webdriver
import unittest
import ddt
from selenium.webdriver import ActionChains
import requests
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basepage.tool import writeData

if not os.path.exists(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today())):
    os.mkdir(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()))

# for i in range(1,101):
#     driver = webdriver.Firefox()
#     driver.get('https://warwetretyry.com/portal.php')
#     driver.implicitly_wait(20)
#     driver.minimize_window()
#     xpath = '/html/body/div[6]/div/div/div/div[2]/div[2]/div/ul/li[' + str(i) + ']/a/span'
#     # 挨个点击链接
#     movie_name = driver.find_element('xpath',xpath).text
#     driver.find_element('xpath',xpath).click()
#     handles = driver.window_handles
#     driver.switch_to.window(handles[1])
#     # 获取图片url
#     time.sleep(3)
#     url = driver.current_url
#     res = requests.get(url).text
#     pic_url_list = re.findall(r'https://www\..*\.jpg', res)
#     # movie_detail = re.findall(r'[\u4e00-\u9fa5]+', res)
#     # print(movie_detail)
#     for j in pic_url_list:
#         try:
#             pic_data = requests.get(j).content
#             time.sleep(3)
#             # 创建影片名文件夹
#             if not os.path.exists(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()) + f'\\{movie_name}'):
#                 os.mkdir(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()) + f'\\{movie_name}')
#             pic_os_path = r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()) + f'\\{movie_name}' + f'\\{movie_name}.jpg'
#             with open(pic_os_path,'wb') as file:
#                 file.write(pic_data)
#             # ActionChains(driver).move_to_element(driver.find_element('xpath',
#             #                                                          '/html/body/div[6]/div[6]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[1]/div[2]/div[2]/span[2]/img')).perform()
#             # driver.find_element('link text', '阅读模式').click()
#             # data = driver.find_element('class name', 't_f').text
#             pic_text = r'C:\Users\11203\Desktop\pic\\' + str(
#                 datetime.date.today()) + f'\\{movie_name}' + f'\\{movie_name}.txt'
#             print(driver.find_element('class name', 't_f').text)
#             with open(pic_text, 'w', encoding='utf-8') as f:
#                 f.write(driver.find_element('class name', 't_f').text)
#         except:
#             pass
#         finally:
#             driver.quit()

xpath = []
for i in range(1, 31):
    '/html/body/div[6]/div[6]/div/div/div[4]/div[2]/form/ul/li[1]/div[2]/cite'
    xpath.append('/html/body/div[6]/div/div/div/div[2]/div[2]/div/ul/li[' + str(i) + ']/a/span')

@ddt.ddt()
class TestGetMovie(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('https://warwetretyry.com/forum-41-1.html')
        # self.driver.implicitly_wait(20)
        self.driver.minimize_window()
        self.movie_name=None
    def tearDown(self) -> None:
        writeData(self.movie_name,self.url,self.movie_data)
        self.driver.quit()
    @ddt.data(*xpath)
    def testCase(self,data):
        # print(data)
        # self.movie_name = self.driver.find_element('xpath', data).text
        WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(('xpath', data))).click()
        self.movie_name = WebDriverWait(self.driver,timeout=20).until(EC.presence_of_element_located(('xpath', data))).text
        # print(self.movie_name)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(3)
        res = requests.get(self.driver.current_url).text
        self.url = re.findall(r'https://www\..*\.jpg', res) #可能会超时
        self.movie_data = WebDriverWait(self.driver,timeout=20).until(EC.presence_of_element_located(('class name', 't_f'))).text

        # print(self.movie_name)
        # print(self.url)
        # print(self.movie_data)
if __name__ == '__main__':
    unittest.main()