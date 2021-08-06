# 肯德基地址信息的爬取
# 导入 1.requests 库
import requests
import json

# 肯德基网址
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'

# UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36'
}

keyword = input("请输入你想要的查询的地址：")

# 要发送的数据
param = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': '1',
    'pageSize': '10'
}

data = {
    'op': 'keyword'
}

# 爬取数据
response = requests.post(url=url, params=param, data=data, headers=headers)

# 整理并保存数据
dic_json = response.json()

filename = './file/' + keyword + '.json'
fp = open(filename, 'w', encoding='utf-8')
json.dump(dic_json, fp=fp, ensure_ascii=False)
print("可以了")
