'''
You have K lists of numbers. Pick one number from each list. Square each picked number, sum them all up, then take mod M. Find the highest possible result.
'''
from itertools import product

K, M = map(int, input().split()) # K - number of lists, M - the modulo value
lists = []
for _ in range(K):
    row = list(map(int, input().split()))
    lists.append(row[1:])  
    # Each line starts with N_i (how many elements follow) - we skip it with row 1 and just keep the actual numbers.

best = 0
for combo in product(*lists): 
    # product(*lists) generates every possible combination of picking one element from each list. So if you have 3 lists, each combo is a tuple like 5, 9, 10 one pick per list.
    s = sum(x**2 for x in combo) % M
    best = max(best, s)
    # For each combination: square every picked number, sum them, mod M. If it beats the current best, save it.
print(best)
