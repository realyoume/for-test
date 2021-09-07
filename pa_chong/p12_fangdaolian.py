import requests

url = 'https://www.pearvideo.com/video_1738554'

vedioId = url.split('_')[1]

child_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={vedioId}&mrd=0.8612413762516935'

hea = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    # 防盗链 看看请求的上一级是什么
    'Referer': url
}

resp = requests.get(child_url, headers=hea)

dic = resp.json()

systemTime = dic['systemTime']
srcUrl = dic['videoInfo']['videos']['srcUrl']

srcUrl = srcUrl.replace(systemTime, f'cont-{vedioId}')

# print(srcUrl)

with open('pear.mp4', mode='wb') as f:
    f.write(requests.get(srcUrl).content)

print('ok')

resp.close()