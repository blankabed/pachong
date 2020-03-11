import urllib.request
'''
进行客户端与服务端之间消息传递时使用

GET：通过url网址传递信息的，可以直接在url网址上添加要添加的信息
POST：可以向服务器提交数据，比较流行的饿安全的数据传递
PUT：请求服务器存储一个资源，要指定存储的位置
DELETE：请求服务器删除一个资源
HEAD：请求获取对应的http报头
OPTIONS：可以获取当前url所支持的请求类型


'''
#get请求
'''
把数据拼接到请求路径的后面传递给服务器
优点速度快，不安全，承载的数量小
'''
url="http://www.sunck.wang:8085/sunck"
response=urllib.request.urlopen(url)
data=response.read().decode("utf-8")
print(data)