import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request,urlopen
from selenium import webdriver
from requests.exceptions import ConnectionError
import re
import csv
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def DoRequest(website):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    try:
        urlopen(website)
    except:
        return '0'
    else:
        req = Request(website, headers=headers)
        response = urlopen(req).read()
        soup = BeautifulSoup(response, 'html.parser')
        return soup
    

def news_for_a_day(website_to_day):
    Input = []
    soup = DoRequest(website_to_day)
    arcticle = soup.find('article',{'class':'article'})
    tag = arcticle.get('data-origin-type-name') 
    print(tag)
    if tag =='產經' or tag == '證券':
        title = arcticle.get('data-title')
        print(title)
        url = arcticle.get('data-canonical-url')
        print(url)
        time = arcticle.find('div',{'class':'updatetime'}).span.text
        print(time)
        print(arcticle.find('div',{'class':'paragraph'}))
        p = arcticle.find('div',{'class':'paragraph'}).find_all('p')
        paragraph = ''
        for text in p:
            paragraph += text.text
        print(paragraph)
        Input.append([title,tag,time,url,paragraph])
            
    return Input


if __name__ == '__main__':
    Input = []
    Input.append([['標題','分類','時間','網址','內文']])
    Input.append(news_for_a_day('https://www.cna.com.tw/news/afe/201512130170.aspx'))
    print(Input)
    