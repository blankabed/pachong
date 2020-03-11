import urllib.request
import requests
import ssl
import re
import os
import bs4
from PIL import Image
from bs4 import BeautifulSoup


http://ojjx.wzu.edu.cn/default2.aspx
payload={
'__VIEWSTATE': 'dDwxNTMxMDk5Mzc0Ozs+yQtK1YbYY9vpBrR/vl1f+XLx3Qk=',
'txtUserName': '16219111216',
'Textbox1':'',
'TextBox2': '!980723sqk',
'txtSecretCode': 'nc61',
'RadioButtonList1': '(unable to decode value)',
'Button1':'',
'lbLanguage':'',
'hidPdrs':'',
'hidsc':'',
}

soup=BeautifulSoup(index.content,'lxml')
value1=soup.find('input',id='__VIEWSTATE')['value']

s=requests.Session()
index=s.get(url,headers=headers)
img=s.get(checkcode,stream=True,headers=headers)
with open('checkcode.gif','wb') as f:
    f.write(img.content)
image=Image.open('checkcode.gif')
image.show()
payload['txtUserName']=input("UserName:")
payload['TextBox2']=input("Password:")
payload['txtSecretCode']=input("checkcode:")
#下面的value1和value2都不需要转码，直接post过去即可。在此浪费了好长时间
payload['__VIEWSTATE']=value1
payload['RadioButtonList1']= '%D1%A7%C9%FA'

post1=s.post(url,data=payload,headers=headers)
http://ojjx.wzu.edu.cn/default2.aspx
http://ojjx.wzu.edu.cn/xs_main.aspx?xh=16219111216
CheckCode.aspx
http://ojjx.wzu.edu.cn/xskbcx.aspx?xh=16219111216&xm=%CA%A9%C6%EC%BF%AD&gnmkdm=N121603


<input type="hidden" name="__VIEWSTATE" value="dDwxNTMxMDk5Mzc0Ozs+yQtK1YbYY9vpBrR/vl1f+XLx3Qk=" />


