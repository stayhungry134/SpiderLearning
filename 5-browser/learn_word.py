from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('../0-file/chromedriver.exe')
driver.get('https://www.shanbay.com/')

cookies = [
    {'domain': '.shanbay.com', 'expiry': 1668048903, 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'secure': False, 'value': '04370f0081087901a904e35e4db4daa4'},
    {'domain': '.shanbay.com', 'expiry': 1637377255, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': False, 'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjMyMjc0ODIwLCJleHAiOjE2MzczNzcyNTcsImV4cF92MiI6MTYzNzM3NzI1NywiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJXZWNoYXRfYTUxNjUwYTNmZmNjZGQwZCIsImlzX3N0YWZmIjowLCJzZXNzaW9uX2lkIjoiYmE3MDFmZmE0MWQxMTFlY2I5NjMxMjhkZTA0ZGEzYjUifQ.6BGCMGmxcBRle___Ju6hmxCSfVuJX47l96ZjJZYDTeY'},
    {'domain': '.shanbay.com', 'expiry': 7943712956, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%22zprmko%22%2C%22first_id%22%3A%2217d07c5c6dd3c5-006c531bb9bf9a-57b1a33-2073600-17d07c5c6df733%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22open.weixin.qq.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22%24device_id%22%3A%2217d07c5c6dd3c5-006c531bb9bf9a-57b1a33-2073600-17d07c5c6df733%22%7D'},
    {'domain': '.shanbay.com', 'expiry': 1636559999, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'},
    {'domain': '.shanbay.com', 'expiry': 1636513504, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},
    {'domain': '.shanbay.com', 'expiry': 1699584930, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.981172990.1636512904'}
]



# 获取 cookies, 打开之后登录，然后等待打印
# time.sleep(20)
# cookie = driver.get_cookies()
# print(cookie)



time.sleep(5)

# 删除所有cookie
driver.delete_all_cookies()
time.sleep(5)
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

driver.implicitly_wait(20)
word_url = driver.find_element_by_class_name('index_vocabularyLink__1c7FY')
word_url.click()
time.sleep(5)

# 未学单词
now_word = driver.find_element_by_id('4')
now_word.click()
time.sleep(5)

# //div[@class="index_right__3EC1l"]/div[2]/div/div[2]
while True:
    # 下一页
    next_page = driver.find_element_by_css_selector('.index_pageContainer__2l7E1 li:last-child')
    # 单词列表
    time.sleep(10)
    word_list = driver.find_elements_by_xpath('//div[@class="index_word__3waO0"]')
    with open('CET-6.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        for word in word_list:
            word_meaning = word.text.split('\n')
            writer.writerow(word_meaning)
    # 如果下一页是最后一页
    if next_page.get_attribute('class') == 'index_nomore__2fTsZ':
        break
    # 下一页
    next_page.click()
