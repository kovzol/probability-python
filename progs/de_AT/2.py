möglich = 0
günstig = 0
for Augenzahl_Würfel_1 in [1,2,3,4,5,6]:
  for Augenzahl_Würfel_2 in [1,2,3,4,5,6]:
    möglich = möglich + 1
    if Augenzahl_Würfel_1 + Augenzahl_Würfel_2 == 10:
      günstig = günstig + 1
print(f"{günstig} von {möglich}")
print(f"p = {günstig/möglich}")
