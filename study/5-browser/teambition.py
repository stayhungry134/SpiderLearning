# coding=utf-8
"""
name: teambition.py
create_time: 2022-09-26
author: Ethan

Description: 爬取 teambition 自己写的日记
"""
from selenium import webdriver
import time

driver = webdriver.Chrome('../0-file/chromedriver.exe')
driver = webdriver.firefox
driver.get('https://www.teambition.com/project/5fedd84cd13ac9c9c6cf14f0/app/5eba5fba6a92214d420a3219/workspaces/5fedd84c2aa6d50046cc8815/docs/5feeae124cc5830001f11eb7')

cookies = [
    {'domain': '.teambition.com', 'expiry': 1664271979, 'httpOnly': False, 'name': 'mp_tbpanel__c', 'path': '/', 'secure': False, 'value': '1'},
    {'domain': '.teambition.com', 'expiry': 1666777579, 'httpOnly': False, 'name': 'referral', 'path': '/', 'secure': False, 'value': '%7B%22domain%22%3A%22account.teambition.com%22%2C%22path%22%3A%22%2F%22%2C%22query%22%3A%22%22%2C%22hash%22%3A%22%22%7D'},
    {'domain': '.teambition.com', 'expiry': 1664790377, 'httpOnly': False, 'name': 'teambition_lang', 'path': '/', 'secure': False, 'value': 'zh'},
    {'domain': '.teambition.com', 'expiry': 1664271977, 'httpOnly': True, 'name': 'TB_ACCESS_TOKEN', 'path': '/', 'secure': True, 'value': 'eyJhbGciOiJFZDI1NTE5IiwidHlwIjoiSldUIn0.eyJhcHAiOiI1ZDRjZWMzMGE1NWMwOTAwMDE3MWNiZDQiLCJhdWQiOiIiLCJleHAiOjE2NjQ0NDQ3NzcsImlhdCI6MTY2NDE4NTU3NywiaXNzIjoidHdzIiwianRpIjoiU3AyaHQwdE5WV0tyOWQwbFMtWFFoSmJxTHA0RzE4VGgwb05NZkUyMXMxZz0iLCJyZW5ld2VkIjoxNjA4NTA5ODUwMDA5LCJzY3AiOlsiYXBwX3VzZXIiXSwic3ViIjoiNWY5Nzc5NDAwZDY3MzFkMjk5M2FlNjRlIiwidHlwIjoiYWNjZXNzX3Rva2VuIn0.2jYyT1GEWgp20PKXtQB7MF3dxENv3nK8eSImZhADFPoj0VEr34Im868j_P1OqvfO14r4byhWgx_DADGox55cDw'},
    {'domain': '.teambition.com', 'expiry': 1698745577, 'httpOnly': False, 'name': 'cna', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '6WK4G5rlSjECAXBwF9LZnjAX'},
    {'domain': '.teambition.com', 'expiry': 1698745564, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1523353174.1664185564'},
    {'domain': '.teambition.com', 'expiry': 1695721579, 'httpOnly': False, 'name': 'mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel', 'path': '/', 'secure': False, 'value': '%7B%22distinct_id%22%3A%20%221837930b67ac5-0846ce9187e0ab-26021c51-1fa400-1837930b67b1cd%22%2C%22userKey%22%3A%20%225f9779400d6731d2993ae64e%22%2C%22name%22%3A%20%22%E6%8D%AD%E9%98%96%22%2C%22email%22%3A%20%221414312486%40qq.com%22%2C%22avatarUrl%22%3A%20%22https%3A%2F%2Ftcs.teambition.net%2Fthumbnail%2F11207bc8239007a65d6ca96374ff2bfc2ac6%2Fw%2F200%2Fh%2F200%22%2C%22env%22%3A%20%22ng%22%2C%22version%22%3A%20%222.14.1%22%2C%22frontVersion%22%3A%20%224.45.16%22%2C%22timezone%22%3A%208%2C%22%24os_version%22%3A%20%22Windows%20NT%2010.0%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Faccount.teambition.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22account.teambition.com%22%7D'},
    {'domain': '.teambition.com', 'expiry': 1664185624, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},
    {'domain': '.teambition.com', 'expiry': 1666777576, 'httpOnly': True, 'name': 'TEAMBITION_SESSIONID.sig', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'ZDCbAqK2x1Vlid5tpoPia-TnDwQ'},
    {'domain': '.teambition.com', 'expiry': 1666777576, 'httpOnly': True, 'name': 'TEAMBITION_SESSIONID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'eyJhdXRoVXBkYXRlZCI6MTYwODUwOTg1MDAwOSwibG9naW5Gcm9tIjoidGVhbWJpdGlvbiIsInVpZCI6IjVmOTc3OTQwMGQ2NzMxZDI5OTNhZTY0ZSIsInVzZXIiOnsiX2lkIjoiNWY5Nzc5NDAwZDY3MzFkMjk5M2FlNjRlIiwibmFtZSI6IuaNremYliIsImVtYWlsIjoiMTQxNDMxMjQ4NkBxcS5jb20iLCJhdmF0YXJVcmwiOiJodHRwczovL3Rjcy50ZWFtYml0aW9uLm5ldC90aHVtYm5haWwvMTEyMDdiYzgyMzkwMDdhNjVkNmNhOTYzNzRmZjJiZmMyYWM2L3cvMjAwL2gvMjAwIiwicmVnaW9uIjoiY24iLCJsYW5nIjoiIiwiaXNSb2JvdCI6ZmFsc2UsIm9wZW5JZCI6IiIsInBob25lRm9yTG9naW4iOiIxNTg4NzQzMzM3NCJ9fQ=='},
    {'domain': '.teambition.com', 'expiry': 1679737577, 'httpOnly': False, 'name': 'TB_GTA', 'path': '/', 'secure': False, 'value': '%7B%22pf%22%3A%7B%22cd%22%3A%22.teambition.com%22%2C%22dr%22%3A1%7D%2C%22uk%22%3A%225f9779400d6731d2993ae64e%22%7D'},
    {'domain': '.teambition.com', 'expiry': 1679737577, 'httpOnly': False, 'name': '_bl_uid', 'path': '/', 'secure': False, 'value': '9jljm8IRi6nlR248vhOXnX6xv9OR'},
    {'domain': '.teambition.com', 'expiry': 1664271964, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.597856466.1664185564'}
]

# 获取 cookies, 打开之后登录，然后等待打印
# time.sleep(20)
# cookie = driver.get_cookies()
# print(cookie)

# 更新cookie
driver.delete_all_cookies()
time.sleep(3)
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

# 获取月份
# driver.implicitly_wait(10)
# month_element = driver.find_elements_by_xpath('//a[@class="node-title__1SwE"]')
# month_href = {month.get_attribute('innerHTML'): month.get_attribute('href') for month in month_element}
# with open('teambition.txt', 'a+', encoding='utf-8') as f:
#     for month in month_href:
#         f.writelines(month + ': ' + month_href.get(month))
#         f.writelines('\n')

# 获取日期
with open('teambition.txt', encoding='utf-8') as f:
    with open('teambition_day.txt', 'a', encoding='utf-8') as d:
        line = f.readline()
        while line is not None and line != '':
            print(line.split(': '))
            month, href = line.split(': ')
            driver.get(href.replace('\n', ''))
            driver.implicitly_wait(10)
            days_element = driver.find_elements_by_xpath('//a[@class="item-container__1Ffc"]')
            days_href = {day.get_attribute('innerHTML'): day.get_attribute('href') for day in days_element}
            for day in days_href:
                d.writelines(month + ':' + days_href.get(day))
                d.writelines('\n')
            d.writelines('\n\n')
            line = f.readline()