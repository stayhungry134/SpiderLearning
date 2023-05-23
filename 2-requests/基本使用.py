import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
# <class 'requests.models.Response'>

print(r.status_code)
# 200

print(type(r.text))
# <class'str'>

# 网页内容
print(r.text)

# 网页cookies
print(r.cookies)