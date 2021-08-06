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
#