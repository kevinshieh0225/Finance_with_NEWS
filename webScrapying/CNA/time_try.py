from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 1, 1)
end_date = date(2020, 3, 17)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y%m%d"))
year , month , day = end_date.strftime("%Y") , end_date.strftime("%m") , end_date.strftime("%d")
print(str(year)+str(month)+str(day))