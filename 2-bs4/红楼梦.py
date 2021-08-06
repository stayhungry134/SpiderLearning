from gushiwen_cn import AncientPoetry

url = 'https://so.gushiwen.cn/guwen/book_46653FD803893E4F3F8B9229F3CD9433.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
}

file_path = './file/红楼梦.txt'


hong_lou_meng = AncientPoetry(url=url, headers=headers, file_path=file_path)

hong_lou_meng.main()

