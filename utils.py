import csv
from datetime import datetime, timedelta

def load_csv(path):
    with open(path, 'r') as file:
        my_reader = csv.reader(file, delimiter=',')
        file = [x for x in my_reader]  
    return file

def parse_time(time):
    ''' , expected format 2021-09-02T05:50:00, expected todays_dat = '2021-09-02T00:00:00'''
    days = time[:10].split('-')
    times = time[-8:].split(':')
    
    return list(map(int,days + times))

def substract_lists(list_1,list_2):
    """ subscract two lists by elements"""
    
    return list(map(lambda x:x[0]-x[1],zip(list_1,list_2)))


def is_time_in_interval(time1,time2,minimum_delta_hours = 1 ,maximum_delta_hours = 6):
    ''' , expected format 2021-09-02T05:50:00, expected todays_dat = '2021-09-02T00:00:00'''
     
    time_a = datetime.fromisoformat(time1)    
    time_b = datetime.fromisoformat(time2)
    
    return ((time_b -time_a) < timedelta(hours=maximum_delta_hours) and (time_b -time_a) > timedelta(hours=minimum_delta_hours))
        
    
    