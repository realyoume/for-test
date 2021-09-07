from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
import csv

f = open('pyjob.csv', mode='w', encoding='utf-8', newline='')
csvwriter = csv.writer(f)

web = Chrome()

web.get('http://lagou.com')

# 找到元素并点击
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()

time.sleep(2)

# 找到输入框，输入python  -->  点击回车或者搜索
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(2)

lis = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')

for li in lis:
    job_name = li.find_element_by_xpath('./div[1]/div[1]/div[1]/a/h3').text
    location = li.find_element_by_xpath('./div[1]/div[1]/div[1]/a/span/em').text
    money = li.find_element_by_xpath('./div[1]/div[1]/div[2]/div/span').text
    company = li.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
    csvwriter.writerow([job_name, location, money, company])
    # break
    
print('ok')