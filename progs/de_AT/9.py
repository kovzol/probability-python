import itertools
Ω = set(itertools.product({"K", "Z"}, repeat=5))
print(Ω)

# Ω wird in eine für unser Programm brauchbarere Form transformiert.
# Aus den Tupeln werden Zeichenketten (strings) gemacht.
Ω = {"".join(Ausgang) for Ausgang in Ω}
print(Ω)

günstig = 0
möglich = len(Ω)
for Ausgang in Ω:
    if Ausgang.count("K") == 2:
        günstig = günstig + 1

print(f"{günstig} von {möglich}")
print(f"p = {günstig/möglich}")

