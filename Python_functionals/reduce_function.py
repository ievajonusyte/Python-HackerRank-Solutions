from fractions import Fraction
from functools import reduce
'''
You are given a list of rational numbers (fractions). Your job is to find their product and print it in its simplest form.
Input:the first line contains an integer n - the number of fractions. Each of the next n lines contains two integers: the numerator and denominator of one fraction.
Output:print two integers on one line - the numerator and denominator of the final product, reduced to lowest terms (no common divisors other than 1).
'''

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)  # multiply all fractions together one by one
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())): # read n fractions from input
        fracs.append(Fraction(*map(int, input().split()))) # split each line into numerator and denominator
    result = product(fracs) # Fraction automatically simplifies as you go
    print(*result) # print numerator and denominator separated by space
