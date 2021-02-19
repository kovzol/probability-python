import itertools
max_tosses = 4
for W in range(1, max_tosses + 1):
  Ω = set(itertools.product({1, 2, 3, 4, 5, 6}, repeat=W))
  sums = [0] * (max_tosses * 6 + 1)
  for ω in Ω:
    sums[sum(ω)] += 1
  probabilities = [h/len(Ω) for h in sums]
  print(probabilities)
