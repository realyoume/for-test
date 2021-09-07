# 1.拿到主页面源代码，提取到子页面的链接，herf
# 2.通过herf进入子页面，找到图片的链接
# 3.下载图片

import requests
from bs4 import BeautifulSoup
import time

url = 'https://umei.cc/bizhitupian/'

resp = requests.get(url)

resp.encoding = 'utf-8'

main_page = BeautifulSoup(resp.text, "html.parser")

alist = main_page.find("div", class_="TypeList").find_all("a")

herf_list = []

for a in alist:
    herf = 'https://umei.cc/' + a.get("href")
    herf_list.append(herf) 

img_list = []

for h in herf_list:
    child_resp = requests.get(h)
    child_resp.encoding = 'utf-8'
    child_resp_text = child_resp.text

    child_page = BeautifulSoup(child_resp_text, 'html.parser')
    p = child_page.find('p', align="center")
    img = p.find('img')

    img_list.append(img.get('src'))

    child_resp.close()
    time.sleep(1)

for i in img_list:
    img_resp = requests.get(i)

    img_name = i.split("/")[-1]
    with open(img_name, mode="wb") as f:
        f.write(img_resp.content)

    img_resp.close()
    time.sleep(2)
    break

resp.close()