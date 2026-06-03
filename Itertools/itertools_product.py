'''
Given two sorted lists A and B, output all possible pairs (a, b) - one element from A, 
one from B - in sorted order.
Example:
A = 1, 2, B = 3, 4
Output: (1, 3) (1, 4) (2, 3) (2, 4)
'''
from itertools import product

A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

print(*[str(t) for t in product(A, B)])
# The output of product is already tuples like (1, 3), so str(t) converts each to the exact format needed: (1, 3) (1, 4) (2, 3) (2, 4)
