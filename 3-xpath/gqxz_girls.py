# 导入相关库
import requests
from lxml import etree

# 指定url，高清写真网
url = 'https://m.gqxz.com/'

# 进行 UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
}

# 指定保存目录
file_path = 'D:/images/jj20/'


# 解析小分栏数据，返回分组类名和链接，下一页链接
def img_group(img_group_url):
    group_url = img_group_url
    group_data = requests.get(url=group_url, headers=headers).content
    group_html = etree.HTML(group_data)
    div_item = group_html.xpath('//div[@class="item"]')[0]
    # 获取下一页链接
    pages = group_html.xpath('//div[@id="page"]//a/@href')
    this_page = group_html.xpath('//div[@id="page"]//a[@class="listpage curpage"]/@href')[0]
    # 判断下一页是否和尾页链接一样，如果一样，返回false
    if pages[-1] == this_page:
        next_page = False
    else:
        next_page = pages[-2]
    # return div_item
    ls_group = div_item.xpath('./ul//a/@href')
    ls_name = div_item.xpath('./ul//a/p/text()')
    return ls_name, ls_group, next_page


# 解析图片详情页，返回图片名称，图片地址，下一页链接
def get_img(detail_str):
    detail_url = 'https://m.gqxz.com' + detail_str
    img_detail = requests.get(url=detail_url, headers=headers).content
    img_html = etree.HTML(img_detail)
    img_name = img_html.xpath('//div[@id="endtext"]/p/img/@title')[0].split(' ')[-1]
    img_url = img_html.xpath('//div[@id="endtext"]/p/img/@src')[0]
    pages = img_html.xpath('//div[@id="page"]/a/@href')
    this_page = img_html.xpath('//div[@id="page"]/a[@class="listpage curpage"]/@href')[0]
    if pages[-1] == this_page:
        next_page = False
    else:
        next_page = pages[-1]
    return img_name, img_url, next_page


# 下载图片
def download_img(img_name, img_url):
    img_path = img_name + '.jpg'
    img_data = requests.get(url=img_url, headers=headers).content
    with open(img_path, 'wb') as f:
        f.write(img_data)
        print(img_name, "下载成功！！！")


def get_down(img_group_str, imgs_path):
    img_name, img_url, img_next_page = get_img(img_group_str)
    download_img(imgs_path + img_name, img_url)
    while img_next_page:
        img_name, img_url, img_next_page = get_img(img_next_page)
        download_img(imgs_path + img_name, img_url)
    print("!!!!!!!!!!!")


def get_group(menu_url):
    # 风景照片
    img_groups_name, img_groups_str, group_next_page = img_group(menu_url)
    for img_group_name, img_group_str in zip(img_groups_name, img_groups_str):
        img_path = 'D:/images/mobil/{}'.format(img_group_name)
        get_down(img_group_str, img_path)
    while group_next_page:
        img_groups_name, img_groups_str, group_next_page = img_group(group_next_page)
        for img_group_name, img_group_str in zip(img_groups_name, img_groups_str):
            img_path = 'D:/images/mobil/{}'.format(img_group_name)
            get_down(img_group_str, img_path)
        print("下一个章节！")


# 爬取图片
def main():
    group_url = input("请输入网址：")
    get_group(group_url)


if __name__ == '__main__':
    main()