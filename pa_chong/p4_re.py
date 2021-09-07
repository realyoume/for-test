# coding:utf-8
import re

# findall 匹配所有符合正则表达式的内容，返回列表
#lst = re.findall(r"\d+", "我的电话10012，小胖的电话23942，耗子电话32342")

#print(lst)

# finditer 匹配所有符合正则表达式的内容,返回迭代器，拿取内容用.group
#it = re.finditer(r"\d+", "我的电话10012，小胖的电话23942，耗子电话32342")

#for i in it:
   # print(i.group())


# search 返回match 对象，用.group拿对象
# search 找到一个结果就返回
#s = re.search(r"\d+", "我的电话10012，小胖的电话23942，耗子电话32342")
#print(s.group())


# match 从头开始匹配
#s = re.match(r"\d+", "10012，小胖的电话23942，耗子电话32342")
#print(s.group())


# 预加载正则表达式
# obj = re.compile(r"\d+")
# a = obj.finditer("10012，小胖的电话23942，耗子电话32342")
# for i in a:
#     print(i.group())

s = 'ok1-向可-okok2-小胖-okok3-耗子-okok4-花-ok'

# (?P<命名>正则) 从正则匹配中提取需要的
obj = re.compile(r'ok(?P<id>\d+)-(?P<name>.*?)-ok', re.S)

result = obj.finditer(s)
print(result)
for i in result:
   print(i.group('id'))
   print(i.group('name'))