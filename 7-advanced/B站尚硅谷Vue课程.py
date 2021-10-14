# 导入模块
import requests
import os

# https://www.bilibili.com/video/BV1Zy4y1K7SH?p=14&spm_id_from=pageDriver
# 30280，音频链接
url_280 = 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/61/83/373288361/373288361_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1634139061&gen=playurlv2&os=coso1bv&oi=1782178914&trid=57654668cf6b4d9991aaf3fa523cdbc9u&platform=pc&upsig=e4a6af5ce669f2b51c118c4126d4a79a&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=472410137&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000'
# 30080，视频链接
url_80 = 'https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/61/83/373288361/373288361_nb2-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1634139061&gen=playurlv2&os=hwbv&oi=1782178914&trid=57654668cf6b4d9991aaf3fa523cdbc9u&platform=pc&upsig=ec3cd6221d2622371e89f23cd93b8c0d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=472410137&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'cookie': 'b_ut=-1; i-wanna-go-back=-1; _uuid=02E822AC-236C-D1B9-E06F-B571D0F2896517754infoc; CURRENT_BLACKGAP=0; buvid3=33D0ADF5-5B8C-4D0D-AFE9-E72766481E5D167642infoc; fingerprint=6e10f21b5ce8c8f71873ee229e489979; buvid_fp=33D0ADF5-5B8C-4D0D-AFE9-E72766481E5D167642infoc; buvid_fp_plain=33D0ADF5-5B8C-4D0D-AFE9-E72766481E5D167642infoc; SESSDATA=4f618192%2C1646137861%2C17954%2A91; bili_jct=891e699c797d679ad48d3d3b651d8901; DedeUserID=472410137; DedeUserID__ckMd5=8821f17a497b0a0f; sid=a9k60wrj; blackside_state=1; rpdid=|(u))YJmu)kY0J\'uYJ|~YYY~R; bp_video_offset_472410137=581043405108490466; innersign=1; CURRENT_FNVAL=976; LIVE_BUVID=AUTO3316341249649196; PVID=2; bfe_id=6f285c892d9d3c1f8f020adad8bed553',
    'Referer': 'https://www.bilibili.com/'
}

response_280 = requests.get(url=url_280, headers=headers)
response_80 = requests.get(url=url_80, headers=headers)

data_280 = response_280.content
data_80 = response_80.content

with open('D:/Programma/Python/file/videos/114_1.mp3', 'wb') as f:
    f.write(data_280)

with open('D:/Programma/Python/file/videos/114_2.mp4', 'wb') as f:
    f.write(data_80)

# 改变工作目录
os.chdir('D:/Programma/Python/file/videos')
# 合成视频
os.system('ffmpeg -i "114_1.mp3" -i "114_2.mp4" -c copy "114.mp4"')
