möglich = 0
günstig = 0
for Münze1 in {"K","Z"}:
  for Münze2 in {"K","Z"}:
    for Münze3 in {"K","Z"}:
      for Münze4 in {"K","Z"}:
        for Münze5 in {"K","Z"}:
          möglich = möglich + 1
          # Eine Zeichenkette wird generiert:
          Ausgang = Münze1 + Münze2 + Münze3 + Münze4 + Münze5
          if Ausgang.count("K")==2:
            günstig = günstig + 1
print(f"{günstig} von {möglich}")
print(f"p = {günstig/möglich}")
