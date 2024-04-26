def increment(x):
  return x + 1

result = increment (10)
print (result)

increment_v2 = lambda x : x + 1

result = increment_v2(10)
print (result)

full_name = lambda name, last : f'full name is {name.capitalize()} {last.capitalize()}'

text = full_name('gabriel', 'rodriguez')
print (text)