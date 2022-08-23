import re

import requests

from pic.BasePage import BasePage


class newPage(BasePage):
    def locator(self):
        movie_locator = []
        for i in range(1,101):
            movie_xpath = '/html/body/div[6]/div/div/div/div[2]/div[2]/div/ul/li[' + str(i) + ']/a/span'
            movie_locator.append(movie_xpath)
    def get_pic_data(self):
        url = self.get_current_url()
        res = requests.get(url).text
        pic_url_list = re.findall(r'https://www\..*\.jpg', res)
        pic_data = None
        for i in pic_url_list:
            try:
                pic_data = requests.get(i).content
            except:
                pass
        return pic_data
