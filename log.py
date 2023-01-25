
import datetime

def logger(rezhim):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{rezhim} - {str(datetime.datetime.now())} \n')
