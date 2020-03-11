import lxml
import pymongo
import requests
import os
from bs4 import BeautifulSoup
import re
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

browser=webdriver.Chrome()
headers={

        "Referer": "http://www.cpppc.org:8086/pppcentral/map/toPPPPotentialList.do",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

    }
data={
    "queryPage": "1",
    "distStr": "",
    "induStr":"" ,
    "investStr":"",
    "publTimeStr":"",
    "projName":"" ,
    "sortby": "",
    "orderby": "",
    "stageArr": "",
    "projStateType": "2"
}
dic={
    "money":"",
    "time":""
}
list1=[]
list2=[]
urllist=[]
wait = WebDriverWait(browser, 10)
def search_url():
    new_url=get_json()
    urllist.append(list['PROJ_RID'],new_url)[0]
    money=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.margin > table > tbody > tr:nth-child(3) > td:nth-child(2)')))
    time=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.margin > table > tbody > tr:nth-child(5) > td:nth-child(2)')))
    return money,time
def search():
    browser.get("http://www.cpppc.org:8086/pppcentral/map/toPPPPotentialList.do")
    submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.wrap > div > div.dist > div.page > div > a:nth-child(7)')))
    submit.click()
def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False,headers=headers,data=data)
        if response.status_code==200:
            html=response.json()
            print(html)
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def get_json():
    html = get_html(
        "http://www.cpppc.org:8086/pppcentral/map/getPPPList.do")
    return html
def get_data():
    list1.append(re.findall(r""))
    dic['money']=dic.get()


def main():
    for i in range(0,625):
        search()
        get_json()
        for i in range(8):
            search_url()
        html=get_json()
if __name__ == '__main__':
    main()







