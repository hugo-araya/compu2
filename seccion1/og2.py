auxiliar = 0
while (auxiliar == 0):
    hijas = int(input("Ingrese la cantidad de hijas"))
    hijos = int(input("Ingrese la cantidad de hijos"))
    total = hijas+hijos
    print("Og tiene", total, "hijos/as")

    if hijas == 0 and hijos == 0:
        auxiliar = 1