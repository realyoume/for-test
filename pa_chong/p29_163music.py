from selenium.webdriver import Chrome
import time

# 搜索条件 东西填在下面
name = '香格里拉'

url = f'https://music.163.com/#/search/m/?s={name}&type=1'

web = Chrome()

web.get(url)
time.sleep(3)

# 找到内置框架
f1 = web.find_element_by_xpath('//*[@id="g_iframe"]')

web.switch_to_frame(f1)

time.sleep(2)

web.find_elements_by_xpath('//*[@class="s-fc7"]')[0].click()

time.sleep(3)

web.switch_to.default_content()  # 返回默认窗口

f2 = web.find_element_by_xpath('//*[@id="g_iframe"]')

web.switch_to_frame(f2)

time.sleep(2)

comments = web.find_elements_by_xpath('//*[@class="cmmts j-flag"]/div')

i = 1
for c in comments:
    if(i > 15):
        break
    # print(c.find_element_by_xpath('./div[2]').text.strip('|回复'))  # 打印全部信息
    txt = c.find_element_by_xpath('./div[2]/div[1]/div').text.split('：', 1)[1]   # 仅打印文本
    print(i)
    print(txt)  # 文本
    # print(c.find_element_by_xpath('./div[2]/div[2]/div').text)
    i = i + 1