'''
Task: Given 2 integers (a, b), print three lines - integer division, modulo, then divmod tuple
Input: 2 numbers, each on a separate line
Output:

Line 1: a // b (integer quotient)
Line 2: a % b (remainder)
Line 3: divmod(a, b) (both as a tuple)
'''

a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))
