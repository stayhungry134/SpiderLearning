# 导入相关库
import requests
from lxml import etree
import os

# 指定url，高清写真网
url = 'https://m.gqxz.com/'

# 进行 UA 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
}

# 指定保存目录
file_path = './file/gqxz/'


# 解析主页数据，返回主页菜单分类和链接
def get_index(index_url):
    index_data = requests.get(url=index_url, headers=headers).content
    index_html = etree.HTML(index_data)
    a_list = index_html.xpath('//div[@class="menu"]//a/@href')
    a_name = index_html.xpath('//div[@class="menu"]//a/text()')
    del a_list[0]
    del a_name[0]
    return a_name, a_list


# 解析分栏页数据，返回分组类名和链接
def menu_group(group_str):
    group_url = 'https://m.gqxz.com/' + group_str
    group_data = requests.get(url=group_url, headers=headers).content
    group_html = etree.HTML(group_data)
    ls_group = group_html.xpath('//div[@class="more"]/p/a/@href')
    ls_name = group_html.xpath('//div[@class="more"]/p/a/text()')
    return ls_name, ls_group


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


def get_group(menu_url, folder, menu_name):
    # 风景照片
    img_groups_name, img_groups_str, group_next_page = img_group(menu_url)
    for img_group_name, img_group_str in zip(img_groups_name, img_groups_str):
        img_path = './file/gqxz/{}/{}/{}'.format(folder, menu_name, img_group_name)
        get_down(img_group_str, img_path)
    while group_next_page:
        img_groups_name, img_groups_str, group_next_page = img_group(group_next_page)
        for img_group_name, img_group_str in zip(img_groups_name, img_groups_str):
            img_path = './file/gqxz/{}/{}/{}'.format(folder, menu_name, img_group_name)
            get_down(img_group_str, img_path)
        print("下一个章节！")


# 爬取图片
def main():
    # 获取主页数据
    folders, groups_str = get_index(url)
    for folder, group_str in zip(folders, groups_str):
        # 创建文件夹
        if not os.path.exists('./file/gqxz/{}'.format(folder)):
            os.mkdir('./file/gqxz/{}'.format(folder))
        # 电脑壁纸
        menus_name, menus_str = menu_group(group_str)
        for menu_name, menu_str in zip(menus_name, menus_str):
            if not os.path.exists('./file/gqxz/{}/{}'.format(folder, menu_name)):
                os.mkdir('./file/gqxz/{}/{}'.format(folder, menu_name))
            # 风景壁纸
            menu_url = 'https://m.gqxz.com/' + menu_str
            try:
                get_group(menu_url, folder, menu_name)
            except:
                break


if __name__ == '__main__':
    main()

