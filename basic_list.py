temps = [221, 234, 340, -9999, 230]

# Lista sin comprensiones
'''
new_temps = [] 
for temp in temps: 
    new_temps.append(temp / 10)
'''

# LISTA DE COMPRENSIONES CON CONDICION

# Se agrega cada elemento a la lista nueva, siendo diviso por 10 si el elemento es diferente a -9999
# Si el elemento es -9999 se añade 0 a la lista nueva
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

