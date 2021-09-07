import requests

url = 'https://fanyi.baidu.com/sug'

danci = input('输入单词')

data = {
    "kw": danci
}

resp = requests.post(url, data=data)

print(resp.json())

resp.close()