import itertools
Ω = set(itertools.product({"h", "t"}, repeat=5))
E = 0
V = 0
for ω in Ω:
  x = ω.count("h")
  E = E + x
  V = V + x*x
E = E / len(Ω)
V = V / len(Ω) - E*E
print(f"expected value = {E}")
print(f"variance = {V}")
