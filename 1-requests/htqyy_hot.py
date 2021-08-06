# 导入相关库
import requests

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
response = requests.get(url=url, data=data, headers=headers)

print(response.content.decode())
