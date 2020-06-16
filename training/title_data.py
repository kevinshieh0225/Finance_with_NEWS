#!/usr/bin/env python3
"""
需求格式為：(x_train, y_train), (x_test, y_test)
X.shape = (768,100)
y.shape = int
"""
import re
import csv
from datetime import timedelta, date
import json
import numpy as np
import os.path

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def construct_Y_data(number):
    if number > 5:return 1
    elif number < -5:return -1
    else: return 0

def load_data(X_route,Y_route):

    X_data = np.load(X_route).item()
    with open(Y_route, 'r') as f:
        Y_data = json.load(f)

    x_train, y_train = [],[]
    x_test, y_test = [],[]

    global date
    start_date = date(2014, 3, 11)
    end_date = date(2020, 3, 17)
    switch_bit = 0 #0 train;1 test
    for single_date in daterange(start_date, end_date):
        year , month , day = str(single_date.strftime("%Y")) , str(single_date.strftime("%m")) , str(single_date.strftime("%d"))
        date = year+month+day
        print(date)
        try:
            Y_data[date]
            X_data[date]
        except:continue

        if switch_bit == 0:
            x_train.append(X_data[date])
            y_train.append(construct_Y_data(Y_data[date]))
            switch_bit = 1
        else:
            x_test.append(X_data[date])
            y_test.append(construct_Y_data(Y_data[date]))
            switch_bit = 0
    return (x_train, y_train), (x_test, y_test)