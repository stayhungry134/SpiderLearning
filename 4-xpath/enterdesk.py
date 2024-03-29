# 导入相关库
import requests
from lxml import etree
from random import choice

# 指定url
# url = 'https://sj.enterdesk.com/woman/1.html'

# 进行 UA 伪装
headers = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.5 Safari/537.36',
        'Referer': 'https://sj.enterdesk.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
        'Referer': 'https://sj.enterdesk.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Referer': 'https://sj.enterdesk.com'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Referer': 'https://sj.enterdesk.com'
    }
]

# 指定保存目录
file_path = 'D:/Image/回车桌面/'


# 解析主页数据
def get_index(index_url):
    response = requests.get(url=index_url, headers=choice(headers)).content
    index_html = etree.HTML(response)
    # 获取图片链接
    detail_url = index_html.xpath('//div[@class="egeli_pic_li"]//a/@href')
    return detail_url


# 获取图片链接
def get_img(detail_url):
    detail_data = requests.get(url=detail_url, headers=choice(headers)).content
    detail_html = etree.HTML(detail_data)
    # 获取图片链接
    img_url = detail_html.xpath('//div[@class="arc_main_pic"]/img/@src')[0]
    high_img_url = img_url.replace('edpic', 'edpic_source')
    img_name = high_img_url.split('/')[-1]
    return high_img_url, img_name


# 保存图片
def down_img(img_url, img_name):
    img_data = requests.get(url=img_url, headers=choice(headers)).content
    img_path = file_path + img_name
    with open(img_path, 'wb') as f:
        f.write(img_data)
        print(img_name, "\t\t下载成功！！！")


def main():
    for i in range(1, 2):
        url = f'https://www.enterdesk.com/search/{i}-13-6-0-0-0'
        try:
            detail_url = get_index(url)
            for detail in detail_url:
                try:
                    high_img_url, img_name = get_img(detail)
                    down_img(high_img_url, img_name)
                except:
                    continue
        except:
            print(url)


if __name__ == '__main__':
    main()