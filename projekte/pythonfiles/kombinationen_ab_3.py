from math import factorial

# sei eine Menge M mit n Elementen
# script berechnet wie viele Teilmengen dieser Menge einen Betrag von groesser gleich 3 haben(anzahlMoeglichkeitenTeilmengen) und vergleicht diese anzahl mit der anzahl der benoetigten anzahl an teilmengen(2**n-1)

n = 10

for n in range(10000):
    anzahlMoeglichkeitenTeilmengen = 0

    benoetigteTeilmengen = float(2**(n-1))
    # print("benoetigte Teilmengen: ", benoetigteTeilmengen)

    def Binomialkoeffizient(n, k):
        binomialkoeffizient = factorial(n)/(factorial(k)*factorial(n-k))
        return binomialkoeffizient

    # for element in range(4, n+1):
        # anzahlMoeglichkeitenTeilmengen += Binomialkoeffizient(n, element)

    # print(anzahlMoeglichkeitenTeilmengen)

    anzahlMoeglichkeitenTeilmengen = 0
    # sei n-2 Teilmengen haben die Elemente a und b, 2 Elemente haben nur a oder nur b, wie viele Kombinationen gibt es jetzt?

    for element in range(1, n-1):
        anzahlMoeglichkeitenTeilmengen += Binomialkoeffizient(n-2, element)

    # print(anzahlMoeglichkeitenTeilmengen+2)

    if benoetigteTeilmengen > anzahlMoeglichkeitenTeilmengen:
        print("alles gut")
    else:
        print("error")
