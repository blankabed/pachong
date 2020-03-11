import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
browser=webdriver.Chrome()
wait=WebDriverWait(browser, 10)
newurl=[]
headers={

        "Referer": "http://www.cpppc.org:8086/pppcentral/map/toPPPPotentialList.do",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

    }
data={
    "queryPage": "1",
    "distStr": "",
    "induStr":"" ,
    "investStr":"",
    "publTimeStr":"",
    "projName":"" ,
    "sortby": "",
    "orderby": "",
    "stageArr": "",
    "projStateType": "2"
}
dic={
    "money":"",
    "time":""
}
def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False,headers=headers,data=data)
        if response.status_code==200:
            html=response.json()
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def get_json():
    json=get_html("http://www.cpppc.org:8086/pppcentral/map/getPPPList.do")
    return json
def new_url():
    json=get_json()
    url=re.findall(r".*? 'PROJ_RID': '(.*?)'.*?",str(json))
    for i in url:
        newurl.append("http://www.cpppc.org:8083/efmisweb/ppp/projectLibrary/getProjInfoNational.do?projId="+str(i))
    return newurl
def get_data():
    url2=new_url()
    for i in url2:
        try:
            response = requests.get(i, allow_redirects=False)
            if response.status_code == 200:
                html = response.text.encode(response.encoding).decode('utf-8','ignore')
                dic["money"]=re.findall(r'.*?text-align: left">\s+(.*?)[\u4e00-\u9fa5][\u4e00-\u9fa5].*?',html)[0]
                dic["time"]=re.findall(r'.*?text-align: left">(\d{4})-(\d{2})-(\d{2})</td>',html)
                print(dic)
            if response.status_code == 302:
                print('302')
        except ConnectionError:
            return get_html(i)
def updata():
    browser.get("http://www.cpppc.org:8086/pppcentral/map/toPPPPotentialList.do")
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.wrap > div > div.dist > div.page > div > a:nth-child(7)')))
    submit.click()
def main():
    get_data()
    for i in range(625):
        updata()
        get_data()
main()