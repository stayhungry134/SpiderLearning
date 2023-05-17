"""
name: today_words_win
create_time: 2023/5/16
author: Ethan

Description:
"""
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from today_words import save_django_words


chrome_options = Options()
chrome_options.add_argument("--headless")  # 设置无窗口模式
chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.shanbay.com/")

f = open('cookie_win.txt').read()
cookies = eval(f)

csv_path = 'C:/Users/stayh/Desktop/My_Server/csvwords'
text_path = 'C:/Users/stayh/Desktop/My_Server/textwords'

time.sleep(5)

# 更换cookie
driver.delete_all_cookies()
time.sleep(5)
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

driver.implicitly_wait(20)
# 单词
word_url = driver.find_element(By.ID, 'task-1')
word_url.click()
time.sleep(5)

# 今日新词
word_book = driver.find_element(By.XPATH, '//a[@class="index_vocabularyLink__1c7FY"]')
word_book.click()
time.sleep(3)
learn_word = driver.find_element(By.XPATH, '//*[@id="1"]/div')
learn_word.click()
time.sleep(3)

file_name = datetime.date.today().isoformat()
for i in range(10):
    # 下一页
    next_page = driver.find_element(By.CSS_SELECTOR, '.index_pageContainer__2l7E1 li:last-child')
    # 单词列表
    time.sleep(3)
    word_list = driver.find_elements(By.XPATH, '//div[@class="index_wordName__1lkbV"]')
    mean_list = driver.find_elements(By.XPATH, '//div[@class="index_bottom__XLoPQ"]')
    with open(f'{csv_path}/{file_name}.csv', 'a+', newline='') as csvfile:
        for word, mean in zip(word_list, mean_list):
            word = word.text
            mean = mean.text
            csvfile.write(f'{word}, {mean}\n')
        save_django_words(word_list, mean_list)
    with open(f'{text_path}/{file_name}.txt', 'a+', newline='') as textfile:
        for word in word_list:
            word = word.text
            textfile.write(f'{word}\n')
    # 如果是最后一页
    if next_page.get_attribute('class') == 'index_nomore__2fTsZ':
        break
    # 下一页
    next_page.click()
driver.close()