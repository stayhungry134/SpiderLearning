# 导入相关库
import requests
from lxml import etree
import time

# 指定url
url = 'http://pic.netbian.com/4kmeinv/'

# 进行 UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
    'Connection': 'close'
}

# 指定保存目录
file_path = './file/netbian/'


# 获取图片详情页链接和下一页链接
def get_img_list(net_url):
    # 获取网页数据
    response = requests.get(url=net_url, headers=headers).content.decode('gbk')
    # 解析数据
    html = etree.HTML(response)
    # 解析图片列表
    ls_img = html.xpath('//div[@class="slist"]//li/a/@href')
    next_url = html.xpath('//div[@class="page"]/a/@href')[-1]
    return ls_img, next_url


# 爬取图片
def get_img(href):
    detail_utl = 'http://pic.netbian.com' + href
    img_detail = requests.get(url=detail_utl, headers=headers).content.decode('gbk')
    img_html = etree.HTML(img_detail)
    img_name = img_html.xpath('//h1/text()')[0]
    img_href = img_html.xpath('//div[@class="photo-pic"]//img/@src')[0]
    return img_name, img_href


# 下载图片
def download_img(name, src):
    img_url = 'http://pic.netbian.com' + src
    img_data = requests.get(url=img_url, headers=headers).content
    img_path = file_path + name + '.jpg'
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(name, "保存成功！")


# 主程序
def main():
    img_list, next_url = get_img_list(url)
    for img_url in img_list:
        img_name, img_href = get_img(img_url)
        download_img(img_name, img_href)
    return next_url


for i in range(100):
    next_url = main()
    url = 'http://pic.netbian.com' + next_url
    time.sleep(3)
    print("第{}页保存成功！！！".format(i))
