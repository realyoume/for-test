from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys

web = Chrome()

web.get('http://lagou.com')

# 找到元素并点击
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()

time.sleep(2)

# 找到输入框，输入python  -->  点击回车或者搜索
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(5)

web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[3]/div[1]/div[1]/div[1]/a/h3').click()

time.sleep(2)
# 转换到新窗口
web.switch_to.window(web.window_handles[-1])

time.sleep(2)
detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text

print(detail)

# 关闭当前窗口
web.close()  
# 转换到原来的窗口
web.switch_to.window(web.window_handles[0])  

print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[3]/div[1]/div[1]/div[1]/a/h3').text)

