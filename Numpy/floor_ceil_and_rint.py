import numpy
numpy.set_printoptions(legacy='1.13')

'''
Floor, Ceil and Rint

Print the floor, ceil, and rint of all elements in array A.
floor rounds down, ceil rounds up, rint rounds to nearest.

Sample Input:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Sample Output:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
[ 1.  2.  3.  4.  6.  7.  8.  9. 10.]
'''

my_array = numpy.array(input().split(), dtype=float)
# input().split() reads the input line and splits it into a list of strings by spaces
# numpy.array(..., dtype=float) - converts that list of strings into a numpy array of floats

print(numpy.floor(my_array)) # rounds every element down
print(numpy.ceil(my_array)) # rounds every element up
print(numpy.rint(my_array)) # rounds every element to nearest
