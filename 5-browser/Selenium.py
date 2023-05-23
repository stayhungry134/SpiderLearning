from selenium import webdriver

# 打开浏览器, 传入的参数是驱动的路径
wd = webdriver.Chrome(r'D:\Installation package\Chrome\chromedriver.exe')

# 浏览器打开某个网址
wd.get('https://www.baidu.com')

# 选择元素
# find_elements 符合条件的 所有 元素， 如果没有符合元素， 返回空列表
# find_element 符合条件的 第一个 元素， 如果没有符合元素， 抛出 NoSuchElementException 异常

# 通过 id 选择对象
element = wd.find_element_by_id('kw')  # 返回第一个
# element = wd.find_elements_by_id('kw')  # 返回所有符合条件的元素

# 通过类名选择对象，有多个class属性时只能写一个
class_element = element.find_element_by_class_name('classname')  # 返回第一个
# class_element = wd.find_elements_by_class_name('classname')  # 返回所有

# 通过 tag 名选择元素
div = wd.find_element_by_tag_name('tagname')

# container = wd.find_element_by_css_selector()

# 操作
element.send_keys('我是谁\n')  # 输入字符串
# clear() 清空文字
# click() 点击

ls = [{'domain': '.shanbay.com', 'expiry': 1715787434, 'httpOnly': False, 'name': 'csrftoken', 'path': '/',
       'sameSite': 'Lax', 'secure': False, 'value': 'fdb893e3b5b995f4697cfc8af6a04110'},
      {'domain': '.shanbay.com', 'expiry': 1685115776, 'httpOnly': True, 'name': 'auth_token', 'path': '/',
       'sameSite': 'Lax', 'secure': False,
       'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjMyMjc0ODIwLCJleHAiOjE2ODUxMTU3NzUsImV4cF92MiI6MTY4NTExNTc3NSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJzdGF5aHVuZ3J5MTM0IiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiJhMGIzODM3MmYzZmYxMWVkOTIyNDk2Y2RmNTVmZjE4NSJ9.ByzEkRiJlkXoYq3UtLoES0cyqD2bDmX0qGG718dqwdg'},
      {'domain': '.shanbay.com', 'expiry': 1718811476, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross',
       'path': '/', 'sameSite': 'Lax', 'secure': False,
       'value': '%7B%22distinct_id%22%3A%22zprmko%22%2C%22first_id%22%3A%2218825355fe01935-0f6ea83172f8ff-5153162-480000-18825355fe11c43%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%7D%2C%22%24device_id%22%3A%2218825355fe01935-0f6ea83172f8ff-5153162-480000-18825355fe11c43%22%7D'},
      {'domain': '.shanbay.com', 'expiry': 1684252799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user',
       'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'},
      {'domain': '.shanbay.com', 'expiry': 1684252034, 'httpOnly': False, 'name': '_gat', 'path': '/',
       'sameSite': 'Lax', 'secure': False, 'value': '1'},
      {'domain': '.shanbay.com', 'expiry': 1718811476, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax',
       'secure': False, 'value': 'GA1.2.1462367268.1684251435'}]
