#!/usr/bin/env python3
from regular_expression import daterange , getParagragh , pythex 
import re
import csv
from datetime import timedelta, date
from bert_serving.client import BertClient
import json
import numpy as np
import os.path


if __name__ == '__main__':
    start_date = date(2014, 3, 11)
    end_date = date(2020, 3, 17)

    path = './save_context_training_data.npy'
    try:
        y = np.load(path).item()
    except:
        y = {}
    date_catch = '2018'
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
        context = pythex( datalist , str(chunhua)+month+day ) 
        #Regular expression的部分
        #bert轉譯
        filelist = []
        bc = BertClient()
        i = 0
        
        for article in context:
            if i == 0 :
                i += 1
                continue
            try:
                context_bert = bc.encode(article[2])
            except:
                context_bert = []
            topic_bert = bc.encode([article[0]])
            if context_bert == []:
                bert_news = topic_bert
            else:
                bert_news = np.append(topic_bert,context_bert,axis=0)
            #print(bert_news.shape)
            filelist.append(bert_news)
            #print("ok")
        #print(len(context))
        #print(len(filelist))
        save = {year+month+day:filelist}


        dict.update(y,save)
        
        if date_catch != year:
            date_catch = year
            print('save a year')
            np.save(path,y) #save the new

        

        
