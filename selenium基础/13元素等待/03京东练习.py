'''
登录京东网站，添加一条收获地址
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d7e460f9bb5a482884b7cde46c0502f1')
sleep(20)
# driver.find_element_by_link_text('账户登录').click()
# sleep(2)
# driver.find_element_by_id('loginname').send_keys('13466484787')
# driver.find_element_by_id('nloginpwd').send_keys('yue_426983')
# sleep(10)
# driver.find_element_by_id('loginsubmit').click()
# 点击昵称
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/ul[3]/li[1]/div[1]/a').click()
sleep(5)
# 切换到账户设置页面
driver.switch_to.window(driver.window_handles[1])
a = driver.find_element_by_css_selector('div.dl:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
# 在账户设置悬停
ActionChains(driver).move_to_element(a).perform()
sleep(2)
driver.find_element_by_css_selector('.gt5 > div:nth-child(1) > a:nth-child(5) > span:nth-child(1)').click()
sleep(2)
# 点击新增收货地址
driver.find_element_by_id('edit-add-dialog').click()
# driver.switch_to.frame(0)
# 输入收货人
driver.find_element_by_id('consigneeName').send_keys('方方')
b = driver.find_element_by_css_selector('.ui-area-text')
ActionChains(driver).move_to_element(b).perform()
sleep(2)
# 选择城市、区域、街道
driver.find_element_by_link_text('北京').click()
sleep(2)
driver.find_element_by_link_text('丰台区').click()
sleep(2)
driver.find_element_by_link_text('马家堡街道').click()
sleep(2)
# 输入详细地址
driver.find_element_by_id('consigneeAddress').send_keys('角门西嘉园三里13号楼904')
# 输入手机号
driver.find_element_by_id('consigneeMobile').send_keys(18810237245)
sleep(1)
# 点击保存地址
driver.find_element_by_link_text('保存收货地址').click()
sleep(3)
text = driver.find_element_by_id('addressList').text
if '角门西嘉园三里13号楼904' in text:
    print('succeed')
else:
    print('failed')
driver.quit()