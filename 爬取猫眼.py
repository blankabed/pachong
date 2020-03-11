import urllib.request
import ssl
import re
import os
def imagecrawler(url):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

    }
    req=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(req)
    Htmlstr=response.read().decode("utf-8")
    #with open(r"D:\pycharm\p1\爬虫\maoyan.html","wb") as f:
     #  f.write(Htmlstr)
    pat=r'<dd>.*?data-src="(.*?)".*?<a .*?>(.*?)</a>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>'
    re_Info=re.compile(pat,re.S)
    InfoList=re_Info.findall(Htmlstr)
    for item in InfoList:
        yield {
            'image':item[0],
            'name':item[1],
            'score':item[2]+item[3]

        }
def main(offset):
    url="http://maoyan.com/films?offset="+str(offset)
    for item in imagecrawler(url):
        print(item)
if __name__ == '__main__':
    for i in range(10):
        main(i*30)

