from regular_expression import daterange , getParagragh , pythex 
import re
import csv
from datetime import timedelta, date
from bert_serving.client import BertClient
import json
import numpy as np
import os.path

year , month , day = '2016','05','01'
locate = './../../webScrapying/CNA/DATA/'+year+'/'+year+'_'+month+'/'+year+month+day+'.csv'
datalist = getParagragh(locate)


chunhua = '105'
context = pythex( datalist , str(chunhua)+month+day ) 
#Regular expression的部分
#bert轉譯
filelist = []
bc = BertClient()
i = 0


context_bert = bc.encode(context[1][2])
topic_bert = bc.encode([context[1][0]])
print(context_bert[0][0])
print(len(context_bert))
print(context_bert.shape)
print('')
print(topic_bert[0][0])
print(len(topic_bert))
print(topic_bert.shape)
bert_news = np.append(topic_bert,context_bert,axis=0)
print(bert_news[0][0])
print(len(bert_news))
print(bert_news.shape)
filelist.append(bert_news)
#print("ok")
save = {year+month+day:filelist}