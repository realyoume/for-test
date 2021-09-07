import requests
import re
import csv

# url = 'http://movie.douban.com/top250'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71"
#     #"Cookie": 'll="118159"; bid=IeMMOeRa158; __yadk_uid=RfFRHOapwEwwFd5AdGT8kFMBMIBX16Yb; douban-fav-remind=1; gr_user_id=d4ef6ca7-9174-42d6-8c41-872fb84047cb; viewed="1670376_19940743"; _vwo_uuid_v2=DE198046D784E342E99B0A53DC1FBC0DF|09c62dbe304f15c6ffa87e605fc6abb0; _vwo_uuid_v2=DE198046D784E342E99B0A53DC1FBC0DF|09c62dbe304f15c6ffa87e605fc6abb0; cto_bundle=lggci19tRElxVXV4JTJCU1hraVFNWGlvNDlmJTJGbEtkcGtJSGhqUkpxNHpKSHYzVDU3eGtLQiUyQk9oTks0VG1iWUZXWW80YXI4WkljQnpzV1hvSXlEN0YzR1pLaERSWFpIJTJGZlQyZXZmeG9Uc2xHcWFqT1hCMlBaeVYlMkY3ZjRpakw3eVZOdjlYbmpzTk5PWFpiMnhTTjFKMm9KRW9jeTl3JTNEJTNE; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1627548394%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1644701199.1600873785.1627539021.1627548394.20; __utmz=30149280.1627548394.20.17.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1627548394.12.11.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=223695111.0.10.1627548394; __utma=223695111.497009772.1600873785.1627539021.1627548394.12; dbcl2="243070803:xQ1/xbzYwGk"; ck=utN2; __gads=ID=1fd96c64cce6d531-225817e350c400db:T=1603287990:S=ALNI_MaYJqqEiphSw6EyE1fXW2CdxCu0pg; push_noty_num=0; push_doumail_num=0; __utmt=1; __utmv=30149280.24307; __utmb=30149280.30.10.1627548394; _pk_id.100001.4cf6=dd48d1f150923ea2.1600873785.12.1627549128.1627539471.'
# }

# resp = requests.get(url=url, headers=headers)

# print(resp.text)

# resp.close()

with open("C:\\Users\\xiang\\Desktop\\data.txt", "r", encoding="utf-8") as f:
    s = f.read()
# print(s)

obj = re.compile(r'<div class="hd">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?average">(?P<value>.*?)</span>.*?<span>(?P<num>.*?)</span>', re.S)
result = obj.finditer(s)

f = open("data.csv", mode="w", newline="", encoding="utf-8")
csvwriter = csv.writer(f)


for i in result:
    # print(i.group("name"), end="   ")
    # print(i.group("year").strip(), end="   ")
    # print(i.group("value") + "分", end="   ")
    # print(i.group("num"))
    dic = i.groupdict()
    dic["year"] = dic["year"].strip()
    csvwriter.writerow(dic.values())

f.close()
print('ok')