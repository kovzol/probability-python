import itertools
Ω = list(itertools.product({"h", "t"}, repeat=5))
print(f"Ω={Ω}")
E = [ω for ω in Ω if ω.count("h") == 2]
print(f"E={E}")
print(f"{len(E)} of {len(Ω)}")
print(f"p = {len(E)/len(Ω)}")
