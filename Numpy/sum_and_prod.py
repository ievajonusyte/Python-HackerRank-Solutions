import numpy

'''
Sum and Prod

Compute the sum along axis 0 of a 2-D array, then print the
product of that sum.

Sample Input:
2 2
1 2

Sample Output:
2+1=3, 2+2=4 3x4=12
'''


n, m = map(int, input().split()) #read N (rows) and M (columns)

my_array = numpy.array([input().split() for _ in range(n)], dtype=int) 
#input().split() reads one line of text and splits it into a list of strings by spaces. So if the line is "1 2", this gives you ['1', '2']
#input().split() for _ in range(n)] is a list comprehension - it repeats input().split() exactly n times, and collects each result into a list
#numpy.array(..., dtype=int)takes that list of lists and converts it into a proper 2-D numpy array, casting all the string values to integers


print(numpy.prod(numpy.sum(my_array, axis=0)))

#numpy.sum(my_array, axis=0)sums down the columns, numpy.prod multiplies
