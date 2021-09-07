# 无头浏览器 使用selenium时 不弹出浏览器窗口

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.options import Options

# 下拉标签 用select包装  
# 对得到的元素进行包装
# sel = Select(sel_el)
# 遍历所有选项
# for i in range(len(sel.options)):
#      sel.select_by_index(i)   按照索引进行查找
#       time.sleep(2)           重新加载，程序暂停一会

# 无头选项参数配置
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable--gpu')

web = Chrome(options=opt)

web.get('http://www.baidu.com')

print(web.page_source)

# 拿到经过数据加载后的页面代码
# web.page_source