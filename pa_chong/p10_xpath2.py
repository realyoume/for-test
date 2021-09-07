# 拿页面源代码
# 提取和解析数据

import requests
from lxml import etree
import csv

url = "https://beijing.zbj.com/search/f/?kw=saas"

hea = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"
}

resp = requests.get(url, headers=hea)

resp.encoding = "utf-8"

# print(resp.text)

html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")

f = open("zbj.csv", mode="w", newline="", encoding="utf-8")
csvwriter = csv.writer(f)

for div in divs:
    price = div.xpath('./div/div/a[1]/div[2]/div[1]/span[1]/text()')
    if(len(price) == 0):
        break
    price = price[0].strip("￥")
    title = "assa".join(div.xpath('./div/div/a[1]/div[2]/div[2]/p/text()'))
    com_name = div.xpath('./div/div/a[2]/div[1]/p/text()')[1].strip()
    location = div.xpath('./div/div/a[2]/div[1]/div/span/text()')[0]
    #print(com_name)
    #break
    csvwriter.writerow([price, title, com_name, location])
#/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div[53]/div/div/a[2]/div[1]/p/text()
print('ok')

resp.close()