import requests
from bs4 import BeautifulSoup
import os

# url = 'https://www.mzitu.com/zipai/comment-page-482/#comments'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
}

# response = 1.requests.get(url=url, headers=headers).content.decode()
# soup = BeautifulSoup(response, 'lxml')
# girls = soup.select('.lazy')
# girl_urls = [girl['data-original'] for girl in girls]


# 请求数据
def req_girl(pg):
    url = 'https://www.mzitu.com/zipai/comment-page-{}/#comments'.format(pg)

    response = requests.get(url=url, headers=headers).content.decode()
    soup = BeautifulSoup(response, 'lxml')

    girls = soup.select('.lazy')
    girl_urls = [girl['data-original'] for girl in girls]
    return girl_urls


# 下载图片
def download_girl(src, filepath):
    girl_data = requests.get(url=src, headers=headers).content
    file_name = src.split('/')[-1]
    file_path = filepath + '/' + file_name
    with open(file_path, 'wb') as fp:
        fp.write(girl_data)
        print(file_name + "保存成功")


def main():
    filepath = input("请输入要保存的目录名：")
    if not os.path.exists('./{}'.format(filepath)):
        os.mkdir('./{}'.format(filepath))
    page_num = input("你想看多少页图片(1~482)：")
    for page in range(483-eval(page_num), 483):
        for src in req_girl(page):
            download_girl(src, filepath)


if __name__ == '__main__':
    main()
