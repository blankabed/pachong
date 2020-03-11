import requests
from bs4 import BeautifulSoup
import re
import pymongo
url_list=[]
index=1
dict={"公司":"",
      "联系人":"",
      "联系电话":"",
      "传真":"",
      "移动电话":"",
      "QQ":"",
      "邮编":"",
      "公司邮箱":"",
      "公司地址":""
      }
def get_url(url):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html = response.text.encode(response.encoding).decode('utf-8', 'ignore')
            soup=BeautifulSoup(html,"lxml")
            tag = soup.find_all('div', {'class': "company-list"})
            new_url=(re.findall(r'<a class="contact" href="(.*?)"',str(tag)))
            return new_url
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_url(url)
def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html = response.text.encode(response.encoding).decode('utf-8', 'ignore')
            soup = BeautifulSoup(html, 'lxml')
            tag = soup.find_all('div', {'class': "dealAbout"})
            dict["公司"]=re.findall(r'<h1>(.*?)</h1>',str(tag))[0]
            dict["联系人"]=re.findall(r'</strong>(.*?)<br/>',str(tag))[0]
            dict["联系电话"] = re.findall(r'</strong>(.*?)<br/>', str(tag))[1]
            dict["传真"] = re.findall(r'</strong>(.*?)<br/>', str(tag))[2]
            dict["移动电话"] = re.findall(r'</strong>(.*?)<span class="red">', str(tag))[0]
            try:
                dict["QQ"] = re.findall(r'<img alt="(.*?)" border="0"', str(tag))[0]
            except:
                dict["QQ"]=""
            dict["邮编"] = re.findall(r'</strong>(.*?)<br/>', str(tag))[5]
            dict["公司邮箱"]=re.findall(r'</strong>(.*?)<br/>',str(tag))[6]
            dict["公司地址"] = re.findall(r'</strong>(.*?)<br/>', str(tag))[7]
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def create_db(i):
    conn = pymongo.MongoClient('localhost', 27017)
    db=conn.moviedb
    my_set=db.test_set
    my_set.insert({'id':i,'公司':dict['公司'],'联系人':dict['联系人'],
                   '联系电话':dict['联系电话'],'传真':dict['传真'],
                   '移动电话':dict['移动电话'],'QQ':dict['QQ'],
                   '邮编':dict['邮编'],'公司邮箱':dict['公司邮箱'],
                   '公司地址':dict["公司地址"]})
# def update_db(i):
#     client = pymongo.MongoClient('localhost', 27017)
#     db=client.mydb
#     my_set=db.test_set
#     my_set.update({"id":i},{'$set':{ '公司':dict['公司']}} )
#     my_set.update({"id": i}, {'$set': {'联系人': dict['联系人']}})
for i in range(2,975):
    url_list.append("http://www.famens.com/Company/ListP_%E6%B5%99%E6%B1%9F_"+str(i)+".html")
new_url=get_url("http://www.famens.com/Company/ListP_%E6%B5%99%E6%B1%9F.html")
for i in range(10):
    get_html(new_url[i])
    create_db(index)
    index+=1
for i in range(1,4):
    for j in range(0,10):
        get_html(get_url(url_list[i-1])[j])
        create_db(index)
        index+=1