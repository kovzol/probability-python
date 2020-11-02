möglich = 0
Erwartungswert = 0
for Kopf1 in [0,1]:
  for Kopf2 in [0,1]:
    for Kopf3 in [0,1]:
      for Kopf4 in [0,1]:
        möglich += 1
        x = Kopf1 + Kopf2 + Kopf3 + Kopf4
        print(f"Ereignis={Kopf1}{Kopf2}{Kopf3}{Kopf4}, x={x}")
        Erwartungswert = Erwartungswert + x
Erwartungswert = Erwartungswert / möglich
print(f"E(X)={Erwartungswert}")
