e = 0
while e == 0:
    L = int(input("Hijos de Og (L): "))
    R = int(input("Hijas de Og (R): "))

    if L >= 0 and L < 6 and R >= 0 and R < 6:
        suma = L + R
        print("La cantidad de hijos de og es de: ", suma)
        e = 0
    if L >= 6 or R >= 6:
        e = 1
        print("Og no tiene tantos dedos")
    if L == 0 and R == 0:
        print("Og no tiene hijos")
        e = 1