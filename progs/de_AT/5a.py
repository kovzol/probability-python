import itertools
Ω = list(itertools.product({"K", "Z"}, repeat=5))

# Ω wird in eine für unser Programm
# brauchbarere Form transformiert.
# Aus den Tupeln werden Zeichenketten (strings) gemacht.
Ω = {"".join(Ausgang) for Ausgang in Ω}
print(f"Ω={Ω}")

E = [ω for ω in Ω if ω.count("K") == 2]
print(f"E={E}")

print(f"{len(E)} von {len(Ω)}")
print(f"p = {len(E)/len(Ω)}")
