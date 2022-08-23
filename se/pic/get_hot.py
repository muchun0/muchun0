from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlwt

def get_xpath(num):
    x_front = "/html/body/div[6]/div[6]/div/div/div[4]/div[2]/form/table/tbody["
    x_last = "]/tr/th/a[2]"
    xpath = x_front + str(num) + x_last
    xpath_hot = x_front+str(num) +"]/tr/th/img[2]"
    return [xpath,xpath_hot]
driver = webdriver.Firefox()
url = "https://www.qwewqq.xyz/forum-103-1.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
for i in range(1, 534):
    driver.find_elements_by_class_name("px")[3].clear()
    driver.find_elements_by_class_name("px")[3].send_keys(i)
    driver.find_elements_by_class_name("px")[3].send_keys(Keys.ENTER)
    hot_list = {}
    for j in range(1,40):
        xpath_list = get_xpath(j)
        print(xpath_list)
        try:
            hot = driver.find_element_by_xpath(xpath_list[1]).get_attribute("title")
            hot_num = hot.split(": ")[1]
            if hot_num >= 5:
                name = driver.find_element_by_xpath(xpath_list[0]).text
                hot_list[name] = hot_num
                sheet.write(i, j, name)
                sheet.write(i, j+1, hot_num)
        except:
            continue
driver.quit()
wbk.save("D:\python\se\\test.xls")


