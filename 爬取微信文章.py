import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
base_url= 'http://weixin.sogou.com/weixin?'
header={
'Cookie': 'IPLOC=CN3303; SUID=093A0C3C3020910A000000005B14C010; SUV=1528086548085989; ABTEST=4|1528086552|v1; SNUID=4D3F0939050069CC6425EA5605277DB2; weixinIndexVisited=1; sct=1; JSESSIONID=aaaO3XqAt6aPi7aKr1knw; ppinf=5|1528087407|1529297007|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo5OiVFRSU4MSU5NnxjcnQ6MTA6MTUyODA4NzQwN3xyZWZuaWNrOjk6JUVFJTgxJTk2fHVzZXJpZDo0NDpvOXQybHVQNmtEbGRWRG42NWhMZzdwU3RHamFZQHdlaXhpbi5zb2h1LmNvbXw; pprdig=aPZDhmzLquFRMsZWpQ3U9wv0ehvd4T9ijL3FTaeQ_W2WZcNEiuJ9myxJHPHtjWi_cOiC1hX-c7SzfDZ6c0071940E_e37eSdq8OaJ0KtIHmYbt6GamMRNrY-HBvMBniBNfKLJqkhaewxA_b4g6DMP1SGPlVMjIOVg79UsdCSA0M; sgid=29-35368827-AVsUw29NOgNIfKZxxE0qibI4',
'Host':' weixin.sogou.com',
'Upgrade-Insecure-Requests': '1',
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

}
keyword='风景'
def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False)
        if response.status_code==200:
            return response.text
        if response.status_code==302:
            print('302')


    except ConnectionError:
        return get_html(url)



def get_index(keyword,page):
    data={
        'query':keyword,
        'type':2,
        'page':page
    }
    queries=urlencode(data)
    url=base_url+queries
    html=get_html(url)
    return html

def main():
    for page in range(1,101,):
        html=get_index(keyword,page)
        print(html)

if __name__ == '__main__':
    main()
