#EJERCICIO

'''
Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria.

Ejemplo

Input: data.csv
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output:
60
'''

#PUNTO DE PARTIDA

'''
import csv

def read_csv(path):
   # Tu código aquí 👇
   total = 0
   return total

response = read_csv('./data.csv')
print(response)
'''

#DESARROLLO

import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path,'r') as csvfile:
    reader = dict(csv.reader(csvfile, delimiter=','))
    sum = 0
    for key in reader:
      sum += int(reader[key])
    return sum


    #total = 0
    #return total

response = read_csv(r'Python 102\Playground\data.csv')
print(response)