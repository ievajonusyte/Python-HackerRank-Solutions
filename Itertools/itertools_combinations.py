from itertools import combinations
'''
Given string S and integer k, print ALL combinations of sizes 1 up to k in lexicographic order, one per line.
'''

line = input().split()
S = sorted(line[0])
k = int(line[1])
# split input, sort the string for lexicographic order, convert k to integer

for size in range(1, k + 1): # loop through all sizes 1 to k
    for c in combinations(S, size): 
        #c ombinations(S, size) generates all unique selections of that size. Since S is sorted, output is already in lexicographic order. ''.join(c) converts the tuple to a string.
        print(''.join(c))
