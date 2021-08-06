import requests

url = 'https://www.mzitu.com/zipai/comment-page-482/#comments'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
}

response = requests.get(url=url, headers=headers)

print(response.content.decode())