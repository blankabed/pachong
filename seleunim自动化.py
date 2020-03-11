from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from selenium.webdriver.chrome.options import Options#不弹窗
from pyquery import PyQuery as pq
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 驱动路径
path = 'D:\谷歌下载\chromedriver_win32 (1)/chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
try:
    browser.get("https://www.baidu.com")
    input=browser.find_element_by_id("kw")
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.wrap > div > div.dist > div.page > span > i > span > input.textbox-text.textbox-text-readonly.validatebox-text')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

