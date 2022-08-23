from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.jd.com')
a = 100
while 1:
    try:
        driver.find_element_by_link_text('华为mate20').click()
        break
    except:
        driver.execute_script(f'window.scrollTo(0,{a})')
        a += 6000
        sleep(2)
sleep(4)
driver.quit()
