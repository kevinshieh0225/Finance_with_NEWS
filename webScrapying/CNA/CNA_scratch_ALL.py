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
    reset = 0 # 0 是沒吃到，1 是吃到
    counts = 0
    for i in range(800):
        if i < 10:
            soup = DoRequest(website_to_day+'000'+str(i)+'.aspx')
        elif i > 9 and i < 100 :
            soup = DoRequest(website_to_day+'00'+str(i)+'.aspx')
        else:
            soup = DoRequest(website_to_day+'0'+str(i)+'.aspx')
        if soup == '0':
            if reset == 0:
                counts += 1
            else:
                counts,reset = 1,0
            if counts > 15:
                print('斷在第'+str(i)+'個新聞')
                break
            continue
        counts,reset = 0,1
        #print(str(i))
        arcticle = soup.find('article',{'class':'article'})
        tag = arcticle.get('data-origin-type-name') 
        #print(tag)
        if tag =='產經' or tag == '證券':
            title = arcticle.get('data-title')
            url = arcticle.get('data-canonical-url')
            time = arcticle.find('div',{'class':'updatetime'}).span.text
            p = arcticle.find('div',{'class':'paragraph'}).find_all('p')
            paragraph = ''
            for text in p:
                paragraph += text.text

            Input.append([title,tag,time,url,paragraph])
            
    return Input


if __name__ == '__main__':
    start_date = date(2020, 1, 1)
    end_date = date(2020, 3, 17)
    for single_date in daterange(start_date, end_date):
        print(single_date.strftime("%Y%m%d"))
        Input = []
        Input.append([['標題','分類','時間','網址','內文']])
        Input.append(news_for_a_day('https://www.cna.com.tw/news/afe/'+str(single_date.strftime("%Y%m%d"))))
        year , month , day = single_date.strftime("%Y") , single_date.strftime("%m") , single_date.strftime("%d")
        with open('./DATA/'+str(year)+'/'+str(year)+'_'+str(month)+'/'+str(year)+str(month)+str(day)+'.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(Input)):
                writer.writerows(Input[i])

    