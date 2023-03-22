import csv
#

function read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        data = {}
        for i, row in enumerate(reader):
            
                        
print("hola")