import itertools

def X(ω):
    """Studenten können diese Funktion selbst programmieren.
    X ist Zufallsvariable, also X: Ω → ℝ.
    Einem Ergebnis wird eine reelle Zahl zugeordnet."""
    return ω[0]+ω[1]

Augenzahlen = {1, 2, 3, 4, 5, 6}
Ω = list(itertools.product(Augenzahlen, Augenzahlen))
# Ereignis E
E = []
for ω in Ω:
    if X(ω) == 10:
        E.append(ω)
print(f"{len(Ω)} mögliche Ergebnisse")
print(f"{len(E)} günstige Ergebnisse")
print(f"p = {len(E)/len(Ω)}")
