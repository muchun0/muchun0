from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///D:/selenium%E5%9F%BA%E7%A1%80/%E7%BB%83%E4%B9%A0%E9%A1%B5%E9%9D%A2/注册A.html')
driver.find_element_by_link_text('访问 新浪 网站').click()
sleep(2)
print(driver.window_handles) # 返回所有窗口句柄（窗口id），列表形式
print(driver.current_window_handle) # 返回当前窗口句柄
sleep(2)
driver.switch_to.window(driver.window_handles[1]) # 切换窗口，传入窗口的句柄
sleep(2)
driver.find_element_by_link_text('军事').click()
sleep(3)
driver.quit()