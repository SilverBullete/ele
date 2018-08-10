import os
from selenium import webdriver
from time import sleep

def initWork():
    options = webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    # options.add_argument("--proxy-server=https://218.22.102.107:80")
    options.add_argument(
        'user-agent=( Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080 )')
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver,chrome_options=options)

    return driver

def login(un, pw):
    driver = initWork()
    username = un
    password = pw
    url = 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101204453&redirect_uri=https%3A%2F%2Fh5.ele.me%2Fwechat%3Feleme_redirect%3Dhttps%253A%252F%252Fh5.ele.me%252Fhongbao%252F%2523hardware_id%253D%2526is_lucky_group%253DTrue%2526lucky_number%253D8%2526track_id%253D%2526platform%253D4%2526sn%253D29fb8916ae2c1ca9%2526theme_id%253D569%2526device_id%253D%2526refer_user_id%253D1&scope=get_user_info'
    driver.get(url)
    driver.switch_to.frame("ptlogin_iframe")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[@id='switcher_plogin']").click()
    driver.find_element_by_xpath("//*[@id='u']").send_keys(username)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="p"]').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[@id='login_button']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@id='go2']").click()
    sleep(3)
    driver.refresh()
    driver.get(driver.current_url)
    cookie = driver.get_cookies()
    driver.quit()
    return cookie




# f = open('qq.txt','r')
# f2 = open('errorqq.txt', 'a')
# f1 = open('cookies.txt','a')
# qq = f.readlines()
# error = ""
# index = 0
# for i in qq:
#     index+=1
#     if index==4:
#         break
#     s = ""
#     a = i.split('----')
#     un = a[0]
#     pw = a[1]
#     try:
#         cookies = login(un,pw)
#         for j in cookies:
#             if j['name'] != 'snsInfo[101204453]':
#                 s += j['name']+'='+j['value']+';'
#             else:
#                 s += j['name']+'='+j['value']+'\n'
#         f1.write(s)
#     except:
#         error += i
#
# f2.write(error)
# f.close()
# f1.close()
# f2.close()

driver = initWork()
url = 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101204453&redirect_uri=https%3A%2F%2Fh5.ele.me%2Fwechat%3Feleme_redirect%3Dhttps%253A%252F%252Fh5.ele.me%252Fhongbao%252F%2523hardware_id%253D%2526is_lucky_group%253DTrue%2526lucky_number%253D8%2526track_id%253D%2526platform%253D4%2526sn%253D29fb8916ae2c1ca9%2526theme_id%253D569%2526device_id%253D%2526refer_user_id%253D1&scope=get_user_info'
driver.get(url)