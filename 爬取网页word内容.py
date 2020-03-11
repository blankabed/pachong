import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            html = response.text.encode(response.encoding).decode('gb2312', 'ignore')
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
content=get_html("https://wenku.baidu.com/view/93062fbff71fb7360b4c2e3f5727a5e9846a275a.html")
# soup=BeautifulSoup(content,"lxml")
# html=soup.find_all('div',{'class':"ie-fix"})
print(content)