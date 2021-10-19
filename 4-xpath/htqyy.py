import requests
from lxml import etree


# 指定 URL
url = 'http://www.htqyy.com/top/musicList/hot'


# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
    'Referer': 'http://www.htqyy.com/top/hot',
}
# params = {
#     'pageIndex': '2',
#     'pageSize': '20'
# }


# 获取每一页的数据
def get_index(index_url, params):
    response = requests.get(url=index_url, headers=headers, params=params).content.decode()
    return response


# 获取歌曲代码和名字
def get_code_name(index_html):
    index_html = etree.HTML(index_html)
    # 获取歌曲id
    song_id = index_html.xpath('//li[@class="mItem"]/span[@class="title"]/a/@sid')
    # 获取歌曲名称
    song_name = index_html.xpath('//li[@class="mItem"]/span[@class="title"]/a/@title')
    # 获取作者
    # artists = index_html.xpath('//ul[@id="musicList"]//span[@class="artistName"]/a/@title')
    return song_id, song_name


# print(get_code_name(get_index(url, params)))


# 请求并下载歌曲
def get_song(song_id, song_name):
    # http://f2.htqyy.com/play8/33/mp3/3
    song_url = 'http://f2.htqyy.com/play8/{}/mp3/3'.format(song_id)
    song_data = requests.get(url=song_url, headers=headers, timeout=5).content
    song_path = 'E:/audio/htqyy_hot/demo/' + song_name + '.mp3'
    with open(song_path, 'wb') as f:
        f.write(song_data)
        print(song_name, "\t下载成功！！！")


error_song = []


def main():
    for i in range(24):
        # 数据
        params = {
            'pageIndex': '{}'.format(i),
            'pageSize': '20'
        }
        try:
            index_data = get_index(url, params)
            songs_id, songs_name = get_code_name(index_data)
            for song_id, song_name in zip(songs_id, songs_name):
                try:
                    get_song(song_id, song_name)
                except:
                    error_song.append([song_id, song_name])
        except:
            print(i)


if __name__ == '__main__':
    main()
    print(error_song)
