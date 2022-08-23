from selenium import webdriver
from pic import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import xlwt


wbk = xlwt.Workbook()
sheet = wbk.add_sheet("sheet 1")
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.qwewqq.xyz/forum.php?mod=forumdisplay&fid=41&orderby=heats&filter=dateline&dateline=604800")
class hot(BasePage.BasePage):
    def chang_page(self,page_num: int):
        self.my_find_elements((By.CLASS_NAME,"px"))[3].clear()
        self.my_find_elements((By.CLASS_NAME,"px"))[3].send_keys(page_num)
        self.my_find_elements((By.CLASS_NAME,"px"))[3].send_keys(Keys.ENTER)
        time.sleep(1)
    def get_name(self):
        a = []
        movie_front = "/html/body/div[6]/div[6]/div/div/div[4]/div[2]/form/ul/li["
        movie_last = "]/h3/a"
        for j in range(1,30):
            try:
               moviea_name = driver.find_element_by_xpath(movie_front+str(j)+movie_last)
               a.append(moviea_name.text)
            except:
                pass
        return a
    def get_pic(self):
        b = []
        picture_front = "/html/body/div[6]/div[6]/div/div/div[4]/div[2]/form/ul/li["
        picture_last = "]/div[1]/a/img"
        for k in range(1, 30):
            try:
                l = driver.find_element_by_xpath(picture_front + str(k) + picture_last).get_attribute("src")
                b.append(l)
            except:
                pass
        return b

a = hot(driver)
count = 0
page_num = int(driver.find_element_by_xpath("/html/body/div[6]/div[6]/div/div/div[3]/span[1]/div/label/span").text.replace('/ ','').replace(" 页",""))
for i in range(1,page_num+1):
    try:
        a.chang_page(i)
        name = a.get_name()
        picture = a.get_pic()
        for j in range(len(name)):
            data_name = a.get_name()[j]
            date_picture = a.get_pic()[j]
            sheet.write(count,0,a.get_name()[j])
            sheet.write(count,1,a.get_pic()[j])
            count += 1
    except:
        pass

driver.quit()
