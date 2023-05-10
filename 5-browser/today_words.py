"""
name: today_words.py
create_time: 2023-01-15
author: Ethan

Description: 用于获取今天的单词
"""
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def save_django_words(word_list, mean_list):
    import datetime
    import MySQLdb

    my_db = MySQLdb.connect(
        host="stayhungry134.com",
        port=3306,
        user="root",
        password="(Ethan/997813581....",
        database='django_words',
    )
    cursor = my_db.cursor()

    for word, mean in zip(word_list, mean_list):
        word = word.text
        meaning = mean.text
        today = datetime.date.today()
        review_times = [False] * 9
        # 检查记录是否存在
        cursor.execute(f"SELECT * FROM ebbinghaus_learnwords WHERE word='{word}'")
        rows = cursor.fetchall()
        if rows:
            continue
        sql = f"INSERT INTO `ebbinghaus_learnwords` (`word`, `meaning`, `init_date`, `next_date`,  `review_times`) " \
              f"VALUES " \
              f"('{word}', '{meaning}', '{today}', '{today}', '{review_times}');"
        cursor.execute(sql)
    my_db.commit()


csv_path = '/opt/study/csvwords'
text_path = '/opt/study/textwords'
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

WINDOW_SIZE = "1920, 1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.shanbay.com/')

f = open('cookie.txt').read()
cookies = eval(f)

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
