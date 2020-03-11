import lxml
import pymongo
import requests
import os
from bs4 import BeautifulSoup
import re
dic={
    "date":"",
    "rate":"",
    "this":"",
    "before":"",
    "D-value":"",
    "D-value-rate":""

}
list=[]
stockurl="http://quote.eastmoney.com/stocklist.html"
def get_html(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

        }
        response=requests.get(url,allow_redirects=False,headers=headers)
        if response.status_code==200:
            html=response.text.encode(response.encoding).decode('gb2312','ignore')
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def get_data(url):
    html=get_html(url)
    soup=BeautifulSoup(html,'html.parser')
    print(soup)
    data = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})


    print(data)
    if data==None:
        print("无采集到数据")
    data1=soup.find_all('tr',{'class':"odd"})
    if data1==None:
        print("无采集到数据")
    for i in range(1,20):
        if i%2!=0:
            content1 = re.findall(r"<td><span>.*?31'>(.*?)</span>.*?font-weight:normal'>(.*?)</span>"
                                 + r"<td>(.*?)</td><td>(.*?)</td>.*?font-weight:normal'>(.*?)</span>.*?"
                                 + r"font-weight:normal'>(.*?)</span>",str(data))


        else:
            content1 = re.findall(r"<td><span>.*?31'>(.*?)</span>.*?font-weight:normal'>(.*?)</span>"
                                 + r"<td>(.*?)</td><td>(.*?)</td>.*?font-weight:normal'>(.*?)</span>.*?"
                                 + r"font-weight:normal'>(.*?)</span>",str(data1))


    return content1

def get_stockhtml(stockurl):
    try:
        response=requests.get(stockurl,allow_redirects=False)
        if response.status_code==200:
            html1=response.text.encode(response.encoding).decode('gb2312','ignore')
            return html1
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(stockurl)

def getstocklist(html):
    html=get_stockhtml(stockurl)
    soup=BeautifulSoup(html,"lxml")
    a=soup.find_all("a")
    for i in a:
        try:
            href=i.attrs["href"]
            list.append(re.findall(r".*?s[hz](\d{6}).html",href)[0])
        except:
            continue

def main():
    html=get_stockhtml(stockurl)
    getstocklist(html)
    for i in list:
        url="http://data.eastmoney.com/DataCenter_V3/gdhs/GetDetial.ashx?code=600106&js=var%20eVwVBCqO&pagesize=50&page=1&sortRule=-1&sortType=EndDate&param=&rt=51084432"
        content=get_data(url)

        if content==[]:
            continue
        else:
            dic["date"] = content[0]
            dic["rate"] = content[1]
            dic["this"] = content[2]
            dic["before"] = content[3]
            dic["D-value"] = content[4]
            dic["D-value-rate"] = content[5]
    print(dic)
main()

