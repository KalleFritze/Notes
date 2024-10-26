1. Berechnung der moeglichen Kombinationen bei y = 1, f=0:

Ansatz: Anzahl der moeglichen Teilmengen in Schnittmenge + 2Mengen, die sich nicht in der Schnittmenge befinden (die zahl der 2 mengen ist sowieso festgesetzt, hier muessen also keine Kombinationen berechnet werden, sie muss auch nicht in die Berechnung der anderen KOmbinationen miteinbezogen werden, da die Mengen sich per definition immer von jeder menge in der Schnittmenge unterscheiden werden)



in code (kombinationen_ab_3.py):


    anzahlMoeglichkeitenTeilmengen = 0
    # sei n-2 Teilmengen haben die Elemente a und b, 2 Elemente haben nur a oder nur b, wie viele Kombinationen gibt es jetzt?

    for element in range(1, n-1):
        anzahlMoeglichkeitenTeilmengen += Binomialkoeffizient(n-2, element)

    # print(anzahlMoeglichkeitenTeilmengen+2)

    if benoetigteTeilmengen > anzahlMoeglichkeitenTeilmengen:
        print("alles gut")
    else:
        print("error")

