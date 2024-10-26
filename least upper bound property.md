**bounded above**
a subset A° of an [[ordered set]] A is bounded above iff there is at least one b element A that is bigger or equal than every element of A°
$$
(A° \textnormal{is bounded above} ) \iff \exists b \in A(\forall x \in A°(x \leqslant b))
$$
Every such b is called an upper bound of A°
Sei B the set of all upper bounds of A°
Sei b° the smallest element of that set.
b° is the least upper bound of A°
b° may or may not belong to A°.

**least upper bound property**
An ordered set A has the least upper bound property iff every nonempty subset A° of A that is bounded above has a least upper bound.

$$
\textnormal{(A has the least upper bound property)} \iff \forall A° \subseteq A(( (A\ne \emptyset)\implies((\exists b \in A(\forall x \in A°(x \leqslant b))\implies \textnormal{A has a least upper bound})
$$

greates lower bound property:

**bounded below:**
sei A is an [[ordered set]], sei A° $\subseteq$ A

A° is bounded below $\iff$ $\exists$b$\in$A($\forall$x$\in$A°(x$\ge$b))
b is an upper bound of A° $\iff$ $\forall$x$\in$A°(x$\ge$b)

greatest lower bound
sei b° das größte Element aus A, sodass alle elemente aus A° kleiner als b° sind.
	$\implies$ b° kann auch selbst ein element aus A° sein, bspw wenn das größte Element aus A° auch das größte Element aus A ist.

**greatest lower bound property**
An ordered set A has the greatest lower bound property iff every nonempty subset A° of A that is bounded above has a greatest lower bound.

sei A eine geordnete Menge
sei A hat die greates lower bound property

=>   $\forall$A°$\in$A(A°$\ne$$\emptyset$$\implies$(A° is bounded above$\implies$A°has a greatest lower bound))












Nicht definitionsrelevante Notizen zu greates lower bound/least upper bound property
Frage:
Kann es sein, dass the greatest lower bound kein element von A° ist?

-jede Teilmenge A° von einer Menge A, das bounded below ist, hat auch ein kleinstes Element $\implies$ dieses kleinste Element ist das greates lower bound
						Das greatest lower bound ist also immer ein Element von A°

sei G={b:bis an lower bound of A°}
sei d das kleinste Element von A°
=> $\forall$x$\in$A°(d$\le$x)
=> d$\in$G
es gibt kein größeres lower bound von A°, da d das kleinste Element ist
$\implies$d is the greates lower bound of A°



