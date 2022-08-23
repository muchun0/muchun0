from selenium.webdriver.common.keys import Keys
import xlwt
import time
from selenium import webdriver
from pic import BasePage
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.qwewqq.xyz/forum-103-1.html")
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 2', cell_overwrite_ok=True)
sheet1 = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
class M(BasePage.BasePage):
    def chang_page(self,page_num: int):
        self.my_find_elements((By.CLASS_NAME,"px"))[3].clear()
        self.my_find_elements((By.CLASS_NAME,"px"))[3].send_keys(page_num)
        self.my_find_elements((By.CLASS_NAME,"px"))[3].send_keys(Keys.ENTER)
        time.sleep(0.5)
        global page_url
        page_url = driver.current_url
        return page_url
    def get_url(self):
        movie_url = []
        movie_elements = self.my_find_elements((By.CLASS_NAME, "xst"))
        for i in movie_elements:
            text = i.get_attribute("href")
            movie_url.append(text)
        return movie_url
    # 获取下载链接
    def get_downloadurl(self):
            downurl = self.my_find_element((By.XPATH,
                                                        "/html/body/div[6]/div[6]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/table/tbody/tr/td/div/div/ol/li"))
            pic_url = self.my_find_element((By.CLASS_NAME, "zoom"))
            movie_name = self.my_find_element((By.ID, "thread_subject"))
            view = self.my_find_element((By.CLASS_NAME, "xi1"))
            return [downurl,pic_url,movie_name,view]
    def write_excel(self,a:int,elements:list):

            page = {}
            page.setdefault("url", None)
            page.setdefault("pic_url", None)
            page.setdefault("movie_name", None)
            page.setdefault("view", None)
            try:
                page["url"] = elements[0].text
                page["pic_url"] = elements[1].get_attribute("src")
                page["movie_name"] = elements[2].text
                page["view"] = elements[3].text
                # 写入excel
                sheet.write(a, 0, page["movie_name"])
                sheet.write(a, 1, page["url"])
                sheet.write(a, 2, page["pic_url"])
                sheet.write(a, 3, page["view"])
                wbk.save("D:\python\se\\中文字幕.xls")
            except:
                pass
new_M= M(driver)
a = 0
for i in range(2,545):
    url = new_M.chang_page(i)
    movie_url = new_M.get_url()
    for j in movie_url:
        driver.get(j)
        elements = new_M.get_downloadurl()
        new_M.write_excel(a,elements)
        a += 1
    driver.get(url)
driver.quit()