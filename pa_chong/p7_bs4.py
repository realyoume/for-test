import requests
from bs4 import BeautifulSoup
import csv

# url = 'http://whbsz.com.cn/Price.aspx'  

# resp = requests.get(url)

# print(resp.text)

# resp.close()

h = open("cai.csv", mode="w", newline="", encoding="utf-8")
csvwriter = csv.writer(h)


with open("C:\\Users\\xiang\\Desktop\\caijia.txt", "r", encoding="utf-8") as f:
    s = f.read()

page = BeautifulSoup(s, "html.parser")

table = page.find("table")

trs = table.find_all("tr")

for tr in trs:
    tds = tr.find_all("td")

    name = tds[0].text
    high = tds[2].text
    low = tds[3].text
    avg = tds[4].text

    csvwriter.writerow([name, high, low, avg])

h.close()

print('over')

