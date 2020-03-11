import urllib.request
import random
url=r"http://www.baidu.com"
'''
#模拟请求头
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
#设置一个请求体
req=urllib.request.Request(url,headers=header)
#发起请求
response=urllib.request.urlopen(req)
data=response.read().decode("utf-8")
print(data)'''
agentlist=[
    "User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
]#每次换一个agent
agentstr=random.choice(agentlist)
req=urllib.request.Request(url)
#向请求体里添加了user agent
req.add_header("User-Agent",agentstr)
response=urllib.request.urlopen(req)
data=response.read().decode("utf-8")
print(data)
