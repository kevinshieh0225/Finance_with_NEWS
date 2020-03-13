import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request,urlopen
import html5lib
import re

def writeTXT(soup):
    with open("./test.txt","w") as f:
        f.write(str(soup))  

def DoRequest(website):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = Request(website, headers=headers)
    response = urlopen(req).read()
    soup = BeautifulSoup(response, 'html.parser')
    return soup
#Request for the website

def Scrap(website):
    soup = DoRequest(website)
    #writeTXT(soup.prettify)
    #listofhref = []
    """
    findrows_fully = 'href="(https://tw.news.yahoo.com/[^"a-z].+?)"'
    findrows_partly = 'href="(/[^a-z].+?)"'
    """
    """
    listofhref_fully = re.findall(findrows_fully, str(soup))
    listofhref_partly = re.findall(findrows_partly, str(soup))
    return listofhref_fully , listofhref_partly"""

    #getAllNew = soup.find_all('a',{'class':'D(ib) Ov(h) Whs(nw) C($c-fuji-grey-l) C($c-fuji-blue-1-c):h Td(n) Fz(16px) Tov(e) Fw(700)'}) #抓到新聞的table
    getAllNew = soup.find_all('a')
    return getAllNew

if '__main__' == __name__:
    getAllNew  = Scrap('https://tw.news.yahoo.com/finance')
    """
    print('Fully:')
    for href in listofhref_fully:
        print(' '+href)
    print('Partly:')
    for href in listofhref_partly:
        print(' https://tw.news.yahoo.com'+href)
    print('Fully:'+str(len(listofhref_fully))+' partly:'+str(len(listofhref_partly)))
    """
    for web in getAllNew:
        print(web.text)
        print(web.get("href"))
        print('')
    print(len(getAllNew))
