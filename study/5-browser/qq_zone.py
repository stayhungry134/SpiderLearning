# QQ空间
from selenium import webdriver
import time
from lxml import etree

driver = webdriver.Chrome('D:/Installation package/Chrome/chromedriver.exe')
driver.get('https://qzone.qq.com/')
# driver.get('https://user.qzone.qq.com/3045395793?source=aiostar')

cookies = [
    {'domain': '.qzone.qq.com', 'expiry': 1934200528, 'httpOnly': False, 'name': 'cpu_performance_v8', 'path': '/', 'secure': False, 'value': '0'},
    {'domain': '.user.qzone.qq.com', 'expiry': 1618841433, 'httpOnly': False, 'name': 'x-stgw-ssl-info', 'path': '/', 'secure': False, 'value': '8b79e88b57f7c01c3ed610b55fc1e4fc|0.148|-|25|.|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|52000|h2|0'},
    {'domain': '.qzone.qq.com', 'expiry': 1934200513, 'httpOnly': False, 'name': 'QZ_FE_WEBP_SUPPORT', 'path': '/', 'secure': False, 'value': '1'},
    {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s2703646080'},
    {'domain': 'user.qzone.qq.com', 'httpOnly': False, 'name': '1414312486_totalcount', 'path': '/', 'secure': False, 'value': '129401'},
    {'domain': 'user.qzone.qq.com', 'httpOnly': False, 'name': '1414312486_todaycount', 'path': '/', 'secure': False, 'value': '2'},
    {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2000321307'},
    {'domain': '.qzone.qq.com', 'httpOnly': False, 'name': 'p_skey', 'path': '/', 'secure': True, 'value': 'CBEfGOQF4NCpHqAWXzrcnSpEFhHjIpYbtJ0AStB1xfY_'},
    {'domain': '.qzone.qq.com', 'expiry': 1618847999, 'httpOnly': False, 'name': 'Loading', 'path': '/', 'secure': False, 'value': 'Yes'},
    {'domain': '.qzone.qq.com', 'httpOnly': False, 'name': 'pt4_token', 'path': '/', 'secure': False, 'value': 'YE8fVAPkyU*kow9Yd*2lURk0f5ij14EIWsbj3a6bS2A_'},
    {'domain': '.user.qzone.qq.com', 'expiry': 1621432535, 'httpOnly': False, 'name': 'qz_screen', 'path': '/', 'secure': False, 'value': '1920x1080'},
    {'domain': '.qzone.qq.com', 'httpOnly': False, 'name': 'p_uin', 'path': '/', 'secure': False, 'value': 'o1414312486'},
    {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'HkxRlM7qev'},
    {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False, 'value': '0.3617727160443862'},
    {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'dd2c3f659a5a5868567e6c011788eeb0088a88c6379947042948025761d6539f'},
    {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False, 'value': '@VO6qvwDF0'},
    {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False, 'value': 'o1414312486'}]
time.sleep(3)

# 删除所有cookie
driver.delete_all_cookies()
time.sleep(1)
# 写入cookie
for cookie in cookies:
    driver.add_cookie(cookie)

# 刷新页面
driver.refresh()

# 个人说说页面
self_blog = driver.find_element_by_xpath('//div[@class="head-nav"]/li[@class="menu_item_311 cur"]')
# 进入个人说说页面
self_blog.click()

blog_items = driver.find_elements_by_xpath('//ol[@class="msgList"/li')

