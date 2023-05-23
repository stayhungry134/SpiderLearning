"""
name: shanbay_test
create_time: 2023/5/19
author: Ethan

Description: 
"""
import requests
from requests import Session

url = 'https://web.shanbay.com/wordsweb/#/words-table'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': 'csrftoken=aabe78da8cfdb9e2207f53fc99166fd1; _ga=GA1.2.994386593.1684132597;auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjQ5NTkzNjQ0LCJleHAiOjE2ODUzMjg4MzUsImV4cF92MiI6MTY4NTMyODgzNSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJXZWNoYXRfOTk2MThjOTAxZWYzNjNkZiIsImlzX3N0YWZmIjowLCJzZXNzaW9uX2lkIjoiYjIwZTI4YzRmNWVmMTFlZGFkYjRmNjhkMjkxNjU4OTQifQ.sbGgxd9OXIR13OsqQ-6h-1ZszZ9HV6CkKnS4oSW5er4;',
}

response = requests.get(url=url, headers=headers)

print(response.text)