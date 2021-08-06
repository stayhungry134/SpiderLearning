from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('D:/Installation package/Chrome/chromedriver.exe')
driver.get('https://www.shanbay.com/')

cookies = [
    {'domain': '.shanbay.com', 'expiry': 1618560430, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},
    {'domain': '.shanbay.com', 'expiry': 1681631830, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.976522256.1618559831'},
    {'domain': '.shanbay.com', 'expiry': 1650095829, 'httpOnly': False, 'name': 'csrftoken', 'path': '/', 'secure': False, 'value': '1vF3maVbWHYDUufoek4LNHGYh8j28EaN'},
    {'domain': '.shanbay.com', 'expiry': 1619424137, 'httpOnly': True, 'name': 'auth_token', 'path': '/', 'secure': False, 'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjMyMjc0ODIwLCJleHAiOjE2MTk0MjQxMzcsImV4cF92MiI6MTYxOTQyNDEzNywiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJXZWNoYXRfYTUxNjUwYTNmZmNjZGQwZCIsImlzX3N0YWZmIjowLCJzZXNzaW9uX2lkIjoiNWQxZjBkMTY5ZTg5MTFlYmFjYTgxMjVhMmVjZTQ4ODkifQ.vHayhkxQOFYtwlGPWauknr_vCMUcT5jK2OsJaZLUaUs'},
    {'domain': '.shanbay.com', 'expiry': 7925759860, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%22zprmko%22%2C%22%24device_id%22%3A%22178d9af06509e5-0bc289d3fe04c8-c3f3568-2073600-178d9af065187f%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer_host%22%3A%22open.weixin.qq.com%22%7D%2C%22first_id%22%3A%22178d9af06509e5-0bc289d3fe04c8-c3f3568-2073600-178d9af065187f%22%7D'},
    {'domain': '.shanbay.com', 'expiry': 1618588799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user', 'path': '/', 'secure': False, 'value': '1'}]

time.sleep(3)

# 删除所有cookie
driver.delete_all_cookies()
time.sleep(1)
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

driver.implicitly_wait(10)
word_url = driver.find_element_by_class_name('index_vocabularyLink__1c7FY')
word_url.click()
time.sleep(3)

# 在学单词
now_word = driver.find_element_by_id('3')
now_word.click()
time.sleep(3)

# //div[@class="index_right__3EC1l"]/div[2]/div/div[2]
while True:
    # 下一页
    next_page = driver.find_element_by_css_selector('.index_pageContainer__2l7E1 li:last-child')
    # 单词列表
    time.sleep(1)
    driver.implicitly_wait(10)
    word_list = driver.find_elements_by_xpath('//div[@class="index_word__3waO0"]')
    with open('learn_word.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        for word in word_list:
            word_meaning = word.text.split('\n')
            writer.writerow(word_meaning)
    # 如果下一页是最后一页
    if next_page.get_attribute('class') == 'index_nomore__2fTsZ':
        break
    # 下一页
    next_page.click()
