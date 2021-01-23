import itertools
import matplotlib.pyplot as p
max_Würfe = 4
for W in range(1, max_Würfe + 1):
    Ω = set(itertools.product({1, 2, 3, 4, 5, 6}, repeat=W))
    Augensummen = [0] * (max_Würfe * 6 + 1)
    for ω in Ω:
        Augensummen[sum(ω)] += 1
    Wahrscheinlichkeiten = [h / len(Ω) for h in Augensummen]
    p.plot(range(1, max_Würfe * 6 + 1), Wahrscheinlichkeiten[1:])
p.show()
