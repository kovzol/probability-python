total = 0
desired = 0
for outcome_die_1 in [1,2,3,4,5,6]:
  for outcome_die_2 in [1,2,3,4,5,6]:
    total = total + 1
    if outcome_die_1 + outcome_die_2 == 10:
      desired = desired + 1
print(f"{desired} of {total}")
print(f"p = {desired/total}")
