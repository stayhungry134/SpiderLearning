"""
name: base_class
create_time: 2023/5/20
author: Ethan

Description: 各类壁纸网站的基类
"""
import requests
from lxml import etree

from datas.global_data import chrome_agent


class EnterDesk:
    """回车桌面"""
    def __init__(self, category='', save_path='D:/Image/回车桌面/', *args, **kwargs):
        self.url = 'https://www.enterdesk.com/'
        self.headers = {
            'User-Agent': chrome_agent,
            'Referer': self.url,
        }
        self.category = category
        self.save_path = save_path

    def parsing_page(self, page=1):
        """解析页面，获得图片详情页的 url"""
        url = f"{self.url}{self.category}{'/' if self.category else ''}{page}"
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        img_detail_urls = html.xpath('//div[contains(@class, "egeli_pic_li")]//dd/a/@href')
        return img_detail_urls

    def parsing_detail(self, img_detail_url):
        """解析详情页，获得图片的 url"""
        response = requests.get(img_detail_url, headers=self.headers)
        html = etree.HTML(response.text)
        img_url = html.xpath('//div[contains(@class, "arc_main_pic")]/img/@src')[0]
        return img_url.replace('edpic', 'edpic_source')

    def download_img(self, img_url):
        """下载图片"""
        response = requests.get(img_url, headers=self.headers)
        img_name = img_url.split('/')[-1]
        with open(self.save_path + img_name, 'wb') as f:
            f.write(response.content)
            print(f"{img_name}下载成功！！！")