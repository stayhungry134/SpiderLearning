# 导入相关库
import requests
from lxml import etree
from random import choice

# 指定url
# url = 'https://sj.enterdesk.com/woman/1.html'

# 进行 UA 伪装
headers = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.5 Safari/537.36',
        'Referer': 'https://sj.enterdesk.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
        'Referer': 'https://sj.enterdesk.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Referer': 'https://sj.enterdesk.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Referer': 'https://sj.enterdesk.com'
    }
]

# 指定保存目录
file_path = 'E:/images/jijian/'

