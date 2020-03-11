import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re
from bs4 import BeautifulSoup
browser=webdriver.Chrome()
wait=WebDriverWait(browser, 10)
#headers={
#        "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
 #   }
def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html = response.text.encode(response.encoding).decode('utf-8', 'ignore')
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def get_location():
    html = get_html("http://carrefour.com.cn/Store/Store.aspx")
    soup=BeautifulSoup(html,"lxml")
    location=soup.find_all("dd")
    new_location=re.findall(r"<a.*?>(.*?)</a>",str(location[0]))
    print(new_location)
def main():
    list=get_location()
    browser.get("http://carrefour.com.cn/Store/Store.aspx")
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#sale_lists > div.sale_lists_head.clearfix > div > dl > dt > a"))).click()
    sel=browser.find_elements_by_css_selector("#span_cityname")
    while True:
        if (city for city in sel if "北京" in city.text ):
            for city in sel:
                if "北京"in city.text:
                    city.click()
                    break
                else:continue
            break
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#sale_lists > div.sale_lists_head.clearfix > div > input"))).click()


main()


