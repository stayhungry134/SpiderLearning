"""
File Name: B站单个视频爬取
Author: Ethan
date: 10/14/2021

Description: 用于爬取 B 站 单个视频（不像学习视频一样有好多集）
"""

# 导入模块
import requests
from lxml import etree
import os
import re

url = input("请输入想要爬取的视频网址:")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Referer': 'https://www.bilibili.com/',
    'cookie': 'b_ut=-1; i-wanna-go-back=-1; _uuid=6A2B3837-1212-8A63-CF6E-FB681474A4AA81724infoc; buvid3=18E88705-72DB-405A-9FA6-63834B69A957167623infoc; fingerprint=96cb9dce79132721f312f52c83b6ef9b; buvid_fp=18E88705-72DB-405A-9FA6-63834B69A957167623infoc; buvid_fp_plain=18E88705-72DB-405A-9FA6-63834B69A957167623infoc; SESSDATA=ba839c9b%2C1646954136%2C09226%2A91; bili_jct=191c97fd218a7a1b7bf86d92b113cab0; DedeUserID=472410137; DedeUserID__ckMd5=8821f17a497b0a0f; sid=jseodwh8; blackside_state=1; rpdid=|(J|)Rmkmu|k0J\'uYJuR|kJmu; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO8916323716089346; CURRENT_QUALITY=80; bp_video_offset_472410137=581305045925505624; CURRENT_FNVAL=976; PVID=2; innersign=1',
    'origin': 'https://search.bilibili.com'
}

response = requests.get(url, headers=headers).content.decode('utf-8')

# 解析网页
html = etree.HTML(response)
# 视频名称
video_name = html.xpath('//h1/span/text()')[0]

# 提取 视频 音频 url
url_str = html.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)[0]
audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)[0]

# 爬取视频
video = requests.get(url=video_url, headers=headers).content
audio = requests.get(url=audio_url, headers=headers).content

# 存储视频
with open('E:/video/bilibili/video.mp4', 'wb') as f:
    f.write(video)

with open('E:/video/bilibili/audio.mp3', 'wb') as f:
    f.write(audio)

# 改变工作目录
os.chdir('E:/video/bilibili')
# 合成视频
os.system('ffmpeg -i "video.mp4" -i "audio.mp3" -c copy "{}.mp4"'.format(video_name))
os.remove('video.mp4')
os.remove('audio.mp3')
