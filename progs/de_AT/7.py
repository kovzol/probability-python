import itertools
max_Würfe = 4
Anzahl_Köpfe = [[0] * (max_Würfe * 7)] * (max_Würfe + 1)
for W in range(1, max_Würfe + 1):
    Ω = set(itertools.product({1, 2, 3, 4, 5, 6}, repeat=W))
    for ω in Ω:
        Anzahl_Köpfe[W][sum(ω)] += 1
    Wahrscheinlichkeiten = [h/len(Ω) for h in Anzahl_Köpfe[W]]
    print(Wahrscheinlichkeiten)
