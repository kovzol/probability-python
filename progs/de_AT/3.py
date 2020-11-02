import itertools
# 1. Grundmenge erstellen:
Augenzahlen = {1, 2, 3, 4, 5, 6}
# itertools.product liefert das kartesische Produkt:
Ω = set(itertools.product(Augenzahlen, Augenzahlen))
print(Ω)
# Beachte, dass Ω als Menge nicht sortiert ist.

# 2. Anzahl Günstige und Mögliche bestimmen:
günstig = 0
möglich = len(Ω)
for Augenzahl1, Augenzahl2 in Ω:
  if Augenzahl1 + Augenzahl2 == 10:
    günstig = günstig + 1

# 3. Ausgabe:
print(f"{günstig} von {möglich}")
print(f"p = {günstig/möglich}")
