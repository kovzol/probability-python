möglich = 0
Erwartungswert = 0
Varianz = 0
for Kopf1 in [0,1]:
  for Kopf2 in [0,1]:
    for Kopf3 in [0,1]:
      for Kopf4 in [0,1]:
        möglich += 1
        x = Kopf1 + Kopf2 + Kopf3 + Kopf4
        Erwartungswert = Erwartungswert + x
        Varianz = Varianz + x*x
Erwartungswert = Erwartungswert/möglich
Varianz = Varianz/möglich - Erwartungswert*Erwartungswert
print(f"E(X)={Erwartungswert}, V(X)={Varianz}")
