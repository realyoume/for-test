import requests
import re

domain = 'https://www.dy2018.com'

# resp = requests.get(domain, verify=False)
# print(resp.text)

# resp.close()

with open("C:\\Users\\xiang\\Desktop\\dianying.txt", "r", encoding="utf-8") as f:
    s = f.read()

# print(s)

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<li><a href='(?P<html>.*?)' title=", re.S)

result1 = obj1.finditer(s)

for it in result1:
    ul = it.group("ul")

result2 = obj2.finditer(ul)

child_list = []

for it1 in result2:
    child_herf = domain + it1.group("html")
    #print(it1.group("html"))
    child_list.append(child_herf)

for i in child_list:
    print(i)
