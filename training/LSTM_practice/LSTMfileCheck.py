from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb

import os

max_features = 20000 #最常見的20000字
# cut texts after this number of words (among top max_features most common words)
maxlen = 80 # 一個batch的文字量
batch_size = 32 #一次訓練丟進的batch量

print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features) #50000條分別丟入train和test裡
print(len(x_train), 'train sequences') #x每條都是一個影評；y是對應的好壞分類（1,0）
print(len(x_test), 'test sequences') 


print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen) #sequence.pad_sequences將序列切齊或補齊為同長度的訓練單位
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

"""
model = Sequential()
model.add(Embedding(max_features,128))
model.add(LSTM(128,dropout=0.2,recurrent_dropout=0.2))
model.add(Dense(1,activation='sigmoid'))
model.summary()

model.compile(loss = 'binary_crossentropy',
                optimizer ='adam',metrices =['accuracy'])
model.fit(x_train,y_train,batch_size=batch_size,epochs = 15,validation_data=(x_test,y_test))"""
