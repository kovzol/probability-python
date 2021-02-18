import itertools
# 1. The basic set:
outcomes = {1, 2, 3, 4, 5, 6}
# itertools.product creates a Cartesian product:
Ω = set(itertools.product(outcomes, outcomes))
print(Ω)
# Note that Ω as a set and it is unsorted.
# Instead of "set" we can use a "list":
# in that case the data will be sorted.

# 2. Count the amount of desired and total outcomes:
desired = 0
total = len(Ω)
for outcome_die_1, outcome_die_2 in Ω:
  if outcome_die_1 + outcome_die_2 == 10:
    desired = desired + 1

# 3. Output:
print(f"{desired} of {total}")
print(f"p = {desired/total}")
