limit = 100length_of_rows = 10

list_commonElements = []


def commonElements(aOne, bOne, measure):
    lista = []
    listb = []
    listtogether = []
    lista.append(aOne)
    listb.append(bOne)

    i = 1
    oldelementa = aOne
    oldelementb = bOne

    for k in range(measure):
        newelementa = i*oldelementa + 1
        newelementb = i*oldelementb - 1
        lista.append(newelementa)
        listb.append(newelementb)
        i += 1
        oldelementa = newelementa
        oldelementb = newelementb

    for a in lista:
        for b in listb:
            if a == b:
                if a not in listtogether:
                    listtogether.append(a)
    # print(lista)
    # print(listb)
    # print(listtogether)
    return listtogether


myOutputFile = open("commonelements.txt", "w")
myOutputFile.writelines("common elements")
myOutputFile.close()


for a1 in range(1, limit):
    a1_list = []
    myOutputFile = open("commonelements.txt", "a")
    myOutputFile.writelines("\n a1="+str(a1)+":")
    myOutputFile.close()
    for b1 in range(1, limit):
        a1_list.append(commonElements(a1, b1, length_of_rows))
        myOutputFile = open("commonelements.txt", "a")
        myOutputFile.writelines("[")
        myOutputFile.writelines(
            [str(i)+"," for i in commonElements(a1, b1, length_of_rows)])

        # myOutputFile.writelines(" (")
        # myOutputFile.writelines(str(b1))
        # myOutputFile.writelines(")")

        myOutputFile.writelines("]")
        myOutputFile.close()
    list_commonElements.append(a1_list)
    # print(a1_list)


# print(list_commonElements)

myInputFile = open("commonelements.txt", "r")

for line in myInputFile.readlines():
    print(line),

myInputFile.close()
