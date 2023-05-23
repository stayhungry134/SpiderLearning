# 导入相关库
import requests
from lxml import etree
from random import choice

# 指定url
url = 'http://pic.netbian.com/4kmeinv/'

# 进行 UA 伪装
headers = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.5 Safari/537.36',
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    }
]

# 指定保存目录
file_path = 'E:/images/netbian/'


# 获取图片详情页链接和下一页链接
def get_img_list(net_url):
    # 获取网页数据
    response = requests.get(url=net_url, headers=choice(headers)).content.decode('gbk')
    # 解析数据
    html = etree.HTML(response)
    # 解析图片列表
    ls_img = html.xpath('//div[@class="slist"]//li/a/@href')
    next_url = html.xpath('//div[@class="page"]/a/@href')[-1]
    return ls_img, next_url


# 爬取图片
def get_img(href):
    detail_utl = 'http://pic.netbian.com' + href
    img_detail = requests.get(url=detail_utl, headers=choice(headers)).content.decode('gbk')
    img_html = etree.HTML(img_detail)
    img_name = img_html.xpath('//h1/text()')[0]
    img_href = img_html.xpath('//div[@class="photo-pic"]//img/@src')[0]
    return img_name, img_href


# 下载图片
def download_img(name, src):
    img_url = 'http://pic.netbian.com' + src
    img_data = requests.get(url=img_url, headers=choice(headers)).content
    img_path = file_path + name + '.jpg'
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(name, "保存成功！")


# 主程序
def main():
    img_list, next_url = get_img_list(url)
    try:
        for img_url in img_list:
            try:
                img_name, img_href = get_img(img_url)
                download_img(img_name, img_href)
            except:
                continue
        return next_url
    except:
        pass


for i in range(21, 146):
    next_url = main()
    url = 'http://pic.netbian.com' + next_url
    print("第{}页保存成功！！！".format(i + 1))
