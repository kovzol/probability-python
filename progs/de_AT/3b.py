import itertools

def X(ω):
    """Studenten könnten diese Funktion selbst programmieren.
    X ist Zufallsvariable, also X: Ω → ℝ.
    Einem Ergebnis wird eine reelle Zahl zugeordnet."""
    return ω[0]+ω[1]

Augenzahlen = {1, 2, 3, 4, 5, 6}
# Ergebnisraum Ω ist hier eine Menge an Paaren, wobei der erste (zweite) Eintrag
# die Augenzahl des ersten (zweiten) Würfels ist.
Ω = list(itertools.product(Augenzahlen, Augenzahlen))
# Ereignis E
E = []
for ω in Ω:
    if X(ω) == 10:
        E.append(ω)
# "Anzahl der Möglichen" ist die Mächtigkeit des Ergebnisraumes
print(f"{len(Ω)} mögliche Ergebnisse")
# "Anzahl der Günstigen" ist die Mächtigkeit des Ereignisses
print(f"{len(E)} günstige Ergebnisse")
print(f"p = {len(E)/len(Ω)}")
