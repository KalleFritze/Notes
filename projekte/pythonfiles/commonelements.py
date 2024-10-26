lista1 = []
lista2= []
    
listtogether = []

aone1 = 37
aone2 = 26

limit = 1000

def commonElements(aOne,lista,measure):
    lista.append(aOne)
    i=1
    oldelementa = aOne
    for k in range(measure):
        newelementa=i*oldelementa + 1
        lista.append(newelementa)
        i+=1
        oldelementa = newelementa
    #print(lista)
    #print(listb)
    #print(listtogether)
    return lista

lista1 = commonElements(aone1,lista1, limit)
lista2 = commonElements(aone2, lista2, limit)


for a in lista1:
    for b in lista2:
        if a==b:
            if a not in listtogether:
                listtogether.append(a)



print(aone1, aone2)
print(listtogether)