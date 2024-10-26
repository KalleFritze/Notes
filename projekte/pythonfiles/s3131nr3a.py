

lista = []
listb = []
listtogether = []

aOne = 4
bOne = 2

lista.append(aOne)
listb.append(bOne)

i=1
oldelementa = aOne
oldelementb = bOne

for k in range(100000):
    newelementa=i*oldelementa + 1
    newelementb=i*oldelementb - 1
    lista.append(newelementa)
    listb.append(newelementb)
    i+=1
    oldelementa = newelementa
    oldelementb = newelementb

for a in lista:
    for b in listb:
        if a==b:
            if a not in listtogether:
                listtogether.append(a)
print(aOne, bOne)
#print(lista)
#print(listb)
print(listtogether)


