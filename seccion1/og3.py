from os import system
system("clear")

contador = 1
while contador > 0:
    L = int(input("ingrese la cantidad de HIJOS que tiene og: "))
    R = int(input("ingrese la cantidad de HIJAS que tiene og: "))  
    if L == 0 and R == 0:
        print ("Og no tiene hijos")
        contador = 0
    if L >= 1 and R >= 1:
        if L <= 5 and R <= 5: 
            suma = L + R
            print(" OG tiene en total: ", suma, "hijos")
