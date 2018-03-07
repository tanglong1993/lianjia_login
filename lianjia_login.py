import requests
from selenium import webdriver
import time
import re

url = 'https://wh.lianjia.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

browser = webdriver.Firefox()
browser.get(url=url)
# browser.maximize_window() 最大化界面

browser.find_element_by_class_name('reg').click()
browser.find_element_by_class_name('tologin').click()
browser.find_element_by_xpath('//*[@id="con_login_user"]/form/ul/li[1]/input').send_keys('15711026959')
browser.find_element_by_xpath('//*[@id="con_login_user"]/form/ul/li[2]/input').send_keys('tanglong1214')
browser.find_element_by_class_name('login-user-btn').click()
captcha = input('请输入验证码：')
browser.find_element_by_xpath('//*[@id="con_login_user"]/form/ul/li[3]/input').send_keys(captcha)
browser.find_element_by_class_name('login-user-btn').click()
time.sleep(5)
print('browser.get_cookies:::',browser.get_cookies())
#重点 cookie的转换
cookie =[item["name"] + ":" + item["value"] for item in browser.get_cookies()]
print('coookie:',cookie)
cook_map = {}
for item in cookie :
    str = item.split(':')
    cook_map[str[0]] = str[1]
    print(cook_map)

cookies = requests.utils.cookiejar_from_dict(cook_map, cookiejar=None, overwrite=True)
print('最终的cookie：',cookies)

sess = requests.Session()

sess.cookies = cookies

r = sess.get(url='https://user.lianjia.com/')
print(r.text)








