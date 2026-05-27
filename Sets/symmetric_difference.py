'''
Problem:
Given two sets M and N, find all values that exist in either M or N, but NOT in both. Print them in ascending order, one per line.
Example:

M = {2, 4, 5, 9}
N = {2, 4, 11, 12}
Both contain 2 and 4 exclude those
Result: 5, 9, 11, 12 printed sorted
'''

# Read M
m = int(input())           # size of set M (not really needed)
a = set(map(int, input().split()))  # reads space-separated numbers, converts to int, puts in a set for M

# Read N
n = int(input())           # size of set N (not really needed)
b = set(map(int, input().split()))  # reads space-separated numbers, converts to int, puts in a set for N


for val in sorted(a ^ b): # a ^ b Symmetric difference: elements in a OR b, but not both, sorted(...) returns a sorted list of those elements, for val in ...: print(val) prints each one on its own line
    print(val)
