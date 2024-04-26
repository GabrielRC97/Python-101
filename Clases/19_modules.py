import sys

print(sys.path)

import re

text = 'mi numero de telefono es +5694812345 mi codigo de pais es 56 y mi numero de la suerte es el 7'
print(re.findall('[0-9]+', text))

import time

timestamp = time.time()
print (timestamp)

local = time.localtime()
result = time.asctime(local)
print (result)

import collections

numbers = [1,2,1,2,3,4,1,4,2,43,5,3,4,1,23,4,12,2,3,1,2,4,2]

counter = collections.Counter(numbers)
print (counter)