import numpy

n, m = map(int, input().split()) # reads the first line and gets the dimensions
arr = numpy.array([input().split() for _ in range(n)], int) # reads n more lines, each split into a list of strings

print(arr.transpose()) # swaps rows and column
print(arr.flatten()) # collapses the array into one dimension, in row-major order
