from selenium import webdriver
import time

# 初始化
def restart():
    driver = webdriver.Firefox()
    # 在线视频-国产
    url = "https://www.qwewqq.xyz/forum.php?mod=forumdisplay&fid=41&orderby=heats&filter=dateline&dateline=604800&orderby=heats"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver
# 获取查看次数
def get_pv(driver):
    lv_list = driver.find_elements_by_class_name("y")
    alist = []
    pv = []
    for i in lv_list:
        alist.append(i.text)
    for i in alist:
        try:
            num = int(i.replace("查看: ", ""))
            pv.append(num)
        except:
            continue
    return pv
# 操作查看次数大于45000的文件
def compare(driver,index,num):
    if num >= 45000:
        css = "#waterfall > li:nth-child(" + str(index) + ")> h3:nth-child(2) > a:nth-child(1)"
        name = driver.find_element_by_css_selector(css).text
                                                #横向 waterfall > li:nth-child(2) > h3:nth-child(2) > a:nth-child(1)
                                                #纵向 waterfall > li:nth-child(6) > h3:nth-child(2) > a:nth-child(1)
        driver.find_element_by_id("scbar_txt").send_keys(name)
        driver.find_element_by_id("scbar_btn").click()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        result = driver.find_elements_by_link_text(name)
        for i in result:
            i.click()
        # 关闭搜索结果页
        driver.close()
        handles = driver.window_handles
        # 遍历当前打开页面
        for i in range(len(handles)):
            driver.switch_to.window(handles[i])
            try:
                driver.find_element_by_css_selector(".blockcode > em:nth-child(2)")
                filename = name + ".png"
                driver.save_screenshot(filename)
            except:
                driver.close()
        driver.quit()
        restart()

if __name__ == '__main__':
    driver = restart()
    adict = get_pv(driver)
    print(adict)
    for i in adict:
        for j in range(len(adict)):
            compare(driver,j+1,i)
    time.sleep(2)
    driver.quit()