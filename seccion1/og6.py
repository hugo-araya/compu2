cont = 0
while cont == 0:
    l = int(input("Indicar numero de hijos de Og: "))
    r = int(input("Indicar numero de hijos de Og: "))
    suma = l + r
    print("La cantidad total de hijos e hijas es: ", suma)
    if suma == 0:
        cont = 1
        print("Og no tiene hijos")
