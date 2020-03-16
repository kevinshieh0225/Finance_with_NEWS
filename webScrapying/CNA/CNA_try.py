import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request,urlopen
from selenium import webdriver
import re
import csv

def click_button(website):
    driver = webdriver.Firefox()
    driver.get(website) 
    button = driver.find_element_by_id('SiteContent_uiViewMoreBtn')
    while(button.get_attribute('style') is not 'none'):
        button.click()
    source = driver.page_source
    return source

def DoRequest(website):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = Request(website, headers=headers)
    response = urlopen(req).read()
    soup = BeautifulSoup(response, 'html.parser')
    return soup

if __name__ == '__main__':
    Input = []
    Input.append(['標題','時間','內文'])
    button = click_button('https://www.cna.com.tw/list/aie.aspx')
    soup = DoRequest('https://www.cna.com.tw/list/aie.aspx')
    mainlist = soup.find('ul',{'id':'myMainList'})
    getAllNew = mainlist.find_all('li')
    for web in getAllNew:
        print(web.a.find('div',{'class':'listInfo'}).h2.text)#瀏覽：標題
        print(web.a.find('div',{'class':'listInfo'}).find('div',{'class':'date'}).text)#瀏覽：發文時間
        print(web.a.get("href"))#瀏覽：網址
        print('')
    print(len(getAllNew))
    