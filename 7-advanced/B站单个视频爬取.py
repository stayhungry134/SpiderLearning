"""
File Name: B站单个视频爬取
Author: Ethan
date: 10/14/2021

Description: 用于爬取 B 站 单个视频（不像学习视频一样有好多集）
"""

# 导入模块
import requests
import re  # 正则表达式
import pprint
import json
import subprocess

url = input("请输入想要爬取的视频网址:")
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "referer": "https://www.bilibili.com/",
}

def send_request(url):
    response = requests.get(url=url, headers=headers)
    return response


def get_video_data(html_data):
    """解析视频数据"""

    # 提取视频的标题
    title = re.findall('<span class="tit">(.*?)</span>', html_data)[0]
    # print(title)

    # 提取视频对应的json数据
    json_data = re.findall('<script>window\.__playinfo__=(.*?)</script>', html_data)[0]
    # print(json_data)  # json_data 字符串
    json_data = json.loads(json_data)
    pprint.pprint(json_data)

    # 提取音频的url地址
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
    print('解析到的音频地址:', audio_url)

    # 提取视频画面的url地址
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    print('解析到的视频地址:', video_url)

    video_data = [title, audio_url, video_url]
    return video_data

# # 改变工作目录
# os.chdir('E:/video/bilibili')
# # 合成视频
# os.system('ffmpeg -i "video.mp4" -i "audio.mp3" -c copy "{}.mp4"'.format(video_name))
# os.remove('video.mp4')
# os.remove('audio.mp3')

def save_data(file_name, audio_url, video_url):
    # 请求数据
    print('正在请求音频数据')
    audio_data = send_request(audio_url).content
    print('正在请求视频数据')
    video_data = send_request(video_url).content
    with open(file_name + '.mp3', mode='wb') as f:
        f.write(audio_data)
        print('正在保存音频数据')
    with open(file_name + '.mp4', mode='wb') as f:
        f.write(video_data)
        print('正在保存视频数据')


def merge_data(video_name):
    print('视频合成开始:', video_name)
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
    COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental output.mp4'
    subprocess.Popen(COMMAND, shell=True)
    print('视频合成结束:', video_name)
