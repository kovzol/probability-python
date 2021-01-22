import itertools
Ω = set(itertools.product({"K", "Z"}, repeat=5))
E = 0
for ω in Ω:
  E = E + ω.count("K")
E = E / len(Ω)
V = 0
for ω in Ω:
  V = V + (ω.count("K")-E)**2
V = V / len(Ω)
print(f"Erwartungswert = {E}")
print(f"Varianz = {V}")
