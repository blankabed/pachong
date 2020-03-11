import os
import re
from lxml import etree
import requests
import sys
import time
#设置编码
#初始参数
studentnumber = input("请输入学号")
password = input("请输入密码")
#访问教务系统
s = requests.session()
url = "http://ojjx.wzu.edu.cn/default2.aspx"
response = s.get(url)
selector = etree.HTML(response.content)
__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
# 使用xpath获取__VIEWSTATE
#selector = etree.HTML(response.content)

#__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]

#获取验证码并下载到本地
imgUrl = "http://ojjx.wzu.edu.cn/CheckCode.aspx"
imgresponse = s.get(imgUrl, stream=True)
print(s.cookies)
image = imgresponse.content
DstDir = os.getcwd()+"\\"
print("保存验证码到："+DstDir+"code.jpg"+"\n")
try:
    with open(DstDir+"code.jpg" ,"wb") as jpg:
        jpg.write(image)
except IOError:
    print("IO Error\n")
finally:
    jpg.close
#手动输入验证码
code = input("验证码是：")
#构建post数据
RadioButtonList1 = u"学生".encode('gb2312','replace')
data = {
    "RadioButtonList1":RadioButtonList1,
    "__VIEWSTATE":__VIEWSTATE,
    "TextBox1":studentnumber,
    "TextBox2":password,
    "TextBox3":code,
    "Button1":"",
    "lbLanguage":""
    }
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
    }
#登陆教务系统
response1 = s.post(url,data=data,headers=headers)
print('欢迎登录教务系统!')
'''
def getInfo(response,xpath):
    content=response.content.decode('gb2312')
    selector=etree.HTML(content)
    infor = selector.xpath(xpath)[0]
    return infor
# 获取学生基本信息
text = getInfo(response, '//*[@id="xhxm"]/text()')
text = text.replace(" ", "")
studentname=text[5:]
print('姓名'+studentname)
'''
kburl="http://ojjx.wzu.edu.cn/xskbcx.aspx?xh=16219111216&xm=%CA%A9%C6%EC%BF%AD&gnmkdm=N121603"
header={
    "Referer":"http://ojjx.wzu.edu.cn/xs_main.aspx?xh=16219111216",
    "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}
response2 = s.get(kburl,headers=header,allow_redirects=False)
html = response2.text
'''selector=etree.HTML(html)
kburl1=selector.xpath('//a/@href')[0]
kburl2=os.path.join(kburl,kburl1)
print(kburl2)
response3=s.get(kburl2,headers=header)
print(response3)
html1=response3.text
print(html1)'''
selector=etree.HTML(html)
content=selector.xpath('//*[@id="Table1"]/tr/td/text()')
for each in content:
    print(each)
