file = open("Python 102/Clases/text.txt")

'''
print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
'''

for line in file:
    print(line)


file.close()

with open("Python 102/Clases/text.txt") as file:
    for line in file:
        print(line)