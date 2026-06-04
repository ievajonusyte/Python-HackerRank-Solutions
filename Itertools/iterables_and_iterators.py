from itertools import combinations
'''
You have a bag of letters. You randomly pick K of them. 
What is the chance that at least one of the picked letters is 'a'
'''

n = int(input()) # how many letters there are (N)
letters = input().split() # the letters themselves
k = int(input()) # how many you pick (K)

all_combos = list(combinations(range(n), k)) # all ways to pick K indices
a_indices = {i for i, letter in enumerate(letters) if letter == 'a'} # positions of 'a'

has_a = sum(1 for combo in all_combos if any(i in a_indices for i in combo)) # count combos with at least one 'a'


print(round(has_a / len(all_combos), 4))
