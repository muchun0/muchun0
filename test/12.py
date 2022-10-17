from selenium import webdriver

url = 'https://cld675.com/thread.php?fid=6'
driver = webdriver.Firefox()
driver.get(url)
for i in range(8,100):
    movieDetailsXpath={}
    nameXpath = '/html/body/div[3]/div[3]/table/tbody[2]/tr[' + str(i) + ']/td[2]/h3/a'

    isHotXpath = '/html/body/div[3]/div[3]/table/tbody[2]/tr[' + str(i) + ']/td[1]/a/span'
                # /html/body/div[3]/div[3]/table/tbody[2]/tr[8]/td[1]/a/span
    countNumberXpath = '/html/body/div[3]/div[3]/table/tbody[2]/tr[' + str(i) + ']/td[4]'

    movieDetails = {}

    name = driver.find_element('xpath', nameXpath).is_enabled()
    print(name)
    isHot = driver.find_element('xpath', isHotXpath).is_enabled()
    print(isHot)
    countNumber = driver.find_element('xpath', countNumberXpath).text
    print(countNumber)
    movieUrl = driver.find_element('xpath',
                                   nameXpath).get_attribute(
        'href')
    print(movieUrl)



driver.quit()
