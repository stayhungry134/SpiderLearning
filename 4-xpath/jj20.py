import requests
from lxml import etree
import time
from random import choice

# url = 'http://www.jj20.com/bz/nxxz/list_7_1.html'

# url = input("请输入网址：")

headers = [
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4427.5 Safari/537.36',
        'Referer': 'http://cj.jj20.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
        'Referer': 'http://cj.jj20.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Referer': 'http://cj.jj20.com/'
    },
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Referer': 'http://cj.jj20.com/'
    }
]



# 获取主页数据
def get_index(index_url):
    # 发起请求
    index_data = requests.get(url=index_url, headers=choice(headers)).content
    # 解析数据
    index_html = etree.HTML(index_data)
    # 获取具体图片集链接
    imgs_group = index_html.xpath('//ul[@class="picbz"]/li/a[1]/@href')
    # ['/bz/nxxz/shxz/318786.html', '/bz/nxxz/nxmt/318147.html', ...]
    return imgs_group


# 获取照片集数据, 返回查看图片编号和下一页数据
def get_img_group(group_url):
    # 发起请求
    group_data = requests.get(url=group_url, headers=choice(headers)).content
    # 解析数据
    group_html = etree.HTML(group_data)
    # 获取查看原图链接
    imgs = group_html.xpath('//ul[@id="showImg"]/li//img/@src')
    s_imgs_id = [img.split('allimg')[-1] for img in imgs]  # img_url.split('allimg')[-1]
    imgs_id = [img.replace('-lp', '') for img in s_imgs_id] # img_id.replace('-1200', '')
    # ('/1114/022621113921/210226113921-1.jpg', 'http://www.jj20.com/bz/nxxz/shxz318786_2.html')
    return imgs_id


# 保存图片
def get_img(img_id):
    img_url = 'http://pic.jj20.com/up/allimg' + img_id
    img_data = requests.get(url=img_url, headers=choice(headers)).content
    img_name = img_id.split('/')[-1]
    img_path = 'D:/images/jj20/' + img_name
    with open(img_path, 'wb') as f:
        f.write(img_data)
        print(img_name, "保存成功")


def main():
    for i in range(1, 40):
        url = 'http://www.jj20.com/bz/nxxz/list_7_{}.html'.format(i)
        imgs_group = get_index(url)
        try:
            for img_group in imgs_group:
                img_group_url = 'http://www.jj20.com/' + img_group
                imgs_id = get_img_group(img_group_url)
                for img_id in imgs_id:
                    get_img(img_id)
            time.sleep(1)
        except:
            print(imgs_group)
            print(url)


if __name__ == '__main__':
    main()

