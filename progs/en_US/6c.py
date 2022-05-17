import itertools
Ω = set(itertools.product({"h", "t"}, repeat=5))
possible_values = [0, 1, 2, 3, 4, 5]
# In the beginning each value of the random variable
# has a frequency of 0.
heads = [0]*len(possible_values)
for ω in Ω:
  heads[ω.count("h")] += 1
probabilities = [h/len(Ω) for h in heads]
print(list(zip(possible_values, probabilities)))
