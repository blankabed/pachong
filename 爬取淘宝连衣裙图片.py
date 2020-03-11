import urllib.request
import ssl
import re
import os
def imagecrawler(url,topath):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

    }
    req=urllib.request.Request(url,headers=headers)
    context=ssl._create_unverified_context()
    response=urllib.request.urlopen(req,context=context)
    Htmlstr=response.read().decode("utf-8")
    #with open(r"D:\pycharm\p1\爬虫\taobao.html","wb") as f:
     #   f.write(Htmlstr)
    pat=r'"pic_url":"//(.*?)",'
    re_image=re.compile(pat,re.S)
    imagesList=re_image.findall(Htmlstr)
    num=1
    for imageurl in imagesList:
        path=os.path.join(topath,str(num)+".jpg")
        num+=1
        urllib.request.urlretrieve("http://"+imageurl,filename=path)#将图片下载下来



url="https://s.taobao.com/search?spm=a21bo.2017.201856-fline.1.5af911d9Q0nNMV&q=%E8%BF%9E%E8%A1%A3%E8%A3%99&refpid=420460_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f66&sort=default"
topath=r"D:\pycharm\p1\爬虫\image"
imagecrawler(url,topath)

