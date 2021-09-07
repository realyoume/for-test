# 从url登录拿到cookie
# 带着cookie登录到书架url,拿到书架信息

# session,一连串的请求，过程中cookie不会丢失

import requests

# 会话 多次对话   
session = requests.session()

url1 = 'https://passport.17k.com/ck/user/login'

data = {
    'loginName': '19936092336',
    'password': 'yumi020401'
}

# 登录
session.post(url1, data=data)

# print(resp.text)

url2 = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'

resp = session.get(url2)

print(resp.json())

resp.close()