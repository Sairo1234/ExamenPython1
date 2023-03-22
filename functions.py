import csv
import math

#Ejercicio 2
def read_data(filename):
    """Esta funcion lee un fichero csv y devuelve un diccionario con los datos del fichero.

    Args:
        filename (text): nombre del fichero csv

    Raises:
        ValueError: Si el fichero tiene menos de 10 muestras con todos los atributos.

    Returns:
        diccionario: los datos del fichero csv
    """
    
    with open(filename, 'r') as file:
        
        reader = csv.DictReader(file)
        data = {}
        
        for row in reader:
            
            if all(row.values()):
                
                data[f'dato{len(data)+1}'] = {
                    'type': row['type'],
                    'fixed acidity': row['fixed acidity'],
                    'volatile acidity': row['volatile acidity'],
                    'citric acid': row['citric acid'],
                    'residual sugar': row['residual sugar'],
                    'chlorides': row['chlorides'],
                    'free sulfur dioxide': row['free sulfur dioxide'],
                    'total sulfur dioxide': row['total sulfur dioxide'],
                    'density': row['density'],
                    'PH': row['pH'],
                    'sulphates': row['sulphates'],
                    'alcohol': row['alcohol'],
                    'quality': row['quality']
                }
                
        if len(data) < 10:
            raise ValueError('El fichero debe tener al menos 10 muestras con todos los atributos.')
        
        return data

#Ejercicio 3
def split(data):
    """Esta funcion recibe un diccionario con los datos del fichero csv y devuelve dos diccionarios, uno con los datos del tipo white y otro con los datos del tipo red.

    Args:
        data (diccionario): diccionario con los datos del fichero csv

    Returns:
        diccionario: diccionario con los datos del tipo white
        diccionario: diccionario con los datos del tipo red
    """
    
    white = {}
    red = {}
    
    for i in data:
        
        if data[i]['type'] == 'white':
            white[i] = data[i]
            del white[i]['type']
            
        elif data[i]['type'] == 'red':
            red[i] = data[i]
            del red[i]['type']
            
    return white, red

#Ejercicio 4
def reduce(diccionario, atributo):
    """Esta funcion recibe un diccionario y un atributo y devuelve una lista con los valores de ese atributo.
    
    Args:
        diccionario (diccionario): diccionario con los datos del fichero csv
        atributo (str): nombre del atributo
    
    Returns:
        lista: lista con los valores del atributo
    """
    
    lista = []
    
    for i in diccionario:
        
        if atributo in diccionario[i]:
            lista.append(diccionario[i][atributo])
            
        else:
            raise ValueError('El atributo no existe en el diccionario.')
            
    return lista

#Ejercicio 5
def silhouette(lista1, lista2):
    """Esta funcion recibe dos listas y devuelve el coeficiente de Silhouette de la primera lista.

    Args:
        lista1 (lista): lista con los valores del atributo
        lista2 (lista): lista con los valores del atributo

    Returns:
        float: coeficiente de Silhouette de la primera lista
    """
    a = {}
    for i in range(len(lista1)):
        distances = []
        for j in range(len(lista1)):
            if i != j:
                distance = math.sqrt(abs(lista1[i] - lista1[j])**2)
                distances.append(distance)
    
    