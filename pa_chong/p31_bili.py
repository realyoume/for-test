from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

sousuo = '黑龙江'

url = 'https://www.baidu.com/'

web = Chrome()

web.get(url)
time.sleep(5)


web.find_element_by_xpath('//*[@id="kw"]').send_keys(sousuo, Keys.ENTER)

deng = input()