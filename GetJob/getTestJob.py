from selenium import webdriver

driver = webdriver.Firefox()
url = 'https://www.zhipin.com/web/geek/job?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&city=101010100'
driver.get(url)
driver.switch_to.alert.dismiss()
joblist = driver.find_elements("class name",'job-card-left')
print(len(joblist))
for i in joblist:
    print(i.text)
driver.quit()