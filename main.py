
from functions import read_data, split, reduce

#testear la funcion read_data

file = 'winequality.csv'
data = read_data(file)

#testear la funcion split
diccionario_white, diccionario_red = split(data)
#print(diccionario_white)

#testear la funcion reduce
lista = reduce(diccionario_white, 'alcohol')
print(lista)