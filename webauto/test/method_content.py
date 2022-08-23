from selenium import webdriver
import time
driver = webdriver.Firefox()
# 尝试获取网页文本
driver.get("http://doc.redisfans.com/key/del.html")
driver.maximize_window()
driver.implicitly_wait(10)
text = driver.find_element_by_css_selector(".highlight-python > pre:nth-child(1)").text
print(text)
driver.quit()
