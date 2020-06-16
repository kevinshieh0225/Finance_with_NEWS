import json

from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2014, 3, 11)
end_date = date(2020, 3, 1)
Output = {}
for single_date in daterange(start_date, end_date):
    year , month , day = single_date.strftime("%Y") , single_date.strftime("%m") , single_date.strftime("%d")
    try:
        with open("../../json/"+year+"-"+month+"-"+day+".json",'r') as load_f:
            load_dict = json.load(load_f)
    except:
        continue
    else:
        Output.update({ year+month+day :  load_dict['2330']})
with open('./Y_raw_data.json', 'w') as fp:
    json.dump(Output, fp)

