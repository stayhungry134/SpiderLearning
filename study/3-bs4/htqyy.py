# 导入相关的库
import requests
from bs4 import BeautifulSoup

# 爬取数据
# 指定 URL
url = 'http://www.htqyy.com/top/musicList/hot'

# 进行 UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
    'Referer': 'http://www.htqyy.com/top/hot'
}

# 编写请求数据
data = {
    'pageIndex': '0',
    'pageSize': '20'
}

# 请求数据
response = requests.get(url=url, data=data, headers=headers).content.decode()

soup = BeautifulSoup(response, 'lxml')

music_a = soup.select('.title a')
music_nums = [num['sid'] for num in music_a]
music_names = [title['title'] for title in music_a]
print(music_nums)
print(music_names)
