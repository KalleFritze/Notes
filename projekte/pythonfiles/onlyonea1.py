
limit = 100
length_of_rows= 10
a1range= [3, 4, 5]

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
def Writingb1directly():
        myOutputFile.writelines(" (")
        myOutputFile.writelines(str(b1))
        myOutputFile.writelines(")")



myOutputFile= open("commonelements.txt", "w")
myOutputFile.writelines("common elements")
myOutputFile.close()



for a1 in a1range:
    print("a1 = ", a1)
    a1_list = []
    myOutputFile = open("commonelements.txt", "a")
    myOutputFile.writelines("\n a1="+str(a1)+":")
    myOutputFile.close()
    for b1 in range(1,limit):
        common_elements = commonElements(a1, b1, length_of_rows)

        if len(common_elements)!= 0:
            print(common_elements, b1)

        myOutputFile = open("commonelements.txt", "a")
        myOutputFile.writelines("[")
        myOutputFile.writelines([str(i)+"," for i in commonElements(a1, b1, length_of_rows)])

        #Writingb1directly()

        myOutputFile.writelines("]")
        myOutputFile.close()






myInputFile = open("commonelements.txt", "r")

for line in myInputFile.readlines():
    print(line),

myInputFile.close()



