"""
name: words.py
create_time: 2023-03-18
author: Ethan

Description: 
"""
import datetime
import os
import re
import MySQLdb

my_db = MySQLdb.connect(
    host="stayhungry134.com",
    port=3306,
    user="root",
    password="(Ethan/997813581....",
    database='django_words',
)

cursor = my_db.cursor()


def write_words(word, meaning, init_date, next_date, review_times=None):
    if review_times is None:
        review_times = [False] * 9
    sql = f"INSERT INTO `ebbinghaus_learnwords` (`word`, `meaning`, `init_date`, `next_date`,  `review_times`, ) " \
          f"VALUES " \
          f"('{word}', '{meaning}', {init_date}, '{next_date}, '{next_date}, '{review_times}, ');"
    cursor.execute(sql)
    my_db.commit()


words_path = os.listdir('../0_files/words')
words_path = [item for item in words_path if item.startswith('2023')]

for path in words_path:
    with open(f'../0_files/words/{path}', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word_mean = re.search(r'(\w+),\|\| ?(.*)', line)
            word, meaning = word_mean.group(1), word_mean.group(2)
            init_date = datetime.datetime.strptime(path.split('.')[0], '%Y-%m-%d').date()
            next_date = init_date
            review_times = [False] * 9
            sql = f"INSERT INTO `ebbinghaus_learnwords` (`word`, `meaning`, `init_date`, `next_date`,  `review_times`) " \
                  f"VALUES " \
                  f"('{word}', '{meaning}', '{init_date}', '{next_date}', '{review_times}');"
            cursor.execute(sql)
        my_db.commit()

