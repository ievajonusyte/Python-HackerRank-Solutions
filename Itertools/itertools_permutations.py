'''
Given a string S and integer k, print all permutations of size k in lexicographic (alphabetical) sorted order, one per line. Example: S = "HACK", k = 2 - all 2-letter arrangements like AC, AH, AK, CA...
'''

from itertools import permutations

line = input().split() # we take the string and the number separately
S = sorted(line[0]) # list with the first item, this ensures alphabetical order in output
k = int(line[1]) # list with the 2nd item

for p in permutations(S, k): # permutations(S, k) generates all k-length arrangements
    print(''.join(p))
