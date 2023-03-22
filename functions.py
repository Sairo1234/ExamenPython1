import csv

#Ejercicio 2
def read_data(filename):
    """Esta funcion lee un fichero csv y devuelve un diccionario con los datos del fichero.

    Args:
        filename (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
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


file = 'winequality.csv'
data = read_data(file)
