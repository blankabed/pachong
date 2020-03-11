import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
import re
browser=webdriver.Chrome()
wait=WebDriverWait(browser, 20)
renum=[]
def get_url(i):
    browser.get("http://sbgg.saic.gov.cn:9080/tmann/annInfoView/homePage.html")
    input = browser.find_element_by_id("annNum")
    input.send_keys(i)
    input.send_keys(Keys.ENTER)
def get_products():
    i=0
    html=browser.page_source
    doc=pq(html)
    page = doc('#pages > table > tbody > tr > td:nth-child(6) > span')
    total = re.findall(r"<span.*?>[\u4e00-\u9fa5]\s+[\u4e00-\u9fa5]\s(.*?)[\u4e00-\u9fa5]</span>", str(page))
    newtotal=total[0]
    while i<=int(newtotal):
        html = browser.page_source
        doc = pq(html)
        evenBj=doc('#annTB > tbody > tr > td:nth-child(5)')
        pat=re.findall(r"<td>(.*?)</td>",str(evenBj))
        for j in pat:
            renum.append(j)
        try:
            submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#pages > table > tbody > tr > td:nth-child(8) > a > span > span.l-btn-icon.pagination-next')))
            submit.click()
        except:
            continue
        i+=1
    print(renum)
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
def get_newurl():
    for i in range(1,16254):
        get_url(i)
        get_products()
get_newurl()