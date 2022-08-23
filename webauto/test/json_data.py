import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

file_path = "D:\python\webauto\\"
driver = webdriver.Firefox()
driver.get("https://www.bejson.com/explore/index_new/")
driver.maximize_window()
driver.implicitly_wait(20)
for i in os.listdir(file_path):
    if os.path.splitext(i)[1] == ".txt":
        i = file_path+i
        print(i)
        with open(i,"r",encoding="utf-8") as file:
            data = file.read()
            driver.find_element_by_xpath('//*[@id="eT"]').send_keys(data)
            ActionChains(driver).double_click(driver.find_element_by_xpath('//*[@id="eT"]')).perform()
            new_data = driver.find_element_by_xpath('//*[@id="eT"]').text
            with open(i, "w", encoding="utf-8") as f:
                f.write(new_data)
            break