import numpy

'''
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.

Input Format
The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.


Sample Input
1.1 2 3
0

Sample Output
3.0
'''

coefficients = numpy.array(input().split(), dtype=float)
# reads the first line, splits it by spaces, and converts everything into a float numpy array. These are the polynomial's coefficients, ordered from highest degree to lowest.
x = float(input())
# reads the second line and converts it to a float, this is the point where we want to evaluate the polynomial.
print(numpy.polyval(coefficients, x))
# numpy.polyval(coefficients, x) evaluates the polynomial at that point
