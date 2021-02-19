import itertools
max_dice = 4
for d in range(1, max_dice + 1):
  Ω = set(itertools.product({1, 2, 3, 4, 5, 6}, repeat=d))
  sums = [0] * (max_dice * 6 + 1)
  for ω in Ω:
    sums[sum(ω)] += 1
  probabilities = [h/len(Ω) for h in sums]
  print(probabilities)
