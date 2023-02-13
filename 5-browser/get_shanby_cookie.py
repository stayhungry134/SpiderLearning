"""
name: get_shanby_cookies.py
create_time: 2023-01-31
author: Ethan

Description: 获取扇贝单词的 cookie
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

WINDOW_SIZE = "1920, 1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.shanbay.com/')

# 登录
login = driver.find_element(By.CLASS_NAME, 'sign')
time.sleep(10)
login.click()
time.sleep(5)
wechat = driver.find_element(By.XPATH, '//img[@alt="微信登录"]')
time.sleep(5)
wechat.click()
time.sleep(10)
qr_code = driver.find_element(By.CLASS_NAME, 'web_qrcode_img')
wechat_src = qr_code.get_attribute('src')
print(wechat_src)
time.sleep(60)
cookie = driver.get_cookies()
print(cookie)
with open('cookie.txt', encoding='utf-8', mode='w') as f:
    f.write(str(cookie))

driver.close()

