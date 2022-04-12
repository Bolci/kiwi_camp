import csv
from datetime import datetime, timedelta

def load_csv(path):
    with open(path, 'r') as file:
        my_reader = csv.reader(file, delimiter = ',')
        file = [x for x in my_reader]

    return file

def is_time_in_interval(time1,time2,time_range_in_hours):
    ''' , expected format 2021-09-02T05:50:00, expected todays_dat = '2021-09-02T00:00:00'''

    time_a = datetime.fromisoformat(time1)    
    time_b = datetime.fromisoformat(time2)
    
    return ((time_b - time_a) < timedelta(hours = time_range_in_hours[1]) and (time_b - time_a) > timedelta(hours = time_range_in_hours[0]))

def time_to_iso(time_delta):
    return "{}:{}:{}{}".format(time_delta.seconds//3600,(time_delta.seconds%3600)//60,
                               ((time_delta.seconds%3600)%60)//10,((time_delta.seconds%3600)%60)%10)

def get_time_interval(time1,time2):
    time_a = datetime.fromisoformat(time1)    
    time_b = datetime.fromisoformat(time2)
    
    return time_to_iso((time_a - time_b))

def is_time_bigger(time1,time2):
    ''' copare if time1 if bigger than time2'''
    time_a = datetime.fromisoformat(time1)    
    time_b = datetime.fromisoformat(time2)

    return time_a > time_b
    