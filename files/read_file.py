import os
import time
import pandas

# myfile = open('c:/Users/daniq/Desktop/PYTHON-UDEMY/curso-python-udemy/files/fruits.txt', 'r')
# content = myfile.read() # Lee el contenido del archivo
# myfile.close() # Cierra el archivo

while True:
    if os.path.exists('c:/Users/daniq/Desktop/PYTHON-UDEMY/curso-python-udemy/files/fruits.txt'):
        with open('c:/Users/daniq/Desktop/PYTHON-UDEMY/curso-python-udemy/files/fruits.txt', 'r') as myfile:
            content = myfile.read() 
            print(content)
    else:
        print('File does not exist')
    time.sleep(10) # Pausa de 10 segundos

