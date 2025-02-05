with open('c:/Users/daniq/Desktop/PYTHON-UDEMY/curso-python-udemy/files/fruits.txt', 'a+') as myfile:
    myfile.write('Tomatoes\nPeppers\nOnions\n')
    myfile.seek(0)
    content = myfile.read()

print(content)
