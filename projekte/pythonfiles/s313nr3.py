
limit = 10
length_of_rows= 10

list_commonElements = []

def commonElements(aOne,bOne,measure):
    lista = []
    listb = []
    listtogether = []
    lista.append(aOne)
    listb.append(bOne)

    i=1
    oldelementa = aOne
    oldelementb = bOne

    for k in range(measure):
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
    #print(lista)
    #print(listb)
    #print(listtogether)
    return listtogether


for l in range(1,limit):
    for k in range(1,limit):
        print(l,k)
        print(commonElements(l,k,length_of_rows))
        list_commonElements.append(commonElements(l,k,length_of_rows))


print(list_commonElements)
