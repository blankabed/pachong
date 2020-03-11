import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re
from bs4 import BeautifulSoup
browser=webdriver.Chrome(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
wait=WebDriverWait(browser, 10)
selector="#sjina_C"
selector1="_02 > a"
url4=[]
price=[]
def get_url(url):
    for i in range(20,40):
        browser.get("http://hz.newhouse.fang.com/house/s/?ctm=1.hz.xf_search.list_type.1")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selector+str(i)+selector1))).click()
        normal_window = browser.current_window_handle
        all_Handles = browser.window_handles
        for pay_window in all_Handles:
            if pay_window != normal_window:
                browser.switch_to_window(pay_window)
        soup = BeautifulSoup(browser.page_source, "lxml")
        url1=soup.find("div",id='orginalNaviBox')
        url2=re.findall(r'<a href="(.*?)" id="xf.*?_B03_08" target="_self">楼盘详情</a>',str(url1))
        url3="".join(url2)
        url4.append(url3)
    return url4
def get_html(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            html = response.text.encode(response.encoding).decode('gb2312','ignore')
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def main():
    new_url= get_url("http://hz.newhouse.fang.com/house/s/?ctm=1.hz.xf_search.list_type.1")
    for i in range(len(new_url)):
        try:
            html=get_html(new_url[i])
            soup=BeautifulSoup(html,"lxml")
            lab=soup.find_all('div',attrs=('class','main-info-price'))
            price.append(re.findall(r'<em>\s+(.*?)\s+</em>',str(lab)))
        except:
            continue
    print(price)


main()












