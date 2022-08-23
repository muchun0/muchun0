from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('https://www.jd.com')
js = 'window.scrollTo(0,3000)' # 纵向拖动滚动条的js脚本
driver.execute_script(js) # selenium执行js脚本的方法
sleep(2)
driver.close()