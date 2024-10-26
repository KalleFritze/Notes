from math import factorial


def Binomialkoeffizient(n, k):
    binomialkoeffizient = factorial(n)/(factorial(k)*factorial(n-k))
    return (binomialkoeffizient)


m = 40


def Todeskombinationen(n, y, f):
    x = n-y
    # anzahlTodeskombo = (y-f)*Binomialkoeffizient((x+f),2)+x*Binomialkoeffizient((y-f), 2)+Binomialkoeffizient((y-f), 3)+f*f*(x-f)+2*f*Binomialkoeffizient(f, 2)
    try:
        anzahlTodeskombo1 = (y-f)*Binomialkoeffizient((n-y+f), 2)
    except ValueError:
        anzahlTodeskombo1 = 0
    try:
        anzahlTodeskombo2 = x*Binomialkoeffizient((y-f), 2)
    except ValueError:
        anzahlTodeskombo2 = 0
    try:
        anzahlTodeskombo3 = Binomialkoeffizient((y-f), 3)
    except ValueError:
        anzahlTodeskombo3 = 0
    try:
        anzahlTodeskombo4 = 2*f*Binomialkoeffizient(f, 2)
    except ValueError:
        anzahlTodeskombo4 = 0

    anzahlTodeskombo = anzahlTodeskombo1+anzahlTodeskombo2 + \
        anzahlTodeskombo3+anzahlTodeskombo4 + f*f * (x-f)

    return (anzahlTodeskombo)


lowestvalues = []

for k1 in range(m+1):
    lowestvalues_k1 = []
    # print(" ")
    # print(" ")
    # print("n= ", k1)

    for k2 in range(1, k1):
        all_dreierkombos = []
        for s in list(range(1, k1-1)):
            for l in range(s+1, k1):
                for t in range(l+1, k1+1):
                    all_dreierkombos.append([s, l, t])

        # print(" ")
        # print("y = " ,k2, " gesamt dreierkombinationen, die von y Mengen abgedeckt werden können: ",len(all_dreierkombos) )
        highestvalue = 0
        f_highestvalue = 0
        lowestvalue = len(all_dreierkombos)
        f_lowestvalue = 0

        for k3 in range(k2+1):
            anzahlTodeskombinationen = Todeskombinationen(k1, k2, k3)
            if anzahlTodeskombinationen > highestvalue:
                highestvalue = anzahlTodeskombinationen
                f_highestvalue = k3
            if anzahlTodeskombinationen <= lowestvalue:
                lowestvalue = anzahlTodeskombinationen
                f_lowestvalue = k3

            # print("f =" ,k3,": ", anzahlTodeskombinationen)

        lowestvaluecouple = [f_lowestvalue, lowestvalue, k2]
        # print("highest value f was: ", f_highestvalue," with value of ", highestvalue)
        # print("lowest value f was: ",  f_lowestvalue, " with value of ", lowestvalue)

        lowestvalues_k1.append(lowestvaluecouple)
    print("")
    print("n =",  len(lowestvalues_k1)+1)
    for x in lowestvalues_k1:
        print("y=", x[2], ": ", "f=", x[0], "value =",  x[1])
        # if x[0] != x[2]:
        # print("y=", x[2], ": ", "f=", x[0])
