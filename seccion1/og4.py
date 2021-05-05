print ("ingrese numero de hijos: ")
L = int(input())
print ("ingrese numero de hijas: ")
R = int(input())
if L>=0 and  R >=0:  # != L>0 and R > 0
    Totaldehijos = L + R
    print("Total de hijos: ", Totaldehijos)

if L==0 and R==0:
    print("No tiene hijos")
