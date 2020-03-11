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



url="http://ojjx.wzu.edu.cn/default2.aspx"
topath=r"D:\pycharm\p1\爬虫\image"
imagecrawler(url,topath)