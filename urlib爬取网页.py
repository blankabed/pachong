import urllib.request
url=r"http://www.baidu.com"
#data=response.read().decode("utf-8")#读取文件全部内容，会把数据赋值给一个字符串变量
#data1=response.readline()#读取一行
#data2=response.readlines()#读取文件全部内容，会把数据赋值给一个列表
#print(data)
#print(response.info())#当前环境相关信息
#print(response.getcode())#返回状态码200是正确的304有缓存404没有发现文件查询或url写错了500服务器内部产生错误500以上一般都是服务器有问题
#print(response.geturl())#当前正在爬取的url地址
newUrl2=urllib.request.quote(url)
print(newUrl2)
newUrl=urllib.request.unquote(newUrl2)
print(newUrl)#解码
response=urllib.request.urlopen(newUrl)
data=response.read().decode("utf-8")
print(data)