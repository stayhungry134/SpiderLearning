"""
name: temporary
create_time: 2023/5/11
author: stayh

Description: 
"""


# 打开单词文件
with open("../0_files/words/CET6.txt", 'r', encoding='utf-8') as words_file:
    with open("../0_files/words/CET6_group.txt", 'w', encoding='utf-8') as write_file:
        num = 1
        # 将单词写入到文件中
        for word in words_file.readlines():
            # 去除换行符
            word = word.strip()
            write_file.write(word + ', ')
            if num % 30 == 0:
                write_file.write('\n')
            num += 1
