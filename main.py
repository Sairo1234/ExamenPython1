
from functions import read_data, split, reduce, silhouette

#testear la funcion read_data

file = 'winequality.csv'
data = read_data(file)

#testear la funcion split
diccionario_white, diccionario_red = split(data)
#print(diccionario_white)

#testear la funcion reduce
lista1 = reduce(diccionario_white, 'alcohol')
lista2 = reduce(diccionario_white, 'density')

#testear la funcion silhouette
res = silhouette(lista1, lista2)
print(res)

#esta ultima funcion me da error, salta la excepcion de que hay un problema con el primer diccionario
#creo que los calculos están bien, pero no se como solucionarlo