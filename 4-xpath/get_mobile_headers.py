"""
name: get_mobile_headers.py
create_time: 2023-02-13
author: Ethan White

Description: 获取手机壁纸网站的 cookie
"""
import re
import requests
from lxml import html, etree

url = 'https://m.bcoderss.com/'

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Referer': 'https://m.bcoderss.com/',
},

session_requests = requests.session()

login_url = "https://m.bcoderss.com/login/"
hph_url = 'https://m.bcoderss.com/wp-admin/admin-ajax.php'

payload = {
    'username': '',
    'password': '....',
}

response = session_requests.post(login_url, data=payload, headers=dict(login_url))

img_detail = 'https://m.bcoderss.com/2023/02/13/%e4%b9%8c%e8%b4%bc%e6%b8%b8%e6%88%8f-oled-%e9%bb%91%e8%89%b2-iphone-%e5%a3%81%e7%ba%b8/'
# session_requests.get()

# with requests.Session() as s:
#     p = s.post('https://m.bcoderss.com/wp-admin/admin-ajax.php', data=payload)
#     print(p.content)
#
#     detail_data = s.get('https://m.bcoderss.com/', headers=dict(re)).content.decode()
#     res = etree.HTML(detail_data)
#     test = res.xpath('/html/body/header/nav/div/div[1]/div[3]/a[1]/img[2]')
#     # img_url = res.xpath('//div[@id="shengji"]/a/@href')
#     # print(img_url)
#     print(test)
