from lxml import etree
import requests

url = 'https://www.xyyuedu.com/gdmz/sidamingzhu/sgyy/21600.html'
resp = requests.get(url)
resp.encoding = 'gb2312'

# print(resp.text)
# obj = re.compile(r'<div id="arcxsbd"><div id="onearcxsbd" class="onearcxsbd">(?P<t>.*?)</p>', re.S)
# result = obj.finditer(resp.text)
# print(result)
# for i in result:
#     print(i.group('t'))
html = etree.HTML(resp.text)
div = html.xpath('//*[@id="onearcxsbd"]')[0]
ps = div.xpath('./p')
for p in ps:
    txt = p.xpath('./text()')[0].replace('\r\n\t', '')
    print(txt, end='')

resp.close()
