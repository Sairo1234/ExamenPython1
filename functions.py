import csv

def read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            break
    
    
file = 'winequality.csv'
read_data(file)