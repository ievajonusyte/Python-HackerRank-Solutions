from itertools import combinations_with_replacement

'''
Given string S and integer k, print all size-k combinations where a letter can be used more than once.
'''

line = input().split() # split input into string S and integer k
S = sorted(line[0]) # sort string for lexicographic order
k = int(line[1]) # convert k to integer

for c in combinations_with_replacement(S, k):
    print(''.join(c)) # join tuple ('A','A') into string 'AA'
    # generate all size-k combinations allowing repeats and print each
