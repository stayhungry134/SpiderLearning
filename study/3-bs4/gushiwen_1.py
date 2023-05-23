from gushiwen_cn import AncientPoetry

url = input("请输入网址：")

file_name = input("请输入书名：")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4400.8 Safari/537.36',
}

file_path = './file/{}.txt'.format(file_name)

book = AncientPoetry(url=url, headers=headers, file_path=file_path)

book.main()