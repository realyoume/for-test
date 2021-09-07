from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# https://www.bilibili.com/video/BV1i54y1h75W?p=95&spm_id_from=pageDriver
# 用超级鹰处理验证吗


# 影藏自己是自动执行程序
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)

  
# 精确有偏移量的点击
# ActionChains(web).move_to_element_with_offset('xpath', x, y).click().perform()


# 拖拽按钮
# ActionChains(web).drag_and_drop_by_offset(button, x, y).perform()