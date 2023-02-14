import datetime
import re
import sys

import requests
from random import choice
from lxml import etree
import sqlite3

url = 'https://m.bcoderss.com/page/1/'
root_path = 'C:/Users/Ethan White/Pictures/Camera Roll/'
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
conn = sqlite3.connect('../0-file/spider.db')
cursor = conn.cursor()
# 如果数据库没有就创建
cursor.execute("""CREATE TABLE IF NOT EXISTS mobile (
                    id INTEGER PRIMARY KEY, 
                    img_name TEXT, 
                    download_time DATETIME, 
                    size TEXT );""")


# 检查记录是否存在
def check_img(img_name):
    # 查询是否有 img_name=img_id 的记录
    cursor.execute(f"SELECT * FROM mobile WHERE img_name='{img_name}'")
    rows = cursor.fetchall()
    if rows:
        return False
    else:
        return True


# 记录下载记录
def write_record(img_name, size):
    download_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(f"INSERT INTO mobile (img_name, download_time, size) VALUES (?, ?, ?)",
                   (img_name, download_time, size))
    conn.commit()


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
    suffix = re.search(r'[^\/]+$', img_url).group()
    img_name = re.match(r'\w+', suffix).group()
    rule_url = img_url.replace(suffix, f"{img_name}.jpg")
    return rule_url, img_name


# 保存图片
def save_img(rule_url, img_name):
    img_data = requests.get(url=rule_url, headers=choice(headers)).content
    file_path = root_path + img_name
    with open(f"{file_path}.jpg", 'wb') as f:
        f.write(img_data)
        print(f"{img_name}\t\t\t\t保存成功！！！")
        write_record(img_name, round(sys.getsizeof(img_data)/1024, 2))


# 开始爬取
def main():
    for i in range(1, 2):
        index_url = f"https://m.bcoderss.com/page/{i}/"
        try:
            imgs_detail = get_index(index_url)
            for img_detail in imgs_detail:
                try:
                    rule_url, img_name = get_img(img_detail)
                    if check_img(img_name):
                        save_img(rule_url, img_name)
                    else:
                        print(f"{img_name}\t\t\t\t已存在！！！")
                except:
                    print(img_detail)
        except:
            pass


if __name__ == '__main__':
    main()
