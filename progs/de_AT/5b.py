import itertools
Ω = set(itertools.product({"K", "Z"}, repeat=5))
Erwartungswert = 0
for ω in Ω:
  Erwartungswert = Erwartungswert + ω.count("K")
Erwartungswert = Erwartungswert / len(Ω)
print(f"Erwartungswert = {Erwartungswert}")
