# 网站上视频被切片，信息保存在m3u8文件中

import requests
import re

obj = re.compile(r"url: '(?P<m3u8>.*?)',", re.S)
 
url = 'https://91kanju.com/vod-play/54812-1-1.html'

with requests.get(url) as resp:
    # print(resp.text)
    m3u8_url = obj.search(resp.text).group('m3u8')