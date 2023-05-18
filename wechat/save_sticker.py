"""
name: save_sticker
create_time: 2023/5/17
author: Ethan

Description: 用于保存微信表情包
"""
import os
import uuid
import requests
from lxml import etree
"""
https://mp.weixin.qq.com/s?__biz=MzIxMzQ4NjUxNQ==&mid=2247678844&idx=3&sn=d626f59f2c8c4e3fb3adb8626443c6e1&chksm=97ba65a0a0cdecb6240478826ca96438d52831ebe57118ce29f624cef19962ed14f1e7453071&scene=21#wechat_redirect
https://mp.weixin.qq.com/s?__biz=MzIxMzQ4NjUxNQ==&mid=2247678844&idx=3&sn=d626f59f2c8c4e3fb3adb8626443c6e1&chksm=97ba65a0a0cdecb6240478826ca96438d52831ebe57118ce29f624cef19962ed14f1e7453071&scene=21#wechat_redirect
"""
# 指定保存目录
file_path = 'D:/Image/sticker/'
url = input("请输入表情包公众号链接：")

response = requests.get(url)
html = etree.HTML(response.content.decode())
# img_urls = html.xpath('//img[contains(@class, "wxw-img")]/@data-src')
img_urls = html.xpath('//img[contains(@class, "__bg_gif")]/@src')
for img_url in img_urls:
    img = requests.get(img_url).content
    file_name = uuid.uuid4().hex + '.gif'
    with open(f'{file_path}{file_name}', 'wb') as f:
        f.write(img)
        print(f'{file_name}------保存成功！')