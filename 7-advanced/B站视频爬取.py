# 导入模块
import requests
from lxml import etree
import os
import re

url = 'https://www.bilibili.com/video/BV1Zy4y1K7SH?p=15'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'cookie': 'b_ut=-1; i-wanna-go-back=-1; _uuid=02E822AC-236C-D1B9-E06F-B571D0F2896517754infoc; CURRENT_BLACKGAP=0; buvid3=33D0ADF5-5B8C-4D0D-AFE9-E72766481E5D167642infoc; fingerprint=6e10f21b5ce8c8f71873ee229e489979; buvid_fp=33D0ADF5-5B8C-4D0D-AFE9-E72766481E5D167642infoc; buvid_fp_plain=33D0ADF5-5B8C-4D0D-AFE9-E72766481E5D167642infoc; SESSDATA=4f618192%2C1646137861%2C17954%2A91; bili_jct=891e699c797d679ad48d3d3b651d8901; DedeUserID=472410137; DedeUserID__ckMd5=8821f17a497b0a0f; sid=a9k60wrj; blackside_state=1; rpdid=|(u))YJmu)kY0J\'uYJ|~YYY~R; bp_video_offset_472410137=581043405108490466; innersign=1; CURRENT_FNVAL=976; LIVE_BUVID=AUTO3316341249649196; PVID=2; bfe_id=6f285c892d9d3c1f8f020adad8bed553',
    'Referer': 'https://www.bilibili.com/'
}

response = requests.get(url, headers=headers).content.decode('utf-8')

# 视频名称
video_name = re.findall(r'"page":{},"from":"vupload","part":"(.*?)"'.format(15), response)[0]

html = etree.HTML(response)
# 提取 视频 音频 url
url_str = html.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
print(url_str)
video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)
audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)",', url_str)

print(video_url)


# # 改变工作目录
# os.chdir('D:/Programma/Python/file/videos')
# # 合成视频
# os.system('ffmpeg -i "114_1.mp3" -i "114_2.mp4" -c copy "114.mp4"')
