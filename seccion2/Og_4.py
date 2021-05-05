ar= open("hijos.txt")
ar2= open("hijos.out","w")
lr=[]
for linea in ar:
    linea = linea.rstrip("\n")
    linea=linea.split(" ")
    lr.append([linea[0], linea[1]])
print (lr)

for elem in lr:
    l=int(elem[0])
    r=int(elem[1])
    l_r=(l+r)
    l_r=str(l_r)

    if l<=5 and r <= 5:
        if r>=0 and l >=0 :
            ar2.write(l_r+"\n")
    else:
        ar2.write((" "))

ar2.close()
ar.close()

