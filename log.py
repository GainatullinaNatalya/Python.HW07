from datetime import datetime as dt
from time import time
import datetime

def logger(mod):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{mod} - {str(datetime.datetime.now())} \n')

# def logger(rezhim):
#     time = dt.now().strftime('%H:%M')
#     with open('log.txt', 'w', encoding='utf-8') as file:
#         file.write('{};pressure;{}\n'
#                     .format(time, rezhim))
#
#
# def wind_speed_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write('{};wind_speed;{}\n'
#                     .format(time, data))