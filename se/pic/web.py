from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
# 自拍
url = "https://www.qwewqq.xyz/forum-2-1.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(20)
detail = {}
for i in range(1,652):
    driver.find_elements_by_class_name("px")[3].clear()
    driver.find_elements_by_class_name("px")[3].send_keys(i)
    driver.find_elements_by_class_name("px")[3].send_keys(Keys.ENTER)
    time.sleep(1)
    alist = driver.find_elements_by_class_name("xst")
    new_list = []
    for j in alist:
        try:
            name = j.text
            new_list.append(name)
        except:
            pass
    time.sleep(1)
    blist = driver.find_elements_by_class_name("num")
    new_list_num = []
    for k in blist:
        try:
            num = k.text
            num = num.split("\n")[1]
            new_list_num.append(num)
        except:
            pass
    if i == 1:
        new_list_num = new_list_num[7:]
        new_list = new_list[7:]
    # print(len(new_list),len(new_list_num))
    if len(new_list_num) != len(new_list) !=30:
        print(f"第{i}页数据出错")
    for l in range(len(new_list)):
        b = {}
        try:
            b["name"] = new_list[l]
            b["view"] = new_list_num[l]
        except:
            b["view"] = "缺少数据"
        finally:
            detail[f"第{i}页第{l+1}个"] = b
with open("D:\python\se\detail.txt","w",encoding="utf-8") as file:
    file.write(str(detail))
driver.quit()