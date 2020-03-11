import lxml
import pymongo
import requests
import os
from bs4 import BeautifulSoup
import re

client = pymongo.MongoClient('localhost', 27017)
people_info = client['people_info']
info_table = people_info['info_table']
url="http://zj.people.com.cn/GB/186938/186954/index.html"
base_url="http://zj.people.com.cn"
list=[]
list2=[]
content3=[]
dic={
    'title':'',
    'content':''
}
def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html=response.text.encode(response.encoding).decode('gb2312','ignore')
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def get_news_html(url):
    try:
        html=get_html(url)
        soup=BeautifulSoup(html,'lxml')
        link_url=soup.find_all('a')
        for i in link_url:
            try:
                href=i.attrs["href"]
                list.append(re.findall(r"^[/n2].*?[html]$", href)[0])
            except:
                continue
    except:
        return False
def main():
    get_news_html(url)
    for i in list:
        list2=[]
        true_url=base_url+i
        html1=get_html(true_url)
        soup=BeautifulSoup(html1,'lxml')
        con=soup.find('div',{'class':"clearfix w1000_320 text_title"})
        if con==None:
            return False
        else:
            content = re.findall(r"h1>(.*?)</h1>", str(con))[0]
            title=content
            dic['title']=title
            con2 = soup.find_all('p', attrs={'style': 'text-indent: 2em;'})
            for i in con2:
                global content3
                content2 = re.findall(r"<p.*?>(.*?)</p>$", str(i),re.S)
                content4=content3+content2
                content3=content4
            content5=''.join(content4).replace('\n','').replace('\t','')
            dic['content']=content5
        info_table.insert_one({'标题':dic['title'],'内容':dic['content']})


main()



