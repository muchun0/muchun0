"""
需求：
打开163邮箱（https://email.163.com/）,发送一封邮件，带附件
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://email.163.com/')
driver.implicitly_wait(20)
driver.switch_to.frame(1)
sleep(1)
# 输入账号
driver.find_element_by_tag_name('input').send_keys('zhangyue_8972021')
sleep(2)
# 输入密码
driver.find_element_by_name('password').send_keys('zhangyue897')
sleep(2)
# 点击登录
driver.find_element_by_id('dologin').click()
# sleep(10)
driver.switch_to.default_content()
# 点击写信
driver.find_elements_by_class_name('oz0')[1].click()
# 输入收件人
driver.find_element_by_xpath('//*[@aria-label="收件人地址输入框，请输入邮件地址，多人时地址请以分号隔开"]').send_keys('FangFang20190607@163.com')
# 输入主题
driver.find_element_by_xpath('//*[@maxlength="256"]').send_keys('hello')
# 添加附件
driver.find_element_by_xpath('//*[@multiple=""]').send_keys(r'C:\Users\Administrator\Desktop\test.txt')
sleep(2)
# 添加正文
driver.switch_to.frame(driver.find_element_by_class_name('APP-editor-iframe'))
sleep(2)
driver.find_element_by_xpath('/html/body').send_keys('hello')
# 点击发送按钮
driver.switch_to.default_content()
driver.find_elements_by_class_name('nui-btn-text')[2].click()
sleep(5)
# 点击首页
driver.find_element_by_xpath('//*[@title="首页"]').click()
sleep(3)
# 点击已发送
driver.find_element_by_xpath('//*[@title="已发送"]').click()
sleep(2)
# 验证是否发送成功
text = driver.find_element_by_xpath('//b[@aria-label="发送成功"]').get_attribute('title')
if text == '发送成功':
    print('OK')
else:
    print('NO')
# 关闭浏览器
driver.quit()

