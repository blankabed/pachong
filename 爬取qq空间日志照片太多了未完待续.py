import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
number = input("请输入号码")
pwd = input("请输入密码")
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
headers = {
        "referer": "https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone",
        "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
    }
def get_html(url):
    try:
        response=requests.get(url,allow_redirects=False,headers=headers)
        if response.status_code==200:
            html = response.text.encode(response.encoding).decode('utf-8',)
            return html
        if response.status_code==302:
            print('302')
    except ConnectionError:
        return get_html(url)
def load():
    browser.get("https://qzone.qq.com/")
    browser.switch_to_frame('login_frame')
    load = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#switcher_plogin')))
    load.click()
    inputnumber=browser.find_element_by_id("u")
    inputnumber.send_keys(number)
    inputpwd=browser.find_element_by_id("p")
    inputpwd.send_keys(pwd)
    submit = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#login_button')))
    submit.click()
def main():
    load()
main()