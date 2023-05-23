import requests
from bs4 import BeautifulSoup


class AncientPoetry:
    def __init__(self, url, headers, file_path):
        self.url = url
        self.headers = headers
        self.file_path = file_path

    # 获取章节目录
    def req_table(self, link):
        # 爬取数据
        response = requests.get(url=link, headers=self.headers).text
        # 解析数据
        soup = BeautifulSoup(response, 'lxml')
        # 获取目录
        tables = soup.select('.bookcont a')
        table_urls = [a['href'] for a in tables]
        return table_urls

    # 解析详情页数据
    def book_detail(self, href):
        response = requests.get(url=href, headers=self.headers).text
        soup = BeautifulSoup(response, 'lxml')
        # 获取文章详情
        content = soup.select('.contson')[0]
        # 文章标题
        title = soup.find('b').text
        # 章节内容
        chapter_detail = [detail.text for detail in content.find_all('p')]
        return title, chapter_detail

    # 写入文件
    def download_book(self, title, chapter):
        with open(self.file_path, 'a+', encoding='utf-8') as fp:
            fp.write(title + '\n')
            for p in chapter:
                fp.write(p + '\n')

        print(title + '下载完成！')

    # 爬取内容
    def main(self):
        table_urls = self.req_table(link=self.url)
        for url in table_urls:
            href = 'https://so.gushiwen.cn' + url
            title, chapter = self.book_detail(href)
            self.download_book(title, chapter)