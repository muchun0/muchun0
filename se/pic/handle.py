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
class M(BasePage.BasePage):
    def chang_page(self,page_num: int):
        self.my_find_elements((By.CLASS_NAME,"px"))[3].clear()
        self.my_find_elements((By.CLASS_NAME,"px"))[3].send_keys(page_num)
        self.my_find_elements((By.CLASS_NAME,"px"))[3].send_keys(Keys.ENTER)
        time.sleep(1)
        global page_url
        page_url = driver.current_url
        return page_url
    def get_movies(self):
        movie_elements = self.my_find_elements((By.CLASS_NAME, "xst"))
        return movie_elements

    # 获取下载链接
    def get_downloadurl(self):
            downurl = self.my_find_element((By.XPATH,
                                                        "/html/body/div[6]/div[6]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[1]/table/tbody/tr/td/div/div/ol/li"))
            pic_url = self.my_find_element((By.CLASS_NAME, "zoom"))
            movie_name = self.my_find_element((By.ID, "thread_subject"))
            view = self.my_find_element((By.CLASS_NAME, "xi1"))
            return [downurl,pic_url,movie_name,view]
def write_excel(a:int,url,pic_url,movie_name,view):
        page = {}
        page.setdefault("url", None)
        page.setdefault("pic_url", None)
        page.setdefault("movie_name", None)
        page.setdefault("view", None)
        try:
            page["url"] = url.text
            page["pic_url"] = pic_url.get_attribute("src")
            page["movie_name"] = movie_name.text
            page["view"] = view.text
            # 写入excel
            sheet.write(a, 0, page["movie_name"])
            sheet.write(a, 1, page["url"])
            sheet.write(a, 2, page["pic_url"])
            sheet.write(a, 3, page["view"])

        except:
            pass
def get_movie_url(elements:list):
    movie_url = []
    for i in elements:
        text = i.get_attribute("href")
        movie_url.append(text)
    return movie_url
def get_movie_handle(elements:list):
    for i in elements:
        try:
            i.click()
            time.sleep(0.5)
        except:
            pass
    handles = driver.window_handles
    return handles
new_M= M(driver)
a = 0
for i in range(62,545):
    url = new_M.chang_page(i)
    movies = new_M.get_movies()
    handles = get_movie_handle(movies)
    movie_url = get_movie_url(movies)
    handle = driver.current_window_handle
    handles.remove(handle)
    if len(handles) >= 30:
        for j in handles:
            driver.switch_to.window(j)
            movie_list = new_M.get_downloadurl()
            durl, pic_url, movie_name, view = movie_list
            write_excel(a,durl, pic_url, movie_name, view)
            driver.close()
            a += 1
        driver.switch_to.window(handle)
    else:
        for j in movie_url:
            driver.get(j)
            movie_list = new_M.get_downloadurl()
            durl, pic_url, movie_name, view = movie_list
            write_excel(a, durl, pic_url, movie_name, view)
            a += 1
    driver.get(url)
driver.quit()