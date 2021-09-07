from urllib.request import urlopen

url = "http://www.bing.com"
respon = urlopen(url)
#print(respon.read().decode("utf-8"))

with open("mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(respon.read().decode("utf-8"))
print("ok")
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests