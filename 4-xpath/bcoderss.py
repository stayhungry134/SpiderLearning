# 导入相关库
import requests
from lxml import etree
from random import choice

# 指定url
# url = 'http://m.bcoderss.com/tag/%E7%BE%8E%E5%A5%B3/page/1/'

# 进行 UA 伪装
headers = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.5 Safari/537.36',
        'Referer': 'http://m.bcoderss.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
        'Referer': 'http://m.bcoderss.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Referer': 'http://m.bcoderss.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Referer': 'http://m.bcoderss.com'
    }
]

# 指定保存目录
file_path = 'E:/images/phone/'


# 解析主页
def get_index(index_url):
    index_data = requests.get(url=index_url, headers=choice(headers)).content
    index_html = etree.HTML(index_data)
    # 获取图片详情页链接地址
    detail_url = index_html.xpath('//ul[@id="main"]//a/@href')
    return detail_url


# 解析详情页
def get_detail(detail_url):
    detail_data = requests.get(url=detail_url, headers=choice(headers)).content
    detail_html = etree.HTML(detail_data)
    # 获取图片地址
    img_url = detail_html.xpath('//div[@class="single-wallpaper"]/img/@src')[0]
    img_name = img_url.split('/')[-1]
    return img_url, img_name


# 下载图片
def down_img(img_url, img_name):
    img_data = requests.get(url=img_url, headers=choice(headers)).content
    img_path = file_path + img_name
    with open(img_path, 'wb') as f:
        f.write(img_data)
        print(img_name, "\t\t下载成功！！！")


def main():
    for i in range(1, 88):
        url = 'https://m.bcoderss.com/page/{}/'.format(i)
        try:
            detail = get_index(url)
            for detail_url in detail:
                try:
                    img_url, img_name = get_detail(detail_url)
                    down_img(img_url, img_name)
                except:
                    continue
        except:
            print(url)


if __name__ == '__main__':
    main()