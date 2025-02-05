import time
import os
import pandas

while True:
    if os.path.exists('c:/Users/daniq/Desktop/PYTHON-UDEMY/curso-python-udemy/files/temps_today.csv'):
        data = pandas.read_csv('c:/Users/daniq/Desktop/PYTHON-UDEMY/curso-python-udemy/files/temps_today.csv')
        print(data.mean())
    else:
        print('File does not exist')
    time.sleep(10)