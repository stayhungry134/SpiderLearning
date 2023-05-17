"""
name: test
create_time: 2023/5/16
author: stayh

Description: Windows获取扇贝的cookies
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置无窗口模式
chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.shanbay.com/")

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
with open('cookie_win.txt', encoding='utf-8', mode='w') as f:
    f.write(str(cookie))

driver.close()