import requests
from bs4 import BeautifulSoup

url = 'https://pixabay.com/images/search/'

data = {
    'order': 'ec',
    'pagi': '1'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
    'referer': 'https://pixabay.com/images/search/?order=ec'
}

response = requests.get(url=url, data=data, headers=headers).content.decode()

with open('123.html', 'w', encoding='utf-8') as fp:
    fp.write(response)

# soup = BeautifulSoup(response, 'lxml')
# img_items = soup.select('.item a')
#
# img_urls = [a['href'] for a in img_items]
# print(img_urls)
