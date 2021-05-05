datos = "datos"
arch = open(datos)
for linea in arch:
    linea = linea.rstrip("\n")
    lista = linea.split()
    L = int(lista[0])
    R = int(lista[1])
    if (L == 0 and R == 0):
        print('No tiene hijos')
        break
    else:
        suma = L + R
        print("Suma : ", suma)