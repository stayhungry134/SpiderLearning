"""
name: 回车桌面
create_time: 2023/5/20
author: Ethan

Description: 
"""
from base_class import EnterDesk

spider = EnterDesk(category='search')

print(spider.parsing_page(page='1-13-6-0-0-0/'))

