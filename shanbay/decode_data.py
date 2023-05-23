"""
name: decode_data
create_time: 2023/5/22
author: Ethan

Description: 
"""
import json
import subprocess
from functools import partial
# 这样设置之后导入 execjs 才能正确执行
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")


def decode_js(t):
    with open('bays4.js', 'r', encoding='utf-8') as f:
        shell = f.read()
    return execjs.compile(shell).call('kmno4_decode', t)


with open('data.txt', 'r') as f:
    import execjs
    data = f.read()
    print(data)
    print(json.loads(decode_js(data)))