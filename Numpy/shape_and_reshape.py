import numpy
'''
You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.
'''
my_array = numpy.array(input().split(), int)
print(numpy.reshape(my_array, (3, 3)))
