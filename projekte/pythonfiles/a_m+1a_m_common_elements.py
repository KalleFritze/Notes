

lista1 = []
lista2 = []
listtogether = []

a1One = 3
a2One = 4

lista1.append(a1One)
lista2.append(a2One)

i=1
oldelementa = a1One
oldelementb = a2One

for k in range(1000):
    newelementa=i*oldelementa + 1
    newelementb=i*oldelementb + 1
    lista1.append(newelementa)
    lista2.append(newelementb)
    i+=1
    oldelementa = newelementa
    oldelementb = newelementb

for a in lista1:
    for b in lista2:
        if a==b:
            if a not in listtogether:
                listtogether.append(a)
print(a1One, a2One)
#print(lista1)
#print(lista2)
print(listtogether)


