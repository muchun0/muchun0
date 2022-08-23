import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/6_ul下拉菜单.html')
a = driver.find_element_by_css_selector('#nav > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)')
ActionChains(driver).move_to_element(a).perform()
# time.sleep(2)
# driver.find_element_by_link_text('Python').click()
# time.sleep(3)
# driver.quit()
a.click()
time.sleep(2)
a.send_keys(Keys.TAB * 3 + Keys.ENTER)
time.sleep(3)
driver.quit()