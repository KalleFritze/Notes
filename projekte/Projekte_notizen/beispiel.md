Sei y = 1, f = 1


Nach [[Lemma0]] hat jede Teilmenge midestens drei Elemente (drei verbindende Elemente)
Mit dieser Einschraenkung gibt es P(n)= B(n, 4)+B(n, 5)+B(n, 6)+...+B(n, n) Moeglichkeiten an Teilmengen, die untereinander verbindbar sein koennten
Es muss 2^n-1 Teilmengen geben

2^n-1 ist in manchen faellen kleiner als P(n): 
sei n = 6
=> es gibt genauso viele Teilmengen mit mindestens 3 elementen wie Teilmengen insgesamt benoetigt werden

es benoetigt also mehr Einschraenkungen:



Hypothese 1.
sei in einer Kombination haben k Teilmengen sowohl element a, als auch element b: Schnittmenge von Xa und Xb hat einen Betrag von k
je groesser diese Schnittmenge, desto weniger moegliche Kombinationen gibt es fuer die Teilmengen, da mindestens k Teilmengen a und b enthalten muessen

beispiel: sei das gegebene beispiel n=6, ya, yb = 1, f=0: alle Teilmengen, ausser zweien, enthalten die selben zwei Elemente, was die Menge der Kombinationen einschraenkt
hier die Rechnung, um die Kombinationsanzahl zu bestimmen:  [beispielRechnungen](beispielRechnungen)

wenn die Schnittmenge bei der Berechnung mit einbezogen wird, zumindest bei der besonderen konfiguration des beispiels, ist  es bis n=1000 so, dass die Moeglichkeiten immer weniger sind, als die benoetigte Menge, die Hypothese geht also auf
hier die berechnung:


moegliche Einschraenkungen: je kleiner Die Schnittmenge zwischen den Xs zweier Elemente, desto mehr weitere Elemente werden benoetigt, um alle Elemente zu verbinden





[generalisierung dieses Ansatzes](Lemma1.md)
hypothese 1: sei die beispielkonfiguration y = 1, f=0, es gilt also: jede ausser zwei Teilmengen beinhaltet sowohl a, als auch  b, die zwei Teilmengen beinhalten
			nur a, bzw nur b
		-die Anzahl der moeglichen Teilmengen, die beide Elemente haben plus die beiden Teilmengen, die nur ein element haben ueberschreitet dabei niemals
		2^(n-1)
		
sei hypothese 1 ist wahr fuer jedes n

goal: egal wie diese beispielkonfiguration veraendert wird, die grundhypothese steht immer noch

Wege die grundhypothese zu veraendern, sodass alle Teilmengen verbunden bleiben:
[1](1). [f veraendern](fveraender)
2. [x veraendern](xveraendern)
3. [teile von x auf andere Elemente verschieben](xverschieben)

es soll bewiesen werden, dass man diese veraenderungen beliebig oft, in beliebiger Reihenfolge ausfuehren kann, ohne dass dabei die Anzahl der moeglichen Teilmengen steigt, bzw, dass die anzahl der moeglichen Teilmengen nicht 2^(n-1) ueberschreitet

zusammengefasst: finde die Konfiguration, die die meisten Kombinationen bietet, beweise dass sie die meisten Kombinationen bietet und zeige dann, dass diese Kombinationsanzahl trotzdem unter den geforderten Teilmengen liegt
