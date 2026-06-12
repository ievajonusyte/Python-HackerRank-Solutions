import math

'''
You are given two complex numbers C and D.
Print the result of their addition, subtraction, multiplication,
division and modulus operations, each on a separate line.
Real and imaginary parts should be correct to two decimal places.

Input: two lines, each with two floats (real and imaginary parts).
Output: 6 lines - C+D, C-D, C*D, C/D, mod(C), mod(D)
'''

# A class to represent a complex number, e.g. 3 + 4
class Complex(object):
    # Store the real and imaginary parts when a Complex object is created
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    # Called when you write x + y
    # Add real to real, imaginary to imaginary
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    # Called when you write x - y
    # Subtract real from real, imaginary from imaginary
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    
    # Called when you write x * y
    # Uses the expanded bracket rule, plus the fact that i*i = -1
    # real part = real*real - imaginary*imaginary
    # imaginary part = real*imaginary + imaginary*real
    def __mul__(self, no):
        return Complex(
            self.real * no.real - self.imaginary * no.imaginary,
            self.real * no.imaginary + self.imaginary * no.real
        )
    # Called when you write x / y
    # denominator is real*real + imaginary*imaginary of the bottom number
    # the numerator formulas are fixed rules for complex division
    def __truediv__(self, no):
        denominator = no.real**2 + no.imaginary**2
        return Complex(
            (self.real * no.real + self.imaginary * no.imaginary) / denominator,
            (self.imaginary * no.real - self.real * no.imaginary) / denominator
        )
    # Modulus means the size/distance of the number from zero
    # Uses Pythagoras: sqrt(real*real + imaginary*imaginary)
    # Returns a Complex with imaginary=0 because the result is a plain number
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    # Called when you print or str() a Complex object
    # Handles four cases to make sure the sign looks correct
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
