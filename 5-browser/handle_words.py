"""
name: handle_words.py
create_time: 2023-05-09
author: Ethan White

Description: 
"""
import datetime
import csv
import MySQLdb

# 数据库基本配置
my_db = MySQLdb.connect(
    host="stayhungry134.com",
    port=3306,
    user="root",
    password="(Ethan/997813581....",
    database='django_words',
)

cursor = my_db.cursor()


# 保存单词到数据库
def save_django_words(word, mean, date):
    word = word.replace("'", "\'")
    meaning = mean.replace("'", "\'")
    review_times = [False] * 9
    # 检查记录是否存在
    # cursor.execute(f"SELECT * FROM ebbinghaus_learnwords WHERE word='{word}'")
    # rows = cursor.fetchall()
    # if rows:
    #     return
    sql = f"INSERT INTO `ebbinghaus_learnwords` (`word`, `meaning`, `init_date`, `next_date`,  `review_times`) " \
          f"VALUES " \
          f"('{word}', '{meaning}', '{date}', '{date}', '{review_times}');"
    cursor.execute(sql)


# 读取单词csv文件
def read_csv_words():
    today = datetime.date.today()
    with open('../0_files/words/CET6.csv', 'r', encoding='utf-8') as file:
    # with open('../0_files/words/test.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        num = 0
        for row in reader:
            # 排除表头
            if row[0] == 'word':
                continue
            word = row[0]
            mean = row[1]
            days = num // 30
            date = today + datetime.timedelta(days=days)
            print(word, mean, date)
            save_django_words(word, mean, date)
            num += 1


def main():
    try:
        read_csv_words()
    except:
        my_db.close()
    my_db.commit()
    # 关闭数据库连接
    my_db.close()


if __name__ == '__main__':
    main()