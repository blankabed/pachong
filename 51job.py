from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import re
import pymongo
from bs4 import BeautifulSoup
j=0
k=0
info={
    '职位名':'',
    '公司名':'',
}
two_info={
    '工作地点': '',
    '薪资': ''
}
new_info={

}
new_twoinfo={

}
def get_oneurl():
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get("https://mkt.51job.com/tg/sem/pz_2018.html?from=baidupz")
    input = browser.find_element_by_id("kwdselectid")
    input.send_keys("python web")
    input.send_keys(Keys.ENTER)
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#kwdselectid')))
    one_url=browser.current_url
    browser.close()
    return one_url
def get_twourl(url):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html=response.text.encode(response.encoding).decode('gb2312','ignore')
            soup=BeautifulSoup(html,'lxml')
            tag=soup.find_all('div',{'class':"p_in"})
            two_url=re.findall(r'<.*?class="bk".*?"(.*?)"',str(tag))[1]
            return two_url
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_twourl()
# one_url=get_oneurl()
def get_info(url,i):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html=response.text.encode(response.encoding).decode('gb2312','ignore')
            soup=BeautifulSoup(html,'lxml')
            tag1=soup.find_all('div',{'class':"el"})
            try:
                info['职位名']=re.findall(r'.*?target="_blank".*?title="(.*?)"',str(tag1))[i]
                info['公司名'] = re.findall(r'.*?target="_blank".*?title="(.*?)"', str(tag1))[i+1]
            except:
                get_info(url,i+1)
            return info
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_info(url,i)
def get_twoinfo(url,j):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html=response.text.encode(response.encoding).decode('gb2312','ignore')
            soup=BeautifulSoup(html,'lxml')
            tag1=soup.find_all('div',{'class':"el"})
            try:
                two_info['工作地点']=re.findall(r'<span .*?class="t3">(.*?)</span>', str(tag1))[j+1]
                two_info['薪资'] = re.findall(r'<span .*?class="t4">(.*?)</span>', str(tag1))[j+1]
            except:
                get_twoinfo(url,j+1)
            return two_info
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_twoinfo(url,j)
def create_db(i):
    client = pymongo.MongoClient('localhost', 27017)
    db=client.mydb
    my_set=db.test_set
    my_set.insert({'id':i,'职位名':new_info['职位名'],'公司名':new_info['公司名'],
                   '工作地点':'','薪资':''})
def update_db(i):
    client = pymongo.MongoClient('localhost', 27017)
    db=client.mydb
    my_set=db.test_set
    my_set.update({"id":i},{'$set':{ '工作地点':new_twoinfo['工作地点']}} )
    my_set.update({"id": i}, {'$set': {'薪资': new_twoinfo['薪资']}})
two_url=get_twourl("https://search.51job.com/list/000000,000000,0000,00,9,99,"
                   "python%2520web,2,1.html?lang=c&stype=&postchannel=0000&workyear"
                   "=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary"
                   "=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid"
                   "=0&address=&line=&specialarea=00&from=&welfare=")
for i in range(1,6):
    url=("https://search.51job.com/list/000000,000000,0000,00,9,99,"
                   "python%2520web,2,"+str(i)+".html?lang=c&stype=&postchannel=0000&workyear"
                   "=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary"
                   "=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid"
                   "=0&address=&line=&specialarea=00&from=&welfare=")

    for i in range(0,100,2):
        new_info = get_info(url,i)
        create_db(j)
        j+=1
    for i in range(50):
        new_twoinfo = get_twoinfo(url,i)
        print(new_twoinfo['工作地点'])
        update_db(k)
        k+=1





