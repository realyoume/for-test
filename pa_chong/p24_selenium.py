# selenium  可见即可得
# 像人一样打开浏览器 
# chromedriver

from selenium.webdriver import Chrome

web = Chrome()

web.get('http://www.baidu.com')

print(web.title)