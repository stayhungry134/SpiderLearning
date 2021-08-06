import requests
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.org/guwen/book_46653FD803893E4F7F702BCF1F7CCE17.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
}


# 获取章节目录
def req_table(link):
    # 爬取数据
    response = requests.get(url=link, headers=headers).text
    # 解析数据
    soup = BeautifulSoup(response, 'lxml')
    # 获取目录
    tables = soup.select('.bookcont a')
    table_urls = [a['href'] for a in tables]
    return table_urls


# 解析详情页数据
def book_detail(href):
    response = requests.get(url=href, headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    # 获取文章详情
    content = soup.select('.contson')[0]
    # 文章标题
    title_num = soup.find('b').text
    title = title_num + content.find('p').text
    # 章节内容
    chapter_detail =[detail.text for detail in content.find_all('p')]
    del chapter_detail[0]
    return title, chapter_detail


# 写入文件
def download_book(title, chapter):
    with open('./file/three kindoms.txt', 'a+', encoding='utf-8') as fp:
        fp.write(title + '\n')
        for p in chapter:
            fp.write(p + '\n')

    print(title + '下载完成！')


def main():
    table_urls = req_table(link=url)
    for href in table_urls:
        title, chapter = book_detail(href)
        download_book(title, chapter)


if __name__ == '__main__':
    main()
