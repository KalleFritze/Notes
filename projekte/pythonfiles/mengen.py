from math import factorial

n = 4
f = 1
y = 1
x = n-y


all_dreierkombo = []


# berechnet alle möglichen dreierkombinationen bei n verschiedenen Teilmengen
for k in list(range(1, n-1)):
    print(" ")
    for l in list(range(k+1, n)):
        for m in range(l+1, n+1):
            all_dreierkombo.append([k, l, m])
            print("(", k, l, m, ")")

# die Menge der möglichen Dreierkombos an Teilmengen
print(len(all_dreierkombo))


# berechnet die Anzahl der Kombinationen, die weder durch p1, noch durch p2 verbunden werden koennen und darum ein p3 benoetigen

def Binomialkoeffizient(n, k):
    binomialkoeffizient = factorial(n)/(factorial(k)*factorial(n-k))
    return (binomialkoeffizient)


try:
    anzahlP3Kominationen1 = (y-f)*Binomialkoeffizient((n-y+f), 2)
except ValueError:
    anzahlP3Kominationen1 = 0
try:
    anzahlP3Kombinationen2 = x*Binomialkoeffizient((y-f), 2)
except ValueError:
    anzahlP3Kombinationen2 = 0
try:
    anzahlP3Kombinationen3 = Binomialkoeffizient((y-f), 3)
except ValueError:
    anzahlP3Kombinationen3 = 0
try:
    anzahlP3Kombinationen4 = 2*f*Binomialkoeffizient(f, 2)
except ValueError:
    anzahlP3Kombinationen4 = 0

anzahlp3Kombinationen = anzahlP3Kominationen1+anzahlP3Kombinationen2 + \
    anzahlP3Kombinationen3+anzahlP3Kombinationen4 + f*f * (x-f)


print(anzahlp3Kombinationen)
