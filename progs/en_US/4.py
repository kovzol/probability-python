import itertools

def X(ω):
    """Students could edit this function on their own.
    X is a rendom variable, that is, X: Ω → ℝ.
    A real number will be mapped to each outcome."""
    return ω[0]+ω[1]

outcomes = {1, 2, 3, 4, 5, 6}
Ω = list(itertools.product(outcomes, outcomes))
# Event E
E = []
for ω in Ω:
    if X(ω) == 10:
        E.append(ω)
print(f"{len(Ω)} total outcomes")
print(f"{len(E)} desired outcomes")
print(f"p = {len(E)/len(Ω)}")
