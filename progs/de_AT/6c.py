import itertools
Ω = set(itertools.product({"K", "Z"}, repeat=5))
mögliche_Werte = [0, 1, 2, 3, 4, 5]
# Zu Beginn hat jeder mögliche Wert der Zufallsvariablen
# eine Häufigkeit von 0.
Anzahl_Köpfe = [0]*len(mögliche_Werte)
for ω in Ω:
    Anzahl_Köpfe[ω.count("K")] += 1
Wahrscheinlichkeiten = [h/len(Ω) for h in Anzahl_Köpfe]
print(list(zip(*(mögliche_Werte, Wahrscheinlichkeiten))))
