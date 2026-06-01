'''
Task: Convert complex number z to polar coordinates.
Input: One line - a complex number (e.g. 1+2j)
Output:

Line 1: r - modulus (abs(z))
Line 2: phi - phase angle in radians (phase(z))
'''
from cmath import phase

z = complex(input())
print(abs(z))
print(phase(z))

'''
complex() parses the input string directly
abs() gives the modulus
phase() from cmath gives the angle
'''
