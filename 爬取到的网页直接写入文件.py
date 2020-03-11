import urllib.request
urllib.request.urlretrieve("http://www.baidu.com",filename=r"C:\Users\asus\Desktop\python\file1.html")
#urlretrieve在执行的过程中会产生一些缓存
urllib.request.urlcleanup()#清除缓存