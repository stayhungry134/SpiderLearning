import datetime
import re
from threading import Thread

import requests
from random import choice
from lxml import etree
import sqlite3

url = 'https://m.bcoderss.com/page/1/'
#root_path = 'E:/image/mobile/'
root_path = '/opt/download/image/'
headers = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Referer': 'https://m.bcoderss.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
        'Referer': 'https://m.bcoderss.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Referer': 'https://m.bcoderss.com/'
    },
]

# 连接数据库
# conn = sqlite3.connect('../0-file/spider.db')
# cursor = conn.cursor()
# # 如果数据库没有就创建
# cursor.execute("""CREATE TABLE IF NOT EXISTS mobile (
#                     id INTEGER PRIMARY KEY,
#                     img_url TEXT,
#                     download_time DATETIME);""")
#
#
# # 检查记录是否存在
# def check_img(img_name):
#     # 查询是否有 img_name=img_id 的记录
#     cursor.execute(f"SELECT * FROM mobile WHERE img_url='{img_name}'")
#     rows = cursor.fetchall()
#     if rows:
#         return False
#     else:
#         return True
#
#
# # 记录下载记录
# def write_record(img_name):
#     download_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     cursor.execute(f"INSERT INTO mobile (img_url, download_time) VALUES (?, ?)",
#                    (img_name, download_time))
#     conn.commit()


# 解析主页数据
def get_index(index_url):
    response = requests.get(url=index_url, headers=choice(headers)).content.decode()
    html = etree.HTML(response)
    # 获取链接
    imgs_detail = html.xpath('//ul[@id="main"]/li/a/@href')
    return imgs_detail


# 获取图片
def get_img(img_detail):
    detail_data = requests.get(url=img_detail, headers=choice(headers)).content.decode()
    html = etree.HTML(detail_data)
    img_url = html.xpath('//div[@class="single-wallpaper"]/img/@src')[0]
    return img_url


# 保存图片
def save_img(img_url):
    img_data = requests.get(url=img_url, headers=choice(headers)).content
    img_name = img_url.split('/')[-1]
    file_path = root_path + img_name
    with open(file_path, 'wb') as f:
        f.write(img_data)
        print(img_name + '\t\t\t\t保存成功！！！')


def save_task(img_detail):
    img_url = get_img(img_detail)
    rule_url = re.sub('-\d*x\d*', '', img_url)
    save_img(rule_url)


# 开始爬取
def main():
    for i in range(334, 500):
        print(f"----------第{i}页--------------")
        index_url = f'https://m.bcoderss.com/page/{i}/'
        imgs_detail = get_index(index_url)
        threads = []
        for i in range(len(imgs_detail)):
            task = Thread(target=save_task, args=(imgs_detail[i], ))
            task.start()
            threads.append(task)
        for t in threads:
            t.join()


if __name__ == '__main__':
    main()
