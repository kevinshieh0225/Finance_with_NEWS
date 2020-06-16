#!/usr/bin/env python3

from bert_serving.client import BertClient
from regular_expression import daterange , getParagragh , pythex 
import re
import csv
from datetime import timedelta, date
import json
import numpy as np
import os.path

if __name__ == '__main__':
    bc = BertClient()
    locate = './../../webScrapying/CNA/DATA/2018/2018_07/20180718.csv'
    datalist = getParagragh(locate)
    chunhua = 107
    context = pythex( datalist , '1070718' ) 
    #Regular expression的部分
    #bert轉譯
    filelist = []
    bc = BertClient()
    i = 0
    
    for article in context:
        if i == 0 :
            i += 1
            continue
        i+=1
        print(str(i))
        try:
            context_bert = bc.encode(article[2])
        except:
            context_bert = []
        print(context_bert.shape)
        topic_bert = bc.encode([article[0]])
        print(topic_bert.shape)
        bert_news = np.append(topic_bert,context_bert,axis=0)
        print(bert_news.shape)
        filelist.append(bert_news)
        #print("ok")
    #print(len(context))
    #print(len(filelist))