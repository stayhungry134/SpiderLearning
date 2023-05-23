"""
name: base
create_time: 2023/5/22
author: Ethan

Description: 
"""
import json

import requests
from lxml import etree
import subprocess
from functools import partial
# 这样设置之后导入 execjs 才能正确执行
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

from datas.global_data import chrome_agent
from config import *


def parse_data(data):
    """解析数据"""
    import execjs
    with open('bays4.js', 'r', encoding='utf-8') as f:
        shell = f.read()
    return execjs.compile(shell).call('kmno4_decode', data)


class ShanBay:
    """扇贝单词"""

    def __init__(self):
        self.url = 'https://www.shanbay.com/'
        self.total = 50
        self.current = 0
        self.headers = {
        'Cookie': COOKIES,
        'Origin': 'https://web.shanbay.com',
        'Referer': 'https://web.shanbay.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Csrftoken': 'd86328f526f64d3f382cc651cc9a4ef5'
        }

    def get_cookies(self):
        pass

    def get_data(self, page=1):
        """获取数据"""
        url = f'https://apiv3.shanbay.com/wordsapp/user_material_books/buqwfz/learning/words/today_learning_items?ipp=10&page={page}&type_of=NEW'
        response = requests.get(url, headers=self.headers)
        words_data = response.json().get('data')
        return parse_data(words_data)

    def extract_word(self, page=1):
        """提取单词"""
        words_json = json.loads(self.get_data(page))
        words = words_json.get('objects')
        self.total = words_json.get('total')
        self.current += 10
        words_list = [word_item['vocab_with_senses'] for word_item in words]
        words_dic = {word_item['word']: {'word': word_item['word'],
                                         'definition': [f"{definition['pos']} {definition['definition_cn']}" for definition in word_item['senses']],
                                         'uk_sound': word_item['sound']['audio_uk_urls'][0],
                                         'us_sound': word_item['sound']['audio_us_urls'][0],}
                     for word_item in words_list}
        return words_dic

    def get_word(self):
        """获取单词"""
        words_dic = {}
        while self.total > self.current:
            words_dic.update(self.extract_word(page=self.current//10 + 1))
        return words_dic


my_shanbay = ShanBay()
print(my_shanbay.get_data())
# print(my_shanbay.get_word())