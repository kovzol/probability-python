import itertools
Ω = set(itertools.product({"K", "Z"}, repeat=5))
E = 0
V = 0
for ω in Ω:
  x = ω.count("K")
  E = E + x
  V = V + x*x
E = E / len(Ω)
V = V / len(Ω) - E*E
print(f"Erwartungswert = {E}")
print(f"Varianz = {V}")
