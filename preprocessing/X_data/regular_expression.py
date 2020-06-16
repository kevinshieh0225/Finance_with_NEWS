#!/usr/bin/env python3
import re
import csv
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def getParagragh(csvfile):
    
    with open(csvfile, newline='') as csvf:
        datalist = list(csv.reader(csvf, delimiter = ','))
    return datalist
def pythex(datalist,time):
    filelist = []
    regex = "[（\(]中央社.+?[）\)]"
    kill_Punctuation = """＂＃＄＆＇（）＊＋－／＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟﹏"""
    re_punctuation = "[{}]+".format(kill_Punctuation)
    split_sentence = """！？｡。，：；…"""
    re_split_sentence = "[{}]+".format(split_sentence)

    for news in datalist:
        context = re.sub(regex,"",news[4])
        context = re.sub("[（\(]\S\S[：:]\S\S\S[）\)]","",context)
        context = re.sub(time,"",context)
        context = re.sub(re_punctuation,"",context)
        context = re.sub(re_split_sentence," ",context).split()

        topic = re.sub(re_punctuation,"",news[0])
        topic = re.sub(re_split_sentence,"",topic)
        topic = re.sub("[\s]","",topic)
        
        filelist.append([topic,news[2],context])

    return filelist

if __name__ == '__main__':
    start_date = date(2016, 3,1)
    end_date = date(2020, 3, 11)
    for single_date in daterange(start_date, end_date):
        print(single_date.strftime("%Y%m%d"))
        year , month , day = str(single_date.strftime("%Y")) , str(single_date.strftime("%m")) , str(single_date.strftime("%d"))
        filelist = []
        locate = './../../webScrapying/CNA/DATA/'+year+'/'+year+'_'+month+'/'+year+month+day+'.csv'
        datalist = getParagragh(locate)
        context = pythex(datalist)
        with open('./regularEx_file/'+year+'/'+year+month+day+'.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(len(context)):
                writer.writerows(context[i])
