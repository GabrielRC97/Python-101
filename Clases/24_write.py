with open("Python 102/Clases/text.txt", 'r+') as file:
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo')
    file.write("\nnueva linea")
    file.write("\notra linea mas")
