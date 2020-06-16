#!/usr/bin/env python3
from regular_expression import daterange , getParagragh 
import re
import csv
from datetime import timedelta, date
from bert_serving.client import BertClient
import json
import numpy as np
import os.path

def pythex(datalist):
    filelist = []
    regex = "（中央社.+?）"
    kill_Punctuation = """＂＃＄＆＇（）＊＋－／＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟﹏"""
    re_punctuation = "[{}]+".format(kill_Punctuation)
    split_sentence = """！？｡。，：；…"""
    re_split_sentence = "[{}]+".format(split_sentence)

    for news in datalist:

        topic = re.sub(re_punctuation,"",news[0])
        topic = re.sub(re_split_sentence,"",topic)
        topic = re.sub("[\s]","",topic)
        
        filelist.append(topic)

    return filelist

if __name__ == '__main__':
    start_date = date(2014, 3, 11)
    end_date = date(2020, 3, 17)

    path = './save_topic_training_data.npy'
    try:
        y = np.load(path).item()
    except:
        y = {}
    date_catch = '03'
    for single_date in daterange(start_date, end_date):
        year , month , day = str(single_date.strftime("%Y")) , str(single_date.strftime("%m")) , str(single_date.strftime("%d"))
        print(year+month+day)
        if str(year+month+day) in y:
            print('we have '+year+month+day)
            continue
        try:
            locate = './../../webScrapying/CNA/DATA/'+year+'/'+year+'_'+month+'/'+year+month+day+'.csv'
            datalist = getParagragh(locate)
        except:
            continue
        
        chunhua = int(single_date.strftime("%Y")) - 1911
        topic = pythex( datalist ) 
        #Regular expression的部分
        #bert轉譯
        filelist = []
        bc = BertClient()
        i = 0
        
        for article in topic:
            if i == 0 :
                i += 1
                continue

            topic_bert = bc.encode([article])
            try:
                filelist = np.append(filelist,topic_bert,axis=0)
            except:
                filelist = topic_bert

        save = {year+month+day:filelist}


        dict.update(y,save)
        if date_catch != month:
            date_catch = month
            print('save a month')
            np.save(path,y) #save the new
        

        
