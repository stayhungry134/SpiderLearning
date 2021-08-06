import requests
from random import choice
from lxml import etree

url = 'https://m.bcoderss.com/page/1/'

headers = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.5 Safari/537.36',
        'Referer': 'https://m.bcoderss.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
        'Referer': 'https://m.bcoderss.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Referer': 'https://m.bcoderss.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Referer': 'https://m.bcoderss.com/'
    }
]


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
    file_path = 'D:/images/mobile1/' + img_name
    with open(file_path, 'wb') as f:
        f.write(img_data)
        print(img_name + '\t\t\t\t保存成功！！！')


# 开始爬取
def main():
    for i in range(2, 6):
        index_url = 'https://m.bcoderss.com/tag/%e5%8d%8e%e4%b8%ba/page/{}/'.format(i)
        try:
            imgs_detail = get_index(index_url)
            for img_detail in imgs_detail:
                try:
                    img_url = get_img(img_detail)
                    save_img(img_url)
                except:
                    pass
        except:
            pass


if __name__ == '__main__':
    main()
