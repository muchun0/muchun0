import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)
# 执行js脚本，实现在浏览器中打开新标签页，访问京东网站
driver.execute_script('window.open("https://www.jd.com")')
time.sleep(2)
# driver.close() # 关闭浏览器当前窗口
driver.quit() # 关闭浏览器所有窗口