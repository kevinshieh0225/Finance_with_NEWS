#!/usr/bin/env python3
from __future__ import print_function
from title_data import load_data, daterange
from datetime import timedelta, date

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Activation

import os

if __name__ == '__main__':

    # cut texts after this number of words (among top max_features most common words)
    maxlen = 80 # 一個訓練單位的句字量
    batch_size = 5 #一次訓練丟進的batch量

    print('Loading data...')
    X_route = './../preprocessing/X_data/save_topic_training_data.npy'
    Y_route = './../preprocessing/Y_data/Y_data.json'
    (x_train, y_train), (x_test, y_test) = load_data(X_route,Y_route) #50000條分別丟入train和test裡
    print(len(x_train), 'train sequences') #x每條都是一個影評；y是對應的好壞分類（1,0）
    print(len(x_test), 'test sequences') 

    
    print('Pad sequences (samples x time)')
    x_train = sequence.pad_sequences(x_train, maxlen=maxlen) #sequence.pad_sequences將序列切齊或補齊為同長度的訓練單位
    x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
    print('x_train shape:', x_train.shape)
    print('x_test shape:', x_test.shape)

    print('Build model...')
    model = Sequential()
    
    model.add(Flatten(input_shape = (80,768)))
    model.add(Dense(128,kernel_initializer='normal', activation='relu'))
    model.add(Dense(50,kernel_initializer='normal', activation='relu'))
    model.add(Dense(1,kernel_initializer='normal', activation='softmax'))

    # try using different optimizers and different optimizer configs
    model.compile(loss='binary_crossentropy',
                optimizer='adam', # 調整learning rate 數值
                metrics=['accuracy']) 

    print('Train...')
    model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=15,
            validation_data=(x_test, y_test))
    score, acc = model.evaluate(x_test, y_test,
                                batch_size=batch_size)
    print('Test score:', score)
    print('Test accuracy:', acc)
