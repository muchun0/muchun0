from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
driver = webdriver.Firefox()
driver.get('https://www.zhipin.com/?ka=header-home')
sleep(3)
# 定位登录按钮
driver.find_element_by_link_text('登录').click()
# 输入手机号
# 13051770550/18810237245
driver.find_element_by_css_selector('div.sign-form:n'
                                    'th-child(1) > div:nth-child(2) >'
                                    ' div:nth-child(1) > form:nth-child(2) > d'
                                    'iv:nth-child(4) > span:nth-child(2) > input:nth-child(2)').send_keys('13051770550')
# 输入密码/FZT19950321
driver.find_element_by_css_selector('.ipt-pwd').send_keys('poptest2019')
sleep(12)
# 点击登录按钮
driver.find_element_by_css_selector('div.sign-form:nth-child(1) '
                                    '> div:nth-child(2) > div:nth-'
                                    'child(1) > form:nth-child(2) > div:nth-child(12) > button:nth-child(1)').click()
sleep(10)
a = driver.find_element_by_css_selector('.nav-figure > a:nth-child(1) > span:nth-child(1)')
# 鼠标悬停到用户名上
ActionChains(driver).move_to_element(a).perform()
sleep(3)
# 点击账户设置
driver.find_element_by_css_selector('.dropdown > a:nth-child(2)').click()
sleep(3)
# 点击常用语
driver.find_element_by_css_selector('li.nav-list:nth-child(5)').click()
sleep(3)
# 点击添加常用语
driver.find_element_by_link_text('添加常用语').click()
sleep(3)
# 输入您好
driver.find_element_by_css_selector('.input').send_keys('您好')
sleep(3)
driver.find_element_by_link_text('保存').click()
sleep(3)
if '您好' in driver.find_element_by_css_selector('.phrases-content').text:
    driver.quit()
