import urllib.request

import urllib.parse

url = 'https://www.baidu.com'

response = urllib.request.urlopen(url=url, data=None, timeout=5, cafile=None, capath=None, cadefault=False, context=None)
# 网页内容
print(response.read().decode('utf-8'))
# 状态码
print(response.status)
# 请求头信息
print(response.getheaders())
# 获取响应头Sever值
print(response.getheader('Server'))

