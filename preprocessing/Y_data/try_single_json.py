import json

from datetime import timedelta, date

start_date = date(2014, 3, 11)
end_date = date(2020, 1, 2)

year , month , day = end_date.strftime("%Y") , end_date.strftime("%m") , end_date.strftime("%d")
with open("../../json/"+year+"-"+month+"-"+day+".json",'r') as load_f:
    load_dict = json.load(load_f)
result = float(load_dict['2330']['close']) - float(load_dict['2330']['open'])
print(str(result))
