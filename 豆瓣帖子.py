import requests
import pymysql
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import random

headers={

        "Referer": "http://www.cpppc.org:8086/pppcentral/map/toPPPPotentialList.do",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

    }
browser=webdriver.Chrome()
wait=WebDriverWait(browser, 20)
name=[]
user=['yonghu1','yonghu2','yonghu3','yonghu4','yonghu5']
kind=[]
dictinfo={

    '名字':'',
    '创建时间':'',
    '用户':'',
    '类别':'',
    '帖子图片':'',
    '帖子简介':'',
    '帖子正文':'',
    '是否推荐':'',
          }


def get_url(i):
    browser.get("https://www.douban.com/")
    input = browser.find_element_by_name("q")
    input.send_keys(i)
    input.send_keys(Keys.ENTER)

def get_newurl():
    # print(browser.page_source)
    soup = BeautifulSoup(browser.page_source, "lxml")
    ul=soup.find_all('div',attrs=('class','search-cate'))
    url1=re.findall(r'<a href="(.*?)">',str(ul))[1]
    url="https://www.douban.com/"+str(url1)
    return url
def get_html(url):
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            html = response.text.encode(response.encoding).decode('utf-8','ignore')
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def get_info(html):
    soup = BeautifulSoup(html, 'lxml')
    tag = soup.find_all('span', attrs=('class', 'subject-cast'))
    tag2=soup.find_all('div', attrs=('class', 'title'))
    tag3 = soup.find_all('div', attrs=('class', 'content'))
    tag4=soup.find_all('div', attrs=('class', 'pic'))
    aa=re.findall(r'<span>(.*?)</span>', str(tag2))
    zhengwenurl=re.findall(r'<a class="nbg" href="(.*?)" ', str(tag4))
    for l in range(0, len(aa), 2):
        kind.append((aa[l]))
    bb = re.findall(r'<p>(.*?)</p>', str(tag3))
    for m in range(len(tag)):
        dictinfo['用户'] = user[random.randint(0, 4)]
        dictinfo['类别'] = kind[m].replace('[', '').replace(']', '')
        dictinfo['名字'] = re.findall(r'<span class="subject-cast">原名:(.*?) /', str(tag))[m]
        dictinfo['创建时间'] = re.findall(r'/ (\d+)</span>', str(tag))[m]
        dictinfo['帖子图片'] = re.findall(r'<img src="(.*?)"', str(tag4))[m]

        if m > 2:
            dictinfo['帖子简介'] = ''
            dictinfo['是否推荐'] = '0'
        else:
            dictinfo['帖子简介'] = re.findall(r'<p>(.*?)</p>', str(tag3))[m]
            dictinfo['是否推荐'] = '1'

        save_mysqlinfo()
    for i in range(len(zhengwenurl)):
        response = requests.get(zhengwenurl[i], headers=headers)
        zhengwenhtml = response.text.encode(response.encoding).decode('utf-8', 'ignore')
        soup1 = BeautifulSoup(zhengwenhtml, 'lxml')
        tag5 = soup1.find_all('span', attrs=('class', 'short'))
        zhengwen=re.findall(r'<span class="short">(.*?)</span>', str(tag5))
        content=""
        start=0
        for j in range(len(zhengwen)):
            content=content+" "+(str(j+1)+zhengwen[j])
            start=1
        if start==0:
            dictinfo['帖子正文'] = "暂无正文，敬请期待"
        else:
            if '💞' in content:
                content=content.replace('💞','')

            dictinfo['帖子正文']=content
        print(dictinfo['帖子正文'])
        save_mysqlinfo2(str(i+1))





def save_mysqlinfo():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='admin',
        db='bishe',
        charset='utf8mb4',
    )
    cur = conn.cursor()

    # 插入一条数据
    sql = "INSERT INTO `bisheapp_topic`(t_uid,t_kind,create_time,t_photo,t_content,t_title,t_introduce,recommend) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,[
                str(dictinfo["用户"]),
                str(dictinfo["类别"]),
                str(dictinfo["创建时间"]),
                str(dictinfo["帖子图片"]),
                str(dictinfo["帖子正文"]),
                str(dictinfo["名字"]),
                str(dictinfo["帖子简介"]),
                str(dictinfo["是否推荐"]),])
    conn.commit()
    cur.close()
    conn.close()

def save_mysqlinfo2(i):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='admin',
        db='bishe',
    )
    cur = conn.cursor()

    # 插入一条数据
    sql ="UPDATE bisheapp_topic SET t_content=%s  WHERE id = "+i
    cur.execute(sql,[str(dictinfo["帖子正文"]),])
    conn.commit()
    cur.close()
    conn.close()


def main():
    get_url("帖子")
    url=get_newurl()
    html=get_html(url)
    get_info(html)
    browser.close()
main()
