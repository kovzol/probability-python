import itertools
Ω = set(itertools.product({"h", "t"}, repeat=5))
expected_value = 0
for ω in Ω:
  expected_value = expected_value + ω.count("h")
expected_value = expected_value / len(Ω)
print(f"expected value = {expected_value}")
