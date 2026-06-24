import numpy

'''
Read two arrays of Nx P and MxP, then concatenate them along axis 0 (stacking rows).
'''

n, m, p = map(int, input().split()) #  reads the dimensions: N rows for array_1, M rows for array_2, P columns shared by both
array_1 = numpy.array([input().split() for _ in range(n)], int) # reads n lines of input, splits each into numbers, and stacks them into one integer NumPy array
array_2 = numpy.array([input().split() for _ in range(m)], int) 

print(numpy.concatenate((array_1, array_2), axis=0))
