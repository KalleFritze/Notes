genereller möglicher beweisablauf

wie viele dreiermengen, von denen sich Elemente auch in anderen Teilmengen befinden müsste es geben, um am ende die nötige anzahl von 2^n-1 kompatiblen Teilmengen zu erreichen?
goal: es ist unmöglich diese anzahl von unterschiedlichen dreiermengen zu erreichen

Achtung: die dreiermengen müssen nicht kompatibel untereinander sein, nur muss jedes element in ihnen auch in einer anderen dreiertielmenge vorhanden ein





jede menge braucht drei Elemente
gibt es aber Beschränkungen für die position dieser Elemente?

sei s1 hat das element a, b, c
sei s2 hat das element a


case1 
sei s2 hat weder b noch c
sk hat a nicht
es muss also ein element d geben, sodass d in s1, s2 und sk
demnach s1 hat a, b, c, d
	s2 hat a, d
	sk hat d

s2 hat noch mindestens ein element e
sk hat noch mindestens zwei Elemente f1 und f2

alle weiteren Teilmengen s3, s4, s5, ... 





case2 sei s2 hat b

case3 sei s2 hat b und c




annahme1: 
je kleiner die maximale anzahl ist mit der eine Teilmenge Elemente teillt, desto mehr Elemente, die sie mit anderen Teilmengen teilt, enthaelt sie

die maximale anzahl der Teilmengen, mit der eine Teilmenge ein element teilen kann ist n-1
dafür benötigt sie mindestens drei Elemente

sei die maximahle anzahl der Teilmengen ist n-2
sei a in s1, sei a nicht in s2, sei b nicht in s2
(s1, s2, sk) nicht über a kompatibel
es gibt ein c, sodass c in s1 und s2 (und sk)


	sei annahme 1 ist wahr: je weniger Teilmengen sich ein element teilen, desto mehr Elemente benötigt jedes element
	sei max k Teilmengen teilen sich ein element(element 1), die Kombinationsmöglichkeiten für die weiteren Elemente dieser Teilmengen verringert sich 
	sei k-r teilmengen teilen sich ein weiteres element(element2), 

	sei max k teilmengen teilen sich ein element
	-- sie enthalten demnach jeweils mindestens f(k) elemente
	goal: kombinationen größer gleich k sind weniger als 





annahme2:
sei s1 hat a, b
je weniger Teilmengen ebenfalls a und b haben, desto mehr element insg müssen die Teilmengen haben

sei s1 hat a
je mehr teilmengen ebenfalls a haben, desto


sei Q die Mengen der teilmengen, die nicht p1 haben, sei X die Menge der Teilmengen, die p1 haben
alle mengen in Q müssen mit den anderen teilmengen verbunden werden

sei Q wird aufgeteilt in Teilmengen Q1, Q2 ,....Qn, sodass alle Mengen in Qi ein gemeinsames Element haben.

nach ann



-midestens ein p2 um 




zwischen beweis:
 sei zwei Mengen an Teilmengen
je weniger Teilmengen in der einen Menge ein gem. Element haben, desto mehr elemente braucht die andere Menge um sich mit den anderen Teilmengen zu verbinden

