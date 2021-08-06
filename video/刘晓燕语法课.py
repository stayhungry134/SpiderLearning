import requests

#80
url_280 = 'https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/23/77/302717723/302717723-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1621261297&gen=playurlv2&os=kodobv&oi=3084929102&trid=0575549424cc4574b345674e2806c954u&platform=pc&upsig=283f9948479e3035e5b5b88a1786839d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=472410137&orderid=0,3&agrr=0&logo=80000000'
#64
url_80 = 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/23/77/302717723/302717723-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1621261297&gen=playurlv2&os=coso1bv&oi=3084929102&trid=0575549424cc4574b345674e2806c954u&platform=pc&upsig=c4a454b7081611f52e4b0a53b670e175&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=472410137&orderid=0,3&agrr=0&logo=80000000'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Referer': 'https://www.bilibili.com/'
}

response_280 = requests.get(url=url_280, headers=headers)
response_80 = requests.get(url=url_80, headers=headers)

data_280 = response_280.content
data_80 = response_80.content

with open('file/280-.mp4', 'wb') as f:
    f.write(data_280)

with open('file/80-.mp4', 'wb') as f:
    f.write(data_80)