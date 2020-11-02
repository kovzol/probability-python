möglich = 0
günstig = 0
for Augenzahl in [1,2,3,4,5,6]:
  möglich = möglich + 1
  if Augenzahl > 4:
    günstig = günstig + 1
print (f"{günstig} von {möglich}")
