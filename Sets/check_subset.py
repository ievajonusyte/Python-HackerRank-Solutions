'''
The Problem
Given T test cases, for each one:

You get set A and set B
Print True if A is a subset of B
Print False if not

T              - number of test cases
n              - number of elements in A
a1 a2 a3...    - elements of A
m              - number of elements in B
b1 b2 b3...    - elements of B
'''
T = int(input()) # read number of test cases

for _ in range(T): # repeat T times
    n = int(input()) # read size of A (we don't actually need n)
    a = set(map(int, input().split())) # read A as a set of numbers
    m = int(input()) # read size of B (we don't actually need m either)
    b = set(map(int, input().split())) # read B as a set of numbers
    
    print(a.issubset(b)) # print True or False
