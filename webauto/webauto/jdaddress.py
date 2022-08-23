from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Firefox()
driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d7e460f9bb5a482884b7cde46c0502f1')
driver.maximize_window()
driver.find_element_by_link_text('账户登录').click()
sleep(2)
driver.find_element_by_id('loginname').send_keys('账号')
driver.find_element_by_id('nloginpwd').send_keys('密码')
# 需要手动验证，强制等待7秒
sleep(7)
# 点击昵称
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/ul[3]/li[1]/div[1]/a').click()
sleep(2)
# 切换到账户设置页面
driver.switch_to.window(driver.window_handles[1])
a = driver.find_element_by_css_selector('div.dl:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
# 在账户设置悬停
ActionChains(driver).move_to_element(a).perform()
sleep(2)
# 点击收货地址
driver.find_element_by_css_selector('.gt5 > div:nth-child(1) > a:nth-child(5) > span:nth-child(1)').click()
sleep(5)
# 点击新增收货地址
driver.find_element_by_id('edit-add-dialog').click()
# 输入收货人
driver.find_element_by_id('consigneeName').send_keys('收货人姓名')
b = driver.find_element_by_css_selector('.ui-area-text')
ActionChains(driver).move_to_element(b).perform()
sleep(2)
# 选择城市、区域、街道
driver.find_element_by_link_text('城市').click()
sleep(1)
driver.find_element_by_link_text('区域').click()
sleep(1)
driver.find_element_by_link_text('街道').click()
sleep(1)
# 输入详细地址
driver.find_element_by_id('consigneeAddress').send_keys('详细地址')
# 输入手机号
driver.find_element_by_id('consigneeMobile').send_keys('联系方式')
sleep(1)
# 点击保存地址
driver.find_element_by_link_text('保存收货地址').click()
# 定位地址列表
address = driver.find_element_by_id('addressList').text
# 断言是否添加成功
if '详细地址' in address:
    print('success')
else:
    print('fail')
driver.quit()
