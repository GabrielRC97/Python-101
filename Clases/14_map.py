numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
  numbers_v2.append(i*2)

numbers_v3 = list(map(lambda i : i * 2, numbers))

print (numbers)
print (numbers_v2)
print (numbers_v3)

numbers_2 = [5,6,7]

result = list(map(lambda x, y : x + y, numbers, numbers_2))

print(numbers)
print(numbers_2)
print(result)


text = 'hola mundo'
result = list(map(lambda x : x.upper() , text))

result = "".join(result)

print(result)


