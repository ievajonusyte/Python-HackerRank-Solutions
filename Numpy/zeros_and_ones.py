import numpy

'''
Read a shape (3 3 3 in the sample) and print an array of that shape filled with zeros, then ones, as integers.
'''
dims = list(map(int, input().split())) #holding the shape you want for ex.3x3x3

print(numpy.zeros(dims, dtype=int)) # numpy.zeros(dims, ...) creates an array with that exact shape, filled entirely with 0
print(numpy.ones(dims, dtype=int))
