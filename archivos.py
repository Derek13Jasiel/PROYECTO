

f = open("texto.txt","r")
nombre = "Miguel"
dpi = "4060"

for line in f:

    hola = line.split('-')
    if nombre == hola[0] and dpi == hola[1]:
        print("si se puedo")
        print(hola[0])
        print(hola[1])

f.close()











    





