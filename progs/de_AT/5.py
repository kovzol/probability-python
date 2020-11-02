import itertools
# 1. Mathematische Grundmenge Ω besteht aus lauter 5-elementigen Tupeln, wobei K für Kopf und
#    Z für Zahl steht. Jeder Buchstabe im Tupel repräsentiert den Ausgang einer geworfenen Münze.
Ω = set(itertools.product({"K", "Z"}, repeat=5))
print(Ω)

# 2. Ω wird in eine für unser Programm brauchbarere Form transformiert. Aus den Tupeln werden
#    Zeichenketten (strings) gemacht.
Ω = {"".join(Ausgang) for Ausgang in Ω}
print(Ω)

# 3. Anzahl der günstigen und möglichen Ausgänge bestimmen:
günstig = 0
möglich = len(Ω)
for Ausgang in Ω:
    if Ausgang.count("K") == 2:
        günstig = günstig + 1

# 4. Ausgabe:
print(f"{günstig} von {möglich}")
print(f"p = {günstig/möglich}")

