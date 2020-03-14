import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request,urlopen
import re
import csv

def DoRequest(website):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = Request(website, headers=headers)
    response = urlopen(req).read()
    soup = BeautifulSoup(response, 'html.parser')
    return soup

def Scrap(website):
    soup = DoRequest(website)
    return soup

if __name__ == '__main__':
    Input = ['標題','時間','內文']
    for page in range(1,5044):#最多5044
        soup  = Scrap('https://blog.moneydj.com/news/page/'+str(page)+'/')
        getAllNew = soup.find_all('article')#瀏覽：article是內文每條新聞，輸出為list
        print('這是第'+str(page)+'頁：')
        print('')
        for web in getAllNew:
            #print(web.div.header.h3.a.text)#瀏覽：標題
            #print(web.figure.a.get("href"))#瀏覽：網址
            #print('')
            theWeb  = Scrap(web.figure.a.get("href"))#新聞頁
            #print(theWeb.find('article').header.h1.text)#新聞：標題
            #print(theWeb.find('span',{'class':'entry-meta-date updated'}).text)#新聞：時間
            context = theWeb.find('div',{'class':'entry-content mh-clearfix'})#新聞：內文
            #print(context.text)
            #print('')
            Input.append([theWeb.find('article').header.h1.text,theWeb.find('span',{'class':'entry-meta-date updated'}).text,context.text])
        print(len(getAllNew))

    with open('csvNEWSmoneydj.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(Input)