def find_volume(length = 1,width = 1,depth = 1):
  return length * width * depth, width, 'hola'

result, width, string = find_volume (depth=3)
print (result)
print (width)
print (string)