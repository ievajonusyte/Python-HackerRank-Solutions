from itertools import groupby
'''
Group consecutive identical characters in a string and output each group as (count, digit), separated by spaces.
'''

s = input()
print(' '.join(f'({len(list(g))}, {int(k)})' for k, g in groupby(s)))

'''
groupby(s) groups consecutive identical characters, so "1222311" becomes groups of 1, three 2s, one 3, two 1s
len(list(g)) counts how many items are in each group
int(k) converts the character to a number
joining with spaces formats the final output
'''
