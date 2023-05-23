"""
name: 全面屏手机壁纸
create_time: 2023/5/19
author: Ethan

Description: 
"""
import requests
from lxml import etree

url = 'https://m.bcoderss.com/'

# wordpress_logged_in_5ee634311911eb14e008c7dc6aa75229
# stayhungry134%7C1685689453%7CRF3i7BAE6qf8dtagc1u9aqKc1Dkh34hfBtsF54AjMSm%7C60dbb407ab92b340d2be20c8e628cab8cfe97f5dc8479c15b5eacf88668c03da
# stayhungry134%7C1685689453%7CRF3i7BAE6qf8dtagc1u9aqKc1Dkh34hfBtsF54AjMSm%7C60dbb407ab92b340d2be20c8e628cab8cfe97f5dc8479c15b5eacf88668c03da

params = {
    'action': 'is_vip'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Cookie': 'wordpress_5ee634311911eb14e008c7dc6aa75229=stayhungry134%7C1685689453%7CK8DnoCNBFBcd6GLqwmoAHh70RkHg2BsmWV0s6zMGKRQ%7C84eef5bd8aa96b89b7654caa07047c8a1d286754f9bfd1ef6a9324df471ca97a; wordpress_sec_5ee634311911eb14e008c7dc6aa75229=stayhungry134%7C1685689453%7CRF3i7BAE6qf8dtagc1u9aqKc1Dkh34hfBtsF54AjMSm%7C3e5eeb157c478c75731dbc73d7b42382ed72ca079595cea4e2710b6224e9ab65; wordpress_logged_in_5ee634311911eb14e008c7dc6aa75229=stayhungry134%7C1685689453%7CRF3i7BAE6qf8dtagc1u9aqKc1Dkh34hfBtsF54AjMSm%7C60dbb407ab92b340d2be20c8e628cab8cfe97f5dc8479c15b5eacf88668c03da; Hm_lvt_ce3020881c73bb20f0830ef4ed0a61fb=1684295514,1684385921,1684479761; wp-settings-time-56031=1684480388; amp_a0683b=yv9Du7iarQQ2at27PdpNYS.eHU4cnZ5d3E0b3h4Nw==..1h0pd6b2r.1h0pdrjli.0.0.0; Hm_lpvt_ce3020881c73bb20f0830ef4ed0a61fb=1684480577'
}
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)

avatar_url = html.xpath('//div[contains(@class, "user")]//img[2]/@src')[0]

print(avatar_url)