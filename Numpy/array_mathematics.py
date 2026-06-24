import numpy

'''
Given two integer arrays A and B of dimensions N x M, perform the
following operations in order and print each result:
1. Add (A + B)
2. Subtract (A - B)
3. Multiply (A * B)
4. Integer Division (A / B)
5. Mod (A % B)
6. Power (A ** B)
Use numpy.floor_divide() for integer division.
'''

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(a + b)
print(a - b)
print(a * b)
print(numpy.floor_divide(a, b))
print(a % b)
print(a ** b)
