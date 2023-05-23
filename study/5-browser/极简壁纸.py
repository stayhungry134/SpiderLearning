"""
name: 极简壁纸
create_time: 2023/5/18
author: Ethan

Description: 
"""
import time
import datetime
import re
from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox

# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


save_path = 'D:/Image/jijian/'
source_url = 'https://cdn2.zzzmh.cn/wallpaper/origin/'

# chrome_options.add_argument("--headless")  # 设置无窗口模式
# chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://bz.zzzmh.cn/index")

driver.implicitly_wait(20)
time.sleep(15)

# background-image: url("https://api.zzzmh.cn/bz/v3/getUrl/d899bcb691ce49ac921ab6b1422bca4a20"); background-position: center center;
def wrap_url(url_str):
    """处理图片的url，返回图片名"""
    regex_pattern = r"https:\/\/api.zzzmh.cn\/bz\/v3\/getUrl\/(\w*)"
    match = re.search(regex_pattern, url_str)
    if match:
        img_name = match.group(1)[:-2]
        return img_name


def save_page():
    try:
        img_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "img-box")]')
    except Exception as e:
        print("图片按钮获取失败")
        input('按回车继续')
    for img_element in img_elements:
        try:
            img_element.click()
        except Exception as e:
            print("图片按钮点击失败")
            input('按回车继续')
        driver.implicitly_wait(20)
        # 下载按钮
        try:
            download_btn = driver.find_element(By.XPATH, '//div[contains(@title, "下载")]')
            download_btn.click()
        except Exception as e:
            print("下载按钮点击失败")
            input('按回车继续')
        # 关闭按钮
        driver.implicitly_wait(20)
        try:
            close_btn = driver.find_element(By.XPATH, '//span[contains(@class, "close-span")]')
            close_btn.click()
        except Exception as e:
            print("关闭按钮点击失败")
            input('按回车继续')
        time.sleep(1)


for i in range(500):
    save_page()
    with open('jjbz.txt', 'a', encoding='utf8') as f:
        f.write(f'第{i+140}页---保存完成\n')
    # 下一页
    next_page = driver.find_element(By.XPATH, '//div[contains(@class, "vue_pagination_next")]')
    try:
        next_page.click()
    except Exception as e:
        print("下一页点击失败")
        input('按回车继续')
    time.sleep(5)
    if i % 2 == 1:
        time.sleep(600)

# driver.close()

