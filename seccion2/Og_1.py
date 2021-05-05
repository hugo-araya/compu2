print ("calculadora de hijos de primate")

r = int(input("Ingrese la cantidad de hijos de la mano derecha: "))
l = int(input("Ingrese la cantidad de hijos de la mano izquierda: "))

if r <= 5 and l <= 5:
    suma = r + l
    print ("la cantidad de hijos es : ", suma)
else:
    print("error")
