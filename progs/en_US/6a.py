import itertools
Ω = set(itertools.product({"h", "t"}, repeat=5))
E = 0
for ω in Ω:
  E = E + ω.count("h")
E = E / len(Ω)
V = 0
for ω in Ω:
  V = V + (ω.count("h")-E)**2
V = V / len(Ω)
print(f"expected value = {E}")
print(f"variance = {V}")
