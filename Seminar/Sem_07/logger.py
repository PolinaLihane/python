from datetime import datetime as dt
from time import time


def info(l_info):
    d_time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(d_time, l_info)