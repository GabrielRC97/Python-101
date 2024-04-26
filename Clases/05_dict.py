'''
dict = {}
for i in range (1,11):
  dict[i] = i * 2

print(dict)

dict_2 = {i:i*2 for i in range (1,11)}
'''
'''
import random

countries = ['cl','arg','col','bol']
population = {}

for country in countries:
  population[country] = random.randint(1,100)

print (population)

population_v2 = {country:random.randint(1,100) for country in countries}

print (population_v2)
'''

names = ['nico','zule','santi']
ages = [12, 56,  98]

new_list = list(zip(names, ages))
print (new_list)

new_dict = {name:age for name, age in new_list}

print (new_dict)

new_dict_v2 = {names[i]:ages[i] for i in range(len(names))}

print (new_dict_v2)

new_dict_v3 = dict(zip(names, ages))
print(new_dict_v3)
