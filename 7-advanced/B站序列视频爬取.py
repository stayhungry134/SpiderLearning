# 导入模块
import requests
from lxml import etree
import os
import re

url = 'https://www.bilibili.com/video/BV1Zy4y1K7SH?p=15'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Referer': 'https://www.bilibili.com/'
}

response = requests.get(url, headers=headers).content.decode('utf-8')

# 视频名称
video_name = re.findall(r'"page":{},"from":"vupload","part":"(.*?)"'.format(15), response)[0]

html = etree.HTML(response)
# 提取 视频 音频 url
url_str = html.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]

video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)[0]
audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)[0]

# 爬取视频
video = requests.get(url=video_url, headers=headers).content
audio = requests.get(url=audio_url, headers=headers).content

# 存储视频
with open('E:/video/bilibili/tem.mp3', 'wb') as f:
    f.write(audio)

with open('E:/video/bilibili/tem.mp4', 'wb') as f:
    f.write(video)

# 改变工作目录
os.chdir('E:/video/bilibili')
# 合成视频
os.system('ffmpeg -i "tem.mp3" -i "tem.mp4" -c copy "{}.mp4"'.format(video_name))
os.remove('tem.mp3')
os.remove('tem.mp4')
